[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)

This repo contains code sample related to this tutorial:  [Poetry : A Better Alternative to requirements.txt. The Maven for Python ?](https://rovingdev.com/p/poetry-a-better-alternative-to-requirementstxt)

## Info
This is example for usage of poetry for a python project.

### Install Poetry
```bash
pip install pipx
pipx install poetry
```

`poetry config virtualenvs.in-project true` to make .venv directory inside project, this will make your IDE to detect venv

### build this code
```bash
git clone git@github.com:sukumaar/parquet_to_json_example.git
cd parquet_to_json_example
poetry config virtualenvs.in-project true
poetry install
poetry build
# packages will be created under dist/
```
## test, change path-to-project to correct path
```bash
cd ~
mkdir test
cd test
pip uninstall parquet2json -y && pip install --no-cache-dir path-to-project/dist/parquet2json-0.1.0-py3-none-any.whl
```

### Using as standalone cli app:

```bash
#install
pip uninstall parquet2json -y && pip install --no-cache-dir path-to-project/dist/parquet2json-0.1.0-py3-none-any.whl

## use like below
parquet2json -h # for help
parquet2json --i "path/to/parquet" --o "path/for/json"
```

### Create project with Poetry if you dont want to git clone
```
poetry new project-name
cd project-name
poetry install # installs dependency
poetry update # if adding/removing dependency via toml file
```

### venv with all dependencies from pyproject.toml
```poetry shell```

### Build dsitributable wheel and tar
```poetry build```

