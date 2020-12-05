


[Binder_Rstudio]: http://mybinder.org/v2/gh/metagenome-atlas/Tutorial/master?urlpath=rstudio
[Binder_Jupyter]: http://mybinder.org/v2/gh/metagenome-atlas/Tutorial/master?urlpath=lab
[chat]: https://github.com/metagenome-atlas/Tutorial/issues


# Metagenome-Atlas Tutorial

This is a tutorial for Metagenome-Atlas. [Metagenome-Atlas](https://metagenome-atlas.github.io/) is an easy-to-use pipeline for analyzing metagenomic data. It handles all steps from QC, Assembly, Binning, to Annotation.


:interrobang: If you have any question or errors [write us][chat].


:notes: Do you need some music to work. Have a look at this [spotify playlist](https://open.spotify.com/playlist/1uJJpcPx752ddZXCtU6oRc?si=sTO-ec95TFqxHviin59M0g) for bioinformaticians.

![checkmquality](Tutorial/images/quality.svg)


## Analyze the output of Atlas

Usually before starting to install a program I want to make sure that it gives the output I want.
Therefore, we start analyzing the output of Metagenome-atlas.

:sparkles: Follow this link to the [interactive tutorial](https://metagenome-atlas.shinyapps.io/Part2).

<!--
[This cool report](http://htmlpreview.github.io/?https://github.com/metagenome-atlas/Tutorial/blob/master/Example/Results/Summary.html):sparkles: shows the most interesting output of Atlas.


Metagenome-Atlas produces a lot of other outputs from the QC and assembly steps. They are  summarized reports such as these ones:
- [QC_report](https://metagenome-atlas.readthedocs.io/en/latest/_static/QC_report.html)
- [assembly report](https://metagenome-atlas.readthedocs.io/en/latest/_static/assembly_report.html).
-->


## Install and run atlas with three commands

In this part of the tutorial you will install metagenome-atlas on your system and test it with a small dataset.
As real metagenomic assembly can take more than 250GB ram and multiple processors, you would ideally do this directly on a high-performance system, e.g. the cluster of your university. You can install [minconda](https://docs.conda.io/en/latest/miniconda.html) in your home directory if it is not installed on your system.

[Follow this link](https://metagenome-atlas.shinyapps.io/Part1/)

If you want only do the test dataset, you can do most steps on a  normal laptop (Mac or Linux).
See also the [get started](https://metagenome-atlas.readthedocs.io/en/latest/usage/getting_started.html#install-metagenome-atlas) section in the documentation.




<!--

### Run script for differential abundance analysis

We prepared an interactive jupyter notebook with the code for differential analysis. The goal is to find out which changes are associated with High fat diet induced obesity in mice. To analyze the data, we will install some python packages.  

![Picture of obese mice](https://upload.wikimedia.org/wikipedia/commons/0/0b/Fatmouse.jpg)

Click on the links below:

[Rstudio][Binder_Rstudio]          [Jupyter][Binder_Jupyter]

If something doesn't work, [let us know][chat].

-->
