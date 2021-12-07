#!/usr/bin/env bash
set -eo pipefail
atlas_version=2.8

# databases can be replaced with a shared location
db_dir=$HOME/databases
working_dir=$HOME/Test_atlas

ls $db_dir

#source activate adminenv
mamba create -yn testenv metagenome-atlas=$atlas_version

source activate testenv

atlas --version

/patch.py

## Test

echo "Run atlas test"
snakemake_args=" -w $working_dir $DEMO"


atlas init -w $working_dir --db-dir $db_dir $HOME/test_reads

head $working_dir/samples.tsv


echo "run atlas this installs software via conda"


atlas run binning  $snakemake_args $snakemake_args $@


mamba env remove -yn testenv

echo "finished test"
