# Metagenome-Atlas Tutorial for ECCB


This is a tutorial for [Metagenome-Atlas](https://metagenome-atlas.github.io/) used at ECCB. Metagenome-atlas is a easy-to-use pipeline for analyzing metagenomic data. It handles all steps from QC, Assembly, Binning, to Annotation.




# Tutorial part 1: Analyze the output of Atlas

Usually before starting to install a program I want to make sure that it gives the output I want.
Therefore we start analyzing the output of Metagenome-Atlas.
In part 2 of the Tutorial you learn how to run metagenome atlas on some test data or on your own.

## Requirements

The tutorial works on linux and macOS and maybe on Windows. In general you don't need a lot of computation capacity. You would need to install the [conda package manager](https://metagenome-atlas.readthedocs.io/en/latest/usage/getting_started.html#setup) if you don't have it already.


## Example output of Metagenome Atlas
A real Metagenome-Atlas run can take more than a day. Therefore we have you prepared some output of a previous run.
It contains 15 samples from mice fecal samples. 8 of them were fed a high fat diet and got obese. The goal of the Tutorial is too see which changes in the microbes and the functions were induced by the diet.


Download the data from here.

This [summary file](http://htmlpreview.github.io/?https://github.com/metagenome-atlas/Tutorial/blob/master/Example/Results/Summary.html) describes the most interesting output of Atlas.
More detailed description can be found [here](https://metagenome-atlas.readthedocs.io/en/latest/usage/output.html).

## Download scripts for analyzing

To analyze the data we will use a jupyter notebook. For this we need some scripts.

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

# Tutorial part 2: Install and run metagenome Atlas

In the second part of the tutorial you will install metagenome-atlas on your system and test it with a small dataset.
As real metagenomic assembly can take more than 250GB ram and multiple processors, you would ideally do this directly on a high performance system, e.g. the cluster of your university. You can install [minconda](https://docs.conda.io/en/latest/miniconda.html) in your home directory if it is not installed on your system.

[Follow this link](https://metagenome-atlas.readthedocs.io/en/latest/usage/getting_started.html#install-metagenome-atlas)

If you want only do the test dataset, you can do most steps on a  normal labtop (Mac or Linux).
