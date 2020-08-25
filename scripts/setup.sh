#!/usr/bin/env bash

set -e

if ! command -v conda &> /dev/null
then
  echo "I need conda package manager to be isntalled http://anaconda.org/"
fi


#install mamba if it doesnt' exist

if ! command -v mamba &> /dev/null
then
  conda install -y mamba -c conda-forge
fi



mamba env create -n analyze -f condaenv.yml
