


[Binder_Rstudio]: https://rstudio.cloud/project/2975573

<!-- https://mybinder.org/v2/gh/metagenome-atlas/BinderTutorial/R?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fmetagenome-atlas%252FTutorial%26urlpath%3Drstudio%252F%26branch%3Dmaster -->

[Binder_Jupyter]: https://mybinder.org/v2/gh/metagenome-atlas/BinderTutorial/Python?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fmetagenome-atlas%252FTutorial%26urlpath%3Dlab%252Ftree%252FTutorial%252F%26branch%3Dmaster
[chat]: https://github.com/metagenome-atlas/Tutorial/issues


# Metagenome-Atlas Tutorial

This is a tutorial for Metagenome-Atlas. [Metagenome-Atlas](https://metagenome-atlas.github.io/) is an easy-to-use pipeline for analyzing metagenomic data. It handles all steps from QC, Assembly, Binning, to Annotation.

:interrobang: If you have any question or errors [write us][chat].


![checkmquality](Tutorial/images/quality.svg)


## Setup

This steps you can do at the beginning of the tutorial.

### 1. GitHub codespaces


For the tutorial we will use GitHub codespaces as a server.
If you have access to the cluster of your institution, with the conda-package manager installed might want to try to do the tutorial there.


1.  You need a GitHub username.
2.  Go to [github.com/codespaces](https://github.com/codespaces) and log in
3.  Create a new codespaces

   ![Create a new codespaces](Tutorial/images/go_to_codespaces_1.png)

  - Type `metagenome-atlas/Tryitout` as the name for the repo and select it
  - Use 4 processor machine
  - Create the instance

You have 15 GB storage and 120 core-hours free. (If you are already using codespaces intensely, we might look for another solution.)

This opens a visual studio code environment.

Make sure that the `terminal` is selected in the bottom plane. 

➤ Make it bigger. 


➤ Run `./setup_codespaces.sh` in the terminal

This script installs mamba and sets some conda channels.
If you do it on your cluster have a look at the [documentation](https://metagenome-atlas.readthedocs.io/en/latest/usage/getting_started.html)


### 2. Open the Rstudio server

0. Create a free Rstudio cloud account [here](https://posit.cloud/plans/free).
1. Open this [Rstudio online](https://posit.cloud/content/6178419) environment in a new tab.
2. Click on Git then Pull Branches at the center top of the screen.


![Pull Branches](Tutorial/images/rstudio_git_pull.png)




## Analyze the output of Atlas

Usually before starting to install a program I want to make sure that it gives the output I want.
Therefore, we start analyzing the output of Metagenome-atlas.

We prepared an interactive Rmarkdown with the code for differential analysis. 

:sparkles: Follow this link to the [interactive tutorial](https://metagenome-atlas.shinyapps.io/Part2).


Here is an other Tutorial based on human samples with [only the reports](https://metagenome-atlas.shinyapps.io/Output_human)

<!--


![Picture of obese mice](https://upload.wikimedia.org/wikipedia/commons/0/0b/Fatmouse.jpg)


Click on the links below:

[Rstudio][Binder_Rstudio]          [Jupyter][Binder_Jupyter]

If something doesn't work, [let us know][chat].

### Run the code on your computer
If you want to run this code on your machine. 
Download this repo either as zip or with `git clone`. In the directories `Python` and `R` are dedicated scripts to install the necessary packages to run the code. 

-->

## Install and run atlas with three commands

In this part of the tutorial you will install metagenome-atlas either in GitHub codespaces or on your server and test it with a small dataset.
As real metagenomic assembly can take more than 250GB ram and multiple processors, you would ideally do this directly on a high-performance system, e.g. the cluster of your university. You can install [minconda](https://docs.conda.io/en/latest/miniconda.html) in your home directory if it is not installed on your system.

[Follow this link](https://metagenome-atlas.shinyapps.io/TryAtlas)


See also the [get started](https://metagenome-atlas.readthedocs.io/en/latest/usage/getting_started.html#install-metagenome-atlas) section in the documentation.



<!--
[This cool report](http://htmlpreview.github.io/?https://github.com/metagenome-atlas/Tutorial/blob/master/Example/Results/Summary.html):sparkles: shows the most interesting output of Atlas.


Metagenome-Atlas produces a lot of other outputs from the QC and assembly steps. They are  summarized reports such as these ones:
- [QC_report](https://metagenome-atlas.readthedocs.io/en/latest/_static/QC_report.html)
- [assembly report](https://metagenome-atlas.readthedocs.io/en/latest/_static/assembly_report.html).
-->

