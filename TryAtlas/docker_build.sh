#!/usr/bin/env bash

Tag=".metagenomeatlas/atlas_tutorial:v1"

docker build . -t atlas_tutorial

docker tag atlas_tutorial:latest $Tag

docker push $Tag
