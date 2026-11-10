"""Verify preserved code/data and English active documentation without changing files."""
import argparse
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def verify(root=ROOT, tree=None):
    expected = json.loads((root / "SOURCE-FILES.json").read_text(encoding="utf-8"))
    if tree is None:
        output = subprocess.check_output(
            ["git", "ls-tree", "-r", "-z", "HEAD"], cwd=root
        )
        tree = {}
        for record in output.split(b"\0"):
            if record:
                metadata, path = record.split(b"\t", 1)
                mode, kind, sha = metadata.decode("ascii").split()
                if kind == "blob":
                    tree[path.decode("utf-8")] = sha
    missing = [path for path, sha in expected.items() if tree.get(path) != sha]
    if missing:
        raise SystemExit("Changed or missing source files:\n" + "\n".join(missing))
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".rst"} and ".git" not in path.parts:
            content = path.read_text(encoding="utf-8-sig")
            if re.search(r"[\u0400-\u04ff]", content):
                raise SystemExit(f"Non-English active documentation: {path.relative_to(root)}")
            if path.suffix.lower() == ".md" and content.count(chr(96) * 3) % 2:
                raise SystemExit(f"Unclosed Markdown code fence: {path.relative_to(root)}")
    print(f"Verified {len(expected)} preserved code/data files and English active documentation.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tree-json", type=Path,
                        help="Use a recorded GitHub tree for offline verification")
    args = parser.parse_args()
    tree = None
    if args.tree_json:
        snapshot = json.loads(args.tree_json.read_text(encoding="utf-8"))
        assert not snapshot.get("truncated"), "The recorded tree is incomplete."
        tree = {entry["path"]: entry["sha"] for entry in snapshot["tree"] if entry["type"] == "blob"}
    verify(tree=tree)


if __name__ == "__main__":
    main()
