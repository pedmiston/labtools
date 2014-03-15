#!/usr/bin/env bash

PATH="/Users/edmiston/Library/Enthought/Canopy_32bit/User/bin:${PATH}"
export PATH

echo "trials_functions_tests..."
python -m resources.tests.trials_functions_tests
echo "generator_functions_tests..."
python -m resources.tests.generator_functions_tests
