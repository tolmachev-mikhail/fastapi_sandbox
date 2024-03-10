# FASTAPI Sandbox Project

This repo stores sandbox application build on base of fastapi tutorial.
Project will provide API for diagnostic laboratory

# Dependencies

For dependencies installation run:

* Create new Virtual Environment

```bash
python3 -m venv ~/.venvs/<YOUR_ENV_NAME>
```

* Activate the environment

```bash
source ~/.venvs/<YOUR_ENV_NAME>
```

```bash
pip install -r requirements.txt
```

# Run

```bash
uvicorn main:laboratory_app --reload
```
