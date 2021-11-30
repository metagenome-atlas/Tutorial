#!/usr/bin/env bash
set -eo pipefail


# databases can be replaced with a shared location
db_dir=$HOME/databases
working_dir=/Test_atlas

ls $db_dir

source activate adminenv

atlas --version

## Test

echo "Run atlas test"
snakemake_args=" -w $working_dir --resources mem=10 java_mem=10  -j 2"


atlas init -w $working_dir --db-dir $db_dir $HOME/test_reads

head $working_dir/samples.tsv


echo "run atlas this installs software via conda"

atlas run binning  $snakemake_args $snakemake_args $@




echo "finished test"
