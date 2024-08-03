pretty:
	npx prettier . --check

prettier:
	npx prettier . --write

black:
	python3 -m black --check main.py lib

black_diff:
	python3 -m black --diff main.py lib

blacked:
	python3 -m black main.py lib

env:
	python3 -m venv venv
	venv/bin/python3 -m pip install -r requirements.txt

install_pretty:
	npm install --save-dev --seve-extract 'prettier@3.3.3'
