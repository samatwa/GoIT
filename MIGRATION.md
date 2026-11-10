# Repository migration

Verified on November 10, 2026.

## Layout

- [GoIT](https://github.com/samatwa/GoIT): all 84 coursework projects, grouped by subject.
- [Pets](https://github.com/samatwa/Pets): personal applications, with Streamlit projects under `Streamlit/`.

## Preserved Git histories

Before removing any original repository, all advertised Git refs of the 62 non-Pages sources were copied to this repository. [HISTORY-MANIFEST.json](HISTORY-MANIFEST.json) records the original and destination refs and exact object SHAs.

Branch refs use `archive/<original-repository>/<original-branch>`. Tags use the same prefix under `refs/tags/`. Other source refs retain their identities under `refs/archive/`. The migration preserved **90 refs**, including additional lesson branches and historical pull-request refs. Ref SHAs were checked against GitHub after the transfer.

For example:

```sh
git clone https://github.com/samatwa/GoIT.git
cd GoIT
git switch archive/dev/final-project
```

Archive branches preserve the original code and documentation. Active documentation on `main` is English. Project code and data remain unchanged by the documentation translation.

## GitHub Pages exceptions

These 22 originals are intentionally retained as standalone repositories because GitHub Pages is enabled. Their GoIT copies remain available for browsing.

- [goit-de-hw-05](https://github.com/samatwa/goit-de-hw-05)
- [goit-js-hw-01](https://github.com/samatwa/goit-js-hw-01)
- [goit-js-hw-02](https://github.com/samatwa/goit-js-hw-02)
- [goit-js-hw-03](https://github.com/samatwa/goit-js-hw-03)
- [goit-js-hw-04](https://github.com/samatwa/goit-js-hw-04)
- [goit-js-hw-05](https://github.com/samatwa/goit-js-hw-05)
- [goit-js-hw-06](https://github.com/samatwa/goit-js-hw-06)
- [goit-js-hw-07](https://github.com/samatwa/goit-js-hw-07)
- [goit-js-hw-08](https://github.com/samatwa/goit-js-hw-08)
- [goit-markup-hw-01](https://github.com/samatwa/goit-markup-hw-01)
- [goit-markup-hw-02](https://github.com/samatwa/goit-markup-hw-02)
- [goit-markup-hw-03](https://github.com/samatwa/goit-markup-hw-03)
- [goit-markup-hw-04](https://github.com/samatwa/goit-markup-hw-04)
- [goit-markup-hw-05](https://github.com/samatwa/goit-markup-hw-05)
- [goit-markup-hw-06](https://github.com/samatwa/goit-markup-hw-06)
- [goit-neo-react-hw-module3](https://github.com/samatwa/goit-neo-react-hw-module3)
- [goit-neo-react-hw-module6](https://github.com/samatwa/goit-neo-react-hw-module6)
- [goit-neo-react-hw-module7](https://github.com/samatwa/goit-neo-react-hw-module7)
- [goit-node-rest-api](https://github.com/samatwa/goit-node-rest-api)
- [goit-pythonweb-hw-012](https://github.com/samatwa/goit-pythonweb-hw-012)
- [goit-pythonweb-hw-10](https://github.com/samatwa/goit-pythonweb-hw-10)
- [my-vite-project](https://github.com/samatwa/my-vite-project)

## Original repositories selected for removal

Each project below has a verified snapshot in the collection and a preserved Git history. Removal proceeds only after checking that Pages is still disabled and its refs have not changed. The list records the migration scope, not a claim that every deletion has already completed.

| Original repository | Collection directory | Preserved branch |
|---|---|---|
| airflow_sandbox | [DataEngineering/airflow_sandbox](DataEngineering/airflow_sandbox/) | [main](https://github.com/samatwa/GoIT/tree/archive/airflow_sandbox/main) |
| Computer-Systems-and-Their-Fundamentals | [ComputerSystems/Computer-Systems-and-Their-Fundamentals](ComputerSystems/Computer-Systems-and-Their-Fundamentals/) | [main](https://github.com/samatwa/GoIT/tree/archive/Computer-Systems-and-Their-Fundamentals/main) |
| dev | [DevOps/dev](DevOps/dev/) | [main](https://github.com/samatwa/GoIT/tree/archive/dev/main) |
| FinalProjectML | [MachineLearning/FinalProjectML](MachineLearning/FinalProjectML/) | [main](https://github.com/samatwa/GoIT/tree/archive/FinalProjectML/main) |
| FullStack-Web-Development-hw2 | [Python/WebDevelopment/FullStack-Web-Development-hw2](Python/WebDevelopment/FullStack-Web-Development-hw2/) | [main](https://github.com/samatwa/GoIT/tree/archive/FullStack-Web-Development-hw2/main) |
| goit-algo-fp | [Algorithms/goit-algo-fp](Algorithms/goit-algo-fp/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-algo-fp/main) |
| goit-algo-hw-02 | [Algorithms/goit-algo-hw-02](Algorithms/goit-algo-hw-02/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-algo-hw-02/main) |
| goit-algo-hw-03 | [Algorithms/goit-algo-hw-03](Algorithms/goit-algo-hw-03/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-algo-hw-03/main) |
| goit-algo-hw-04 | [Algorithms/goit-algo-hw-04](Algorithms/goit-algo-hw-04/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-algo-hw-04/main) |
| goit-algo-hw-05 | [Algorithms/goit-algo-hw-05](Algorithms/goit-algo-hw-05/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-algo-hw-05/main) |
| goit-algo-hw-06 | [Algorithms/goit-algo-hw-06](Algorithms/goit-algo-hw-06/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-algo-hw-06/main) |
| goit-algo-hw-07 | [Algorithms/goit-algo-hw-07](Algorithms/goit-algo-hw-07/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-algo-hw-07/main) |
| goit-algo-hw-08 | [Algorithms/goit-algo-hw-08](Algorithms/goit-algo-hw-08/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-algo-hw-08/main) |
| goit-algo-hw-09 | [Algorithms/goit-algo-hw-09](Algorithms/goit-algo-hw-09/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-algo-hw-09/main) |
| goit-algo-hw-10 | [Algorithms/goit-algo-hw-10](Algorithms/goit-algo-hw-10/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-algo-hw-10/main) |
| goit-algo2-hw-01 | [Algorithms/goit-algo2-hw-01](Algorithms/goit-algo2-hw-01/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-algo2-hw-01/main) |
| goit-algo2-hw-02 | [Algorithms/goit-algo2-hw-02](Algorithms/goit-algo2-hw-02/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-algo2-hw-02/main) |
| goit-algo2-hw-03 | [Algorithms/goit-algo2-hw-03](Algorithms/goit-algo2-hw-03/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-algo2-hw-03/main) |
| goit-algo2-hw-04 | [Algorithms/goit-algo2-hw-04](Algorithms/goit-algo2-hw-04/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-algo2-hw-04/main) |
| goit-algo2-hw-05 | [Algorithms/goit-algo2-hw-05](Algorithms/goit-algo2-hw-05/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-algo2-hw-05/main) |
| goit-algo2-hw-06 | [Algorithms/goit-algo2-hw-06](Algorithms/goit-algo2-hw-06/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-algo2-hw-06/main) |
| goit-algo2-hw-07 | [Algorithms/goit-algo2-hw-07](Algorithms/goit-algo2-hw-07/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-algo2-hw-07/main) |
| goit-algo2-hw-08 | [Algorithms/goit-algo2-hw-08](Algorithms/goit-algo2-hw-08/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-algo2-hw-08/main) |
| goit-algo2-hw-09 | [Algorithms/goit-algo2-hw-09](Algorithms/goit-algo2-hw-09/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-algo2-hw-09/main) |
| goit-algo2-hw-10 | [Algorithms/goit-algo2-hw-10](Algorithms/goit-algo2-hw-10/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-algo2-hw-10/main) |
| goit-argo | [DevOps/goit-argo](DevOps/goit-argo/) | [master](https://github.com/samatwa/GoIT/tree/archive/goit-argo/master) |
| GoIT-Core | [Python/Basics/GoIT-Core](Python/Basics/GoIT-Core/) | [main](https://github.com/samatwa/GoIT/tree/archive/GoIT-Core/main) |
| goit-cs-hw-01 | [ComputerSystems/goit-cs-hw-01](ComputerSystems/goit-cs-hw-01/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-cs-hw-01/main) |
| goit-cs-hw-02 | [ComputerSystems/goit-cs-hw-02](ComputerSystems/goit-cs-hw-02/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-cs-hw-02/main) |
| goit-cs-hw-03 | [ComputerSystems/goit-cs-hw-03](ComputerSystems/goit-cs-hw-03/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-cs-hw-03/main) |
| goit-cs-hw-04 | [ComputerSystems/goit-cs-hw-04](ComputerSystems/goit-cs-hw-04/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-cs-hw-04/main) |
| goit-cs-hw-05 | [ComputerSystems/goit-cs-hw-05](ComputerSystems/goit-cs-hw-05/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-cs-hw-05/main) |
| goit-cs-hw-06 | [ComputerSystems/goit-cs-hw-06](ComputerSystems/goit-cs-hw-06/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-cs-hw-06/main) |
| goit-de-fp | [DataEngineering/goit-de-fp](DataEngineering/goit-de-fp/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-de-fp/main) |
| goit-de-hw-03 | [DataEngineering/goit-de-hw-03](DataEngineering/goit-de-hw-03/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-de-hw-03/main) |
| goit-de-hw-04 | [DataEngineering/goit-de-hw-04](DataEngineering/goit-de-hw-04/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-de-hw-04/main) |
| goit-de-hw-06 | [DataEngineering/goit-de-hw-06](DataEngineering/goit-de-hw-06/) | [master](https://github.com/samatwa/GoIT/tree/archive/goit-de-hw-06/master) |
| goit-de-hw-07 | [DataEngineering/goit-de-hw-07](DataEngineering/goit-de-hw-07/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-de-hw-07/main) |
| goit-neo-react-extra-hw | [React/goit-neo-react-extra-hw](React/goit-neo-react-extra-hw/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-neo-react-extra-hw/main) |
| goit-neo-react-hw-module1 | [React/goit-neo-react-hw-module1](React/goit-neo-react-hw-module1/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-neo-react-hw-module1/main) |
| goit-neo-react-hw-module2 | [React/goit-neo-react-hw-module2](React/goit-neo-react-hw-module2/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-neo-react-hw-module2/main) |
| goit-neo-react-hw-module4 | [React/goit-neo-react-hw-module4](React/goit-neo-react-hw-module4/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-neo-react-hw-module4/main) |
| goit-neo-react-hw-module5 | [React/goit-neo-react-hw-module5](React/goit-neo-react-hw-module5/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-neo-react-hw-module5/main) |
| goit-node-cli | [NodeJS/goit-node-cli](NodeJS/goit-node-cli/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-node-cli/main) |
| goit-pythonweb-hw-01 | [Python/WebDevelopment/goit-pythonweb-hw-01](Python/WebDevelopment/goit-pythonweb-hw-01/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-pythonweb-hw-01/main) |
| goit-pythonweb-hw-03 | [Python/WebDevelopment/goit-pythonweb-hw-03](Python/WebDevelopment/goit-pythonweb-hw-03/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-pythonweb-hw-03/main) |
| goit-pythonweb-hw-04 | [Python/WebDevelopment/goit-pythonweb-hw-04](Python/WebDevelopment/goit-pythonweb-hw-04/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-pythonweb-hw-04/main) |
| goit-pythonweb-hw-06 | [Python/WebDevelopment/goit-pythonweb-hw-06](Python/WebDevelopment/goit-pythonweb-hw-06/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-pythonweb-hw-06/main) |
| goit-pythonweb-hw-08 | [Python/WebDevelopment/goit-pythonweb-hw-08](Python/WebDevelopment/goit-pythonweb-hw-08/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-pythonweb-hw-08/main) |
| goit-rdb-fp | [Databases/goit-rdb-fp](Databases/goit-rdb-fp/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-rdb-fp/main) |
| goit-rdb-hw-02 | [Databases/goit-rdb-hw-02](Databases/goit-rdb-hw-02/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-rdb-hw-02/main) |
| goit-rdb-hw-03 | [Databases/goit-rdb-hw-03](Databases/goit-rdb-hw-03/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-rdb-hw-03/main) |
| goit-rdb-hw-04 | [Databases/goit-rdb-hw-04](Databases/goit-rdb-hw-04/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-rdb-hw-04/main) |
| goit-rdb-hw-05 | [Databases/goit-rdb-hw-05](Databases/goit-rdb-hw-05/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-rdb-hw-05/main) |
| goit-rdb-hw-07 | [Databases/goit-rdb-hw-07](Databases/goit-rdb-hw-07/) | [main](https://github.com/samatwa/GoIT/tree/archive/goit-rdb-hw-07/main) |
| goitneo-python-hw-1-group_1 | [Python/Basics/goitneo-python-hw-1-group_1](Python/Basics/goitneo-python-hw-1-group_1/) | [main](https://github.com/samatwa/GoIT/tree/archive/goitneo-python-hw-1-group_1/main) |
| goitneo-python-hw-2-group_1 | [Python/Basics/goitneo-python-hw-2-group_1](Python/Basics/goitneo-python-hw-2-group_1/) | [main](https://github.com/samatwa/GoIT/tree/archive/goitneo-python-hw-2-group_1/main) |
| goitneo-python-hw-3-group_1 | [Python/Basics/goitneo-python-hw-3-group_1](Python/Basics/goitneo-python-hw-3-group_1/) | [main](https://github.com/samatwa/GoIT/tree/archive/goitneo-python-hw-3-group_1/main) |
| lesson-09 | [DevOps/lesson-09](DevOps/lesson-09/) | [main](https://github.com/samatwa/GoIT/tree/archive/lesson-09/main) |
| ml-ops | [MLOps/ml-ops](MLOps/ml-ops/) | [main](https://github.com/samatwa/GoIT/tree/archive/ml-ops/main) |
| my-react-project | [React/my-react-project](React/my-react-project/) | [main](https://github.com/samatwa/GoIT/tree/archive/my-react-project/main) |
| vkuznetsov-capstone-project | [DeepLearning/vkuznetsov-capstone-project](DeepLearning/vkuznetsov-capstone-project/) | [master](https://github.com/samatwa/GoIT/tree/archive/vkuznetsov-capstone-project/master) |

## Import maintenance

The original importer fetched standalone source URLs and wrote back to `main`. Those URLs may disappear after consolidation, so import automation has been replaced with read-only verification.

Run `python tools/verify_collection.py` to check preserved code/data blob hashes and English documentation. Git history refs can also be compared with `git ls-remote origin`. Future intentional code changes should update the baseline manifest as part of review.
