![](https://img.shields.io/badge/code%20style-black-000000.svg)

# Development

## Pre requirement
- Python 3.10+
- Any operating system

## Install dev requirements
```shell
pip install -r requirements-dev.txt
```

## Install pre-commit
- add hooks
  ```shell
  pre-commit install
  pre-commit install --hook-type commit-msg
  ```
- update to the latest versions
  ```shell
  pre-commit autoupdate
  ```

## Run locally

```shell
streamlit run deploy_days.py
```

## Formatting and Linting
```shell
pre-commit run --all-files
```

## Run test
```shell
pytest --cov=deploy_calender --cov-report html
```
