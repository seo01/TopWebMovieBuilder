#!/bin/bash

FRAMES=../data/frames
SOUND=../popcorn.mp3
MOVIE=../data/movies/movie.mov
MOVIE_DIR=../data/movies/

mkdir -p $MOVIE_DIR
rm $MOVIE
#without sound
#ffmpeg -f image2 -i $FRAMES/%06d.jpg $MOVIE
#with sound
ffmpeg -f image2 -i $FRAMES/%06d.jpg -i $SOUND $MOVIE
