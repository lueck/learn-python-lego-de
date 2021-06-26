# Installation #

Install `virtualenv`, then `cd` into the project root and create a
virtual environment:

	python3 -m pip install --user virtualenv
	cd learn-python-lego-de
	python3 -m venv env

Then activate the virtual environment:

	source env/bin/activate

This should change your prompt. Call `deactivate`, if you want to
leave the virtual environment. When the virtual environment is active,
assert that `env/bin` is on the `PATH` and overrides your system-wide
installation:

	which python # should return env/bin/python
	which pip # should return env/bin/pip

Install required packages and `learn-python-lego-de` into the virtual
environment:

	python -m pip install -r requirements.txt
	python setup.py bdist_wheel

	pip install .
