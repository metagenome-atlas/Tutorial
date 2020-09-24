
## Setup of the Tutorial on you own computer
#### Setup of Jupyter notebook 

The part of the tutorial works on linux and macOS and maybe on Windows.  You need to install the [conda package manager](https://metagenome-atlas.readthedocs.io/en/latest/usage/getting_started.html#setup). Download this repo with git or download it as [zip archive](https://github.com/metagenome-atlas/Tutorial/archive/master.zip) and extract it.

```
git clone https://github.com/metagenome-atlas/Tutorial.git
cd Tutorial
```

The script use various python package for analyzing and plotting. Set them up by running

```
cd scripts
./setup.sh
```

This creates a conda-environment in order not to interfere with other software on your computer.
Activate the environment by running, then start jupyter:

```
conda activate analyze
jupyter lab
```


Click on the `Differential_abundance.ipynb` and start the differential analysis.
