# Metagenome-Atlas Tutorial for ECCB


This is a tutorial for [Metagenome-Atlas](https://metagenome-atlas.github.io/) used at ECCB. Metagenome-atlas is a easy-to-use pipeline for analyzing metagenomic data. It handles all steps from QC, Assembly, Binning, to Annotation.




# Tutorial part 1: Analyze the output of Atlas

Usually before starting to install a program I want to make sure that it gives the output I want.
Therefore we start analyzing the output of Metagenome-Atlas.
In part 2 of the Tutorial you learn how to run metagenome atlas on some test data or on your own.


## Example output of Metagenome Atlas
A real Metagenome-Atlas run can take more than a day. Therefore we have you prepared some output of a previous run.


<!-- TODO: Describe output -->

This [summary file](http://htmlpreview.github.io/?https://github.com/metagenome-atlas/Tutorial/blob/master/Example/Results/Summary.html) describes the most interesting output of Atlas.

More detailed description can be found [here](https://metagenome-atlas.readthedocs.io/en/latest/usage/output.html).

## Setup

### Requirements

The tutorial works on linux and macOS and maybe on Windows. In general you don't need a lot of computation capacity. You would need to install the [conda package manager](https://metagenome-atlas.readthedocs.io/en/latest/usage/getting_started.html#setup) if you don't have it already.


### Download scripts

Download the scripts for analyzing the output.

Download this repo with git or download it as [zip archive](https://github.com/metagenome-atlas/atlas_analyze/archive/master.zip) and extract it.

```
git clone https://github.com/metagenome-atlas/atlas_analyze.git
cd atlas_analyze
```

The script use various python package for analyzing and ploting. Set them up by running

```
./setup.sh
```

This creates an conda-environment in order not to interfere with other software on your computer. Activate the environment by running:

```
conda activate analyze
```

## Analyze output

Let's start the jupyter notebook to analyze the atlas output. Open the `Analyis_genome_abundances.ipynb`

```

cd scripts
jupyter lab
```
