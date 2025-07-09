## Dog Identifier

![Python](https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54&style=for-the-badge) ![Code Style](https://img.shields.io/badge/code%20style-pep8-orange) [![Linting and Unit Tests](https://github.com/Nomia-Limited/DataLake/actions/workflows/ci.yml/badge.svg)](https://github.com/Nomia-Limited/DataLake/actions/workflows/ci.yml)


| Folder | Description |
|--------|-------------|
|.github/workflows|CI pipeline|
|archive|Unused files may be useful in the future|
|config|Configuration settings such as connection strings and file paths|
|data|Sample datasets that can be used for development and testing purposes|
|docs|Project documentation in markdown format|
|examples|Examples of how to use the code in this repo|
|images|Images in PNG format|
|notebooks|Jupyter notebooks associated with the lake|
|src|All project source code|
|tests|All tests, note this is in the same directory structure as "src"|
|utils|Provides helper functions and utilities that support the main scripts|

## Project Setup

uv is mandated for this project

Install uv
````shell
curl -LsSf https://astral.sh/uv/install.sh | sh
````

Create and activate the virtual enviroment
````shell
uv venv .venv
source .venv/bin/activate
````

Install dependencies
````shell
uv pip install
````

Verify that the dependencies are correctly installed:
````shell
uv pip list
````

Set your environment
````shell
export PYTHONPATH=`pwd`
export ACCOUNTNAME='stguksnglakest' # Azure lake storage account name
export ACCOUNTKEY='...' # Azure lake storage account key
````

Run Your Python Scripts
````shell
uv run src/ingest/ingest.py mydatafile.csv
````

