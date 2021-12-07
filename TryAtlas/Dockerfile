FROM jupyter/base-notebook


################## METADATA ######################
LABEL base.image="jupyter/base-notebook"
LABEL version="$version"
LABEL software="metagenome-atlas"
LABEL software.version="2"
LABEL about.summary="Test metagenome-atlas"
LABEL about.home="https://github.com/metagenome-atlas/Tutorial"
LABEL license="BSD-3"
LABEL about.tags="metagenomics, annotation, snakemake, assembly, genomic-binning, functional-annotation, taxonomic-classifications"

################## MAINTAINER ######################
MAINTAINER Silas Kieser

# Switch back to root for some install

USER root
RUN export LC_ALL=en_US.UTF-8
RUN export LANG=en_US.UTF-8



# setup miniconda
RUN conda config --add channels bioconda
RUN conda config --add channels conda-forge

# get basic bash tools
RUN sudo apt-get -y update
RUN sudo apt-get install -y less nano wget grep


USER $NB_UID
# doesn't work
RUN conda init

ENV databaseDir="$HOME/databases"

RUN mkdir $databaseDir


# get example data
RUN wget --quiet https://zenodo.org/record/3992790/files/test_reads.tar.gz && tar -xzf test_reads.tar.gz && rm -f test_reads.tar.gz

RUN echo "> contig_1\nAAAAAAAAAAATTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT" > $databaseDir/human_genome.fasta




# download atlas
ENV version="2.8.1"

### install atlas


# install metagenome-atlas in its own environemnt
RUN mamba create -yn adminenv metagenome-atlas=$version

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "adminenv", "/bin/bash", "-c"]

RUN atlas --help

# modify atlas code to decrease memory of checkm
ADD patch.py /
RUN python /patch.py

#################

ENV TEST_WORKING_DIR="$HOME/.test/"
# dryrun

# run atlas this installs software via conda
RUN atlas init -w $TEST_WORKING_DIR --db-dir $databaseDir test_reads


RUN atlas run all -w $TEST_WORKING_DIR --dryrun
RUN atlas run  -w $TEST_WORKING_DIR  qc  --conda-create-envs-only
RUN atlas run  -w $TEST_WORKING_DIR  assembly  --conda-create-envs-only
RUN atlas run  -w $TEST_WORKING_DIR  binning  --conda-create-envs-only

##


## add script and make it executable by everyone
USER root
ADD test_atlas.sh /
RUN chmod +x /test_atlas.sh
RUN chmod +x /patch.py
# remove empty folder
RUN rmdir $HOME/work

#remove one env to show instalation
RUN rm -r "$(grep plotly databases/conda_envs/*.yaml | cut -f1 -d'.')"*

ENV DEMO=" --resources mem=3 java_mem=2 --omit-from download_checkm_data -j 2 "
