
VIRTUALENV_PATH=venv
PYTHON=python3.5
PIP=pip
LINT=flake8
SRCS=src


all: test

clean:
	rm -rf $(VIRTUALENV_PATH)

$(VIRTUALENV_PATH):
	virtualenv -p $(PYTHON) $@
	$@/bin/$(PIP) install -r requirements.txt

test:
	$(LINT) $(SRCS)
