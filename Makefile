.PHONY: tests* demos* docs*

tests-trials:
	python -m labtools.tests.trials_functions_tests

tests-generators:
	python -m labtools.tests.generator_functions_tests

tests: tests-trials tests-generators

demos-simple-generation:
	cd demos && \
	runipy -o simple-trial-generation.ipynb && \
	ipython nbconvert --to rst simple-trial-generation.ipynb && \
	cp simple-trial-generation.rst ../docs/demos/generating-trial-lists/simple-trial-generation.rst

demos-using-generators:
	cd demos && \
	runipy -o using-generators.ipynb && \
	ipython nbconvert --to rst using-generators.ipynb && \
	cp using-generators.rst ../docs/demos/generating-trial-lists/using-generators.rst

demos: demos-simple-generation demos-using-generators
	
docs-build:
	cd docs && $(MAKE) html

docs-push:
	cd ../labtools-docs/html && \
	git add --all && \
	git commit -m "Updates to docs" && \
	git push origin gh-pages

docs: docs-build docs-push
