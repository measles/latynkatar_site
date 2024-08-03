pretty:
	npx prettier . --check

prettier:
	npx prettier . --write

env:
	python3 -m venv venv
	venv/bin/python3 -m pip install -r requirements.txt