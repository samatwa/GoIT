"""Import pinned GoIT snapshots without changing any source repository."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import argparse
import json
import os
import subprocess

ROOT = Path(__file__).resolve().parents[1]
def run(*args, cwd=ROOT, data=None, check=True):
    p = subprocess.run(["git", "-c", "core.longpaths=true", *args], cwd=cwd,
                       input=data, capture_output=True, timeout=900)
    if check and p.returncode:
        raise RuntimeError(f"git {args[0]} failed: " + p.stderr.decode("utf-8", "replace")[-1000:])
    return p.stdout.decode("utf-8", "replace").strip()

def get_source(source, cache):
    name, commit = source["name"], source["commit"]
    folder = cache / (name + ".git")
    env = os.environ.copy()
    env.update(GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="Never")
    if not (folder / "HEAD").exists():
        result = subprocess.run(["git", "-c", "credential.helper=", "clone", "--bare", "--depth=1",
                                 "--single-branch", "--branch", source["branch"], source["url"], str(folder)],
                                capture_output=True, env=env, timeout=900)
        if result.returncode:
            raise RuntimeError(name + ": " + result.stderr.decode("utf-8", "replace")[-500:])
    exists = subprocess.run(["git", "--git-dir", str(folder), "cat-file", "-e", commit],
                            capture_output=True, env=env)
    if exists.returncode:
        run("--git-dir", str(folder), "-c", "credential.helper=", "fetch", "--depth=1", source["url"], commit)
    actual_tree = run("--git-dir", str(folder), "rev-parse", commit + "^{tree}")
    if actual_tree != source["tree"]:
        raise RuntimeError(name + ": source tree mismatch")
    return folder

def write_indexes(sources):
    groups = {}
    for source in sources:
        groups.setdefault(str(Path(source["destination"]).parent).replace("\\", "/"), []).append(source)
    for group, items in sorted(groups.items()):
        title = group.removeprefix("").replace("/", " / ")
        folder = ROOT / group
        folder.mkdir(parents=True, exist_ok=True)
        rows = [f"# {title}", "", "| Project | Source history |", "| --- | --- |"]
        for item in sorted(items, key=lambda x: x["name"].lower()):
            rows.append(f'| [{item["name"]}]({item["name"]}/) | [Original repository]({item["web_url"]}) |')
        (folder / "README.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    (ROOT / "Python").mkdir(parents=True, exist_ok=True)
    (ROOT / "Python/README.md").write_text(
        "# Python\n\n- [Basics](Basics/)\n- [Web Development](WebDevelopment/)\n", encoding="utf-8")
    (ROOT / "Capstone").mkdir(parents=True, exist_ok=True)
    (ROOT / "Capstone/README.md").write_text(
        "# Capstone\n\n- [Activation Functions: ResNet and Transformer](../DeepLearning/vkuznetsov-capstone-project/)\n\n"
        "The project is stored in Deep Learning; this entry provides a second navigation route.\n", encoding="utf-8")
    categories = ["Python", "Algorithms", "ComputerSystems", "HTML-CSS", "JavaScript", "React", "NodeJS",
                  "Databases", "DataEngineering", "MachineLearning", "DeepLearning", "MLOps", "DevOps", "Capstone"]
    labels = {"ComputerSystems": "Computer Systems", "HTML-CSS": "HTML and CSS", "NodeJS": "Node.js",
              "DataEngineering": "Data Engineering", "MachineLearning": "Machine Learning",
              "DeepLearning": "Deep Learning"}
    (ROOT / "README.md").write_text("# GoIT\n\n84 coursework repositories organized by subject.\n\n" +
        "\n".join(f"- [{labels.get(c, c)}]({c}/)" for c in categories) +
        "\n\nImported files retain their original content and filenames. Source repositories retain their full histories.\n",
        encoding="utf-8")
    report = ["# Import Verification", "",
              "Each imported project subtree is compared with its pinned source Git tree.", "",
              "| Project | Destination | Files | Source commit | Tree verification |",
              "| --- | --- | ---: | --- | --- |"]
    for s in sources:
        report.append(f'| {s["name"]} | {s["destination"]} | {s["file_count"]} | '
                      f'[{s["commit"][:12]}]({s["web_url"]}/commit/{s["commit"]}) | Exact match |')
    (ROOT / "IMPORT-REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8")

def verify(sources, tree):
    count = 0
    for source in sources:
        imported = run("rev-parse", tree + ":" + source["destination"])
        if imported != source["tree"]:
            raise RuntimeError(source["name"] + ": imported subtree differs from its source")
        paths = run("ls-tree", "-r", "--name-only", imported).splitlines()
        if len(paths) != source["file_count"]:
            raise RuntimeError(source["name"] + ": file count differs")
        count += len(paths)
    print(f"Verified {len(sources)} source trees and {count} files; all hashes match.", flush=True)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache-root", type=Path)
    parser.add_argument("--verify-only", action="store_true")
    parser.add_argument("--push", action="store_true")
    args = parser.parse_args()
    sources = json.loads((ROOT / "sources.json").read_text(encoding="utf-8"))
    if len(sources) != 84 or len({s["destination"] for s in sources}) != len(sources):
        raise RuntimeError("Expected exactly 84 distinct GoIT projects")
    for s in sources:
        dest = Path(s["destination"])
        if dest.is_absolute() or ".." in dest.parts or len(dest.parts) < 2:
            raise RuntimeError("Invalid destination")
        if not s["url"].startswith("https://github.com/samatwa/"):
            raise RuntimeError("Unexpected source owner")
    if args.verify_only:
        verify(sources, "HEAD")
        return

    cache = (args.cache_root or ROOT / ".git/import-cache").resolve()
    cache.mkdir(parents=True, exist_ok=True)
    folders = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        tasks = {pool.submit(get_source, s, cache): s for s in sources}
        for i, future in enumerate(as_completed(tasks), 1):
            folders.append(future.result())
            print(f'{i}/84 ready: {tasks[future]["name"]}', flush=True)
    alternates = ROOT / ".git/objects/info/alternates"
    alternates.parent.mkdir(parents=True, exist_ok=True)
    existing = alternates.read_text(encoding="utf-8").splitlines() if alternates.exists() else []
    alternates.write_text("\n".join(sorted(set(existing + [str(p / "objects").replace("\\", "/")
                                                              for p in folders]))) + "\n", encoding="utf-8", newline="\n")
    base_files = run("ls-files", "-z").split("\0")
    prefixes = tuple(s["destination"] + "/" for s in sources)
    for source in sources:
        current = run("rev-parse", "--verify", "HEAD:" + source["destination"], check=False)
        if current and current != source["tree"]:
            raise RuntimeError(source["name"] + ": existing project was modified; refusing to overwrite")
    base_files = [p for p in base_files if p and not p.startswith(prefixes)]
    run("read-tree", "--empty")
    for source in sources:
        run("read-tree", "--prefix=" + source["destination"] + "/", source["commit"])
    write_indexes(sources)
    generated = ["README.md", "Python/README.md", "Capstone/README.md", "IMPORT-REPORT.md"]
    generated += [str(Path(s["destination"]).parent / "README.md").replace("\\", "/") for s in sources]
    run("add", "-f", "--", *sorted(set(base_files + generated)))
    tree = run("write-tree")
    verify(sources, tree)
    diff = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT)
    if diff.returncode:
        run("commit", "-m", "Organize 84 GoIT projects by subject and retain exact source snapshots")
    else:
        print("The organized snapshot is already up to date.", flush=True)
    verify(sources, "HEAD")
    if args.push:
        run("push", "origin", "HEAD:main")
        print("Published organized projects to GitHub.", flush=True)

if __name__ == "__main__":
    main()

