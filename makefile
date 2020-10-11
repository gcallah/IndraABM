# Need to export as ENV var
export TEMPLATE_DIR = templates

# Set up some variables for directories we'll use:
BOX_DIR = bigbox
BOX_DATA = $(BOX_DIR)/data
BOXPLOTS = $(shell ls $(BOX_DATA)/plot*.pdf)
DOCKER_DIR = docker
REQ_DIR = $(DOCKER_DIR)
REPO = indras_net
MODELS_DIR = models
NB_DIR = notebooks
WEB_STATIC = static
API_DIR = APIServer
PYLINT = flake8
PYLINTFLAGS =
PYTHONFILES = $(shell ls $(MODELS_DIR)/*.py)

UTILS_DIR = utils
PTML_DIR = html_src
INCS = $(TEMPLATE_DIR)/head.txt $(TEMPLATE_DIR)/logo.txt $(TEMPLATE_DIR)/menu.txt

HTMLFILES = $(shell ls $(PTML_DIR)/*.ptml | sed -e 's/.ptml/.html/' | sed -e 's/html_src\///')

MODEL_REGISTRY = registry/models
MODELJSON_FILES = $(shell ls $(MODELS_DIR)/*.py | sed -e 's/.py/_model.json/' | sed -e 's/$(MODELS_DIR)\//registry\/models\//')
JSON_DESTINATION = $(MODEL_REGISTRY)/models.json

FORCE:

notebooks: $(PYTHONFILES)
	cd $(NB_DIR); make notebooks

local: $(HTMLFILES) $(INCS)

%.html: $(PTML_DIR)/%.ptml $(INCS)
	python3 $(UTILS_DIR)/html_checker.py $<
	$(UTILS_DIR)/html_include.awk <$< >$@
	git add $@

$(MODEL_REGISTRY)/%_model.json: $(MODELS_DIR)/%.py
	python3 json_generator.py $< >$@

models.json: $(MODELJSON_FILES)
	python3 json_combiner.py $? --models_fp $(JSON_DESTINATION)

create_dev_env: FORCE
	./setup.sh .bashrc  # change to .bash_profile for Mac!
	git submodule init $(UTILS_DIR)
	git submodule update $(UTILS_DIR)

setup_react: FORCE
	cd $(REACT_TOP); npm install

# build tags file for vim:
tags: FORCE
	ctags --recurse .
	git add tags

submods:
	cd utils; git pull origin master

# run tests then commit all, then push
# add notebooks back in as target once debugged!
prod: local pytests github

# run tests then push just what is already committed:
prod1: tests
	git push origin master

tests: pytests 

python: pytests github

pytests: FORCE
	cd registry; make tests
	cd epidemics; make tests
	cd models; make tests
	cd APIServer; make tests
	cd indra; make tests
	cd capital; make tests

dockertests:
	docker build -t gcallah/$(REPO) docker/

github:
	- git commit -a
	git push origin master

lint: $(patsubst %.py,%.pylint,$(PYTHONFILES))

%.pylint:
	$(PYLINT) $(PYLINTFLAGS) $*.py

# dev container has dev tools
dev_container: $(DOCKER_DIR)/Dockerfile $(DOCKER_DIR)/requirements.txt $(DOCKER_DIR)/requirements-dev.txt
	docker build -t gcallah/$(REPO)-dev docker

# prod container has only what's needed to run
prod_container: $(DOCKER_DIR)/Deployable $(DOCKER_DIR)/requirements.txt
	docker system prune -f
	docker build -t gcallah/$(REPO) docker --no-cache --build-arg repo=$(REPO) -f $(DOCKER_DIR)/Deployable

# deploy prod containerr
deploy_container: prod_container
	docker push gcallah/$(REPO):latest


nocrud:
	-rm *~
	-rm *.log
	-rm *.out
	-rm .*swp
	-rm *.csv
	-rm models/.coverage
