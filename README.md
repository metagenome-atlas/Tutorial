# Metagenome-Atlas Tutorial for ECCB


This is a tutorial for Metagenome-Atlas at ECCB. [Metagenome-Atlas](https://metagenome-atlas.github.io/) is a easy-to-use pipeline for analyzing metagenomic data. It handles all steps from QC, Assembly, Binning, to Annotation.


If you have any question or errors write an Github issue or try to contact us via the conference platfrom chat.


## Tutorial part 1: Analyze the output of Atlas

Usually before starting to install a program I want to make sure that it gives the output I want.
Therefore we start analyzing the output of Metagenome-Atlas.
In part 2 of the Tutorial you learn how to run metagenome atlas on some test data or on your own.

### Requirements

The tutorial works on linux and macOS and maybe on Windows. In general you don't need a lot of computation capacity. You would need to install the [conda package manager](https://metagenome-atlas.readthedocs.io/en/latest/usage/getting_started.html#setup) if you don't have it already.


### Example output of Metagenome Atlas
A real Metagenome-Atlas run can take more than a day. Therefore we have you prepared some output of a previous run. Open the Example output <a href="Example" target="_blank">"Example"</a>._

The folder `Results` contains the most interesting output of Atlas which is summarised in this [report] (http://htmlpreview.github.io/?https://github.com/metagenome-atlas/Tutorial/blob/master/Example/Results/Summary.html). The output is based on 15 samples from mice fecal samples from the project PRJEB7759. 8 of them were fed a high fat diet and got obese. Can you see the difference between the groups in the PCA?

The main goal of atlas is to create metgenome assembled genomes (MAGs). The genomes are in the folder `genomes/genomes`. How many are there?

The Taxonomy is based on the Genome Taxonomy Database (GTDB) which tries to be consistent with genome distances. The taxonomy can be found in `Results/taxonomy.tsv`. Which is the phylum with the most genomes? How many species are new/unnamed?

MAGs are usually not complete or can contain some contamination. Atlas estimates the quality of genomes using checkM. Which is the species with the highest completeness and lowest quality? (You can zoom in in the plot in the summary file).

Quantification is based on mapping the reads to the genomes using bbmap. The counts of the raw reads can be used to calculate the mapping rate and for statistics based on compositional data analysis (CODA). See this [Article](https://www.frontiersin.org/articles/10.3389/fmicb.2017.02224/) why CODA statistics is a good idea for microbiome analysis.

Do you think the mapping rate is good? If reads from the host (Mouse) would have been filtered out do you think the mapping rate would be higher?

Analysis based on relative abundance can better be performed with the coverage information than with the raw counts.  We use the median coverage over the genomes to calculate the relative abundance. What is the most abundant species in these metagenomes?

Functional annotation is based on the output of EggNOG mapper of all the genes. Using the link  between the genes and the genomes we can calculate which function is present in which genome (`genomes/gene2genome.tsv.gz`). And finally the relative abundance of functions (`Results/annotations`).


 The atlas pipeline produces a lot of other outputs along the line from the QC and assembly steps, summarised in the reports: [QC_report](https://metagenome-atlas.readthedocs.io/en/latest/_static/QC_report.html) [assembly report](https://metagenome-atlas.readthedocs.io/en/latest/_static/assembly_report.html).


### Run script for differential abundance analysis

#### Setup

To analyze the data we will use a jupyter notebook. If something doesn't work, let me know. You can always have a look at the [notebook](scripts/Differencial abundance based on genomes.ipynb) to see what would be the output.

To run the notebook yourself we need some scripts in the `scripts` subdirectory. Download this repo with git or download it as [zip archive](https://github.com/metagenome-atlas/Tutorial/archive/master.zip) and extract it.

```
git clone https://github.com/metagenome-atlas/Tutorial.git
cd Tutorial
```

The script use various python package for analyzing and ploting. Set them up by running

```
cd scripts
./setup.sh
```

This creates an conda-environment in order not to interfere with other software on your computer.
Activate the environment by running:

```
conda activate analyze
```

then start jupyter:

```
jupyter lab
```

# Tutorial part 2: Install and run metagenome Atlas

In the second part of the tutorial you will install metagenome-atlas on your system and test it with a small dataset.
As real metagenomic assembly can take more than 250GB ram and multiple processors, you would ideally do this directly on a high performance system, e.g. the cluster of your university. You can install [minconda](https://docs.conda.io/en/latest/miniconda.html) in your home directory if it is not installed on your system.

[Follow this link](https://metagenome-atlas.readthedocs.io/en/latest/usage/getting_started.html#install-metagenome-atlas)

If you want only do the test dataset, you can do most steps on a  normal labtop (Mac or Linux).
