.PHONY: tests demos docs

tests:
	python -m labtools.tests.trials_functions_tests
	python -m labtools.tests.generator_functions_tests
demos:
	runipy -o demos/simple-trial-generation.ipynb
	ipython nbconvert --to rst --output demos/simple-trial-generation \
	    demos/simple-trial-generation.ipynb
	cp demos/simple-trial-generation.rst docs/demos/generating-trial-lists/simple-trial-generation.rst

	runipy -o demos/using-generators.ipynb
	ipython nbconvert --to rst --output demos/using-generators \
	    demos/using-generators.ipynb
docs:
	cd docs && $(MAKE) html

docs-push:
	cd ../labtools/docs/html
	git add .
	git commit -m "Updates to docs"
	git push origin gh-pages
