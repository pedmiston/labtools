#!/usr/bin/env bash

export PATH=$PATH:/Users/edmiston/Library/Enthought/Canopy_32bit/User/bin
export PATH=$PATH:/usr/local/bin

runipy -o demos/trial-lists-notebook.ipynb
ipython nbconvert --to rst --output docs/trial-lists-notebook \
    demos/trial-lists-notebook.ipynb

runipy -o demos/generators-notebook.ipynb
ipython nbconvert --to rst --output docs/generators-notebook \
    demos/generators-notebook.ipynb
