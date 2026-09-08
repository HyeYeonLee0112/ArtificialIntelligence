.PHONY: setup test check
PYTHON ?= python3
setup:
	$(PYTHON) -m pip install -r requirements.txt
test:
	$(PYTHON) -m pytest -q
check:
	$(PYTHON) scripts/check_environment.py
