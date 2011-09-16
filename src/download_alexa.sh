#!/bin/bash
OUTPUT_FILE=../data/alexa/top-1m.csv.zip
ALEXA_URL=http://s3.amazonaws.com/alexa-static/top-1m.csv.zip

mkdir -p $ALEXA_FILE

wget -O $OUTPUT_FILE $ALEXA_URL
unzip $OUTPUT_FILE