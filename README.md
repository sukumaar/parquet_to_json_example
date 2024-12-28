## Info
This is example for usage of poetry for a python project.

### Install Poetry
```bash
pip install pipx
pipx install poetry
```

`poetry config virtualenvs.in-project true` to make .venv directory inside project, this will make your IDE to detect venv

### Create project
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

### Using as standalone cli app:

```bash
pip uninstall parquet2json -y && pip install --no-cache-dir path-to-project/dist/parquet2json-0.1.0-py3-none-any.whl

## use like below
parquet2json --i "~/project/data/titanic.parquet" --o "~/project/data/444.json"
```