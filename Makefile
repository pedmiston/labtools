.PHONY: tests demos docs

tests:
	python -m experiment_resources.tests.trials_functions_tests
	python -m experiment_resources.tests.generator_functions_tests
demos:
	runipy -o demos/trial-lists-notebook.ipynb
	ipython nbconvert --to rst --output docs/trial-lists-notebook \
	    demos/trial-lists-notebook.ipynb

	runipy -o demos/generators-notebook.ipynb
	ipython nbconvert --to rst --output ../docs/generators-notebook \
	    demos/generators-notebook.ipynb
docs:
	cd docs && $(MAKE) html
