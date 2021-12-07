#!/usr/bin/env bash

Tag="metagenomeatlas/atlas_tutorial:v3"

docker build . -t atlas_tutorial

echo "Docker image build!"

# docker run -t atlas_tutorial /test_atlas.sh --resources mem=3 java_mem=2 --omit-from download_checkm_data


docker tag atlas_tutorial:latest $Tag



docker push $Tag
