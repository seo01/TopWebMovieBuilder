#!/bin/bash

#cleaning
echo "Cleaning"
./clean.sh
echo "Downloading from Alexa"
./download_alexa.sh
echo "Crawl Pages"
./crawl_pages.sh
echo "Pre Process images"
./preprocess.sh
echo "Building Frames script"
mkdir -p ../data/scripts
./generate_frames.py > ../data/scripts/gen_frames.sh
source ../data/scripts/gen_frames.sh
echo "Post Process Frames"
./postprocess.sh
echo "Build Movie"
./build_movie.sh
