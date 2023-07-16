


[Binder_Rstudio]: https://rstudio.cloud/project/2975573

<!-- https://mybinder.org/v2/gh/metagenome-atlas/BinderTutorial/R?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fmetagenome-atlas%252FTutorial%26urlpath%3Drstudio%252F%26branch%3Dmaster -->

[Binder_Jupyter]: https://mybinder.org/v2/gh/metagenome-atlas/BinderTutorial/Python?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fmetagenome-atlas%252FTutorial%26urlpath%3Dlab%252Ftree%252FTutorial%252F%26branch%3Dmaster
[chat]: https://github.com/metagenome-atlas/Tutorial/issues


# Metagenome-Atlas Tutorial

This is a tutorial for Metagenome-Atlas. [Metagenome-Atlas](https://metagenome-atlas.github.io/) is an easy-to-use pipeline for analyzing metagenomic data. It handles all steps from QC, Assembly, Binning, to Annotation.

:interrobang: If you have any question or errors [write us][chat].


![checkmquality](Tutorial/images/quality.svg)


## Setup

Got to the [setup page](Setup.md) and follow the instructions.


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

