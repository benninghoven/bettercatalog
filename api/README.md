How to Install and Run Flask
======

##Installation
Create a python virtual environment and activate:

```bash
python3 -m venv [VENV NAME]
source [/dir/to/venv]/activate
```

**Note**: [VENV NAME] can be any venv name of your choice

Use the package manager [`pip`](https://pip.pypa.io/en/stable/) to install dependencies:

```bash
pip install -r requirements.txt
```

##Running Flask
1. Change into api directory
```bash
cd api
```
2. Run the following command to set `FLASK_APP` environment variable
```bash
# For linux:
export FLASK_APP=main.py
# For Mac:
set FLASK_APP=main.py
```
3. Run flask
```bash
flask run --port=5000
```