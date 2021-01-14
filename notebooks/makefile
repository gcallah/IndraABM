# Need to export as ENV var
export TEMPLATE_DIR = templates

PYLINT = flake8
PYLINTFLAGS = --ignore=E501
PYTHONFILES = $(shell ls *.py)
MODELS_DIR = ../models
MODELFILES = $(shell ls $(MODELS_DIR)/*.py)
NBFILES = $(shell ls $(MODELS_DIR)/*.py | sed -e 's/.py/.ipynb/' | sed 's/\.\.\/models\///')

FORCE:

lint: $(patsubst %.py,%.pylint,$(PYTHONFILES))

%.pylint:
	$(PYLINT) $(PYLINTFLAGS) $*.py

notebooks: $(NBFILES)

%.ipynb: $(MODELS_DIR)/%.py
	python3 create_model_nb.py $< > $@
	git add $@
