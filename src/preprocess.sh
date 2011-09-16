#!/bin/bash

RAWIMGS=../data/rawimgs
CLEANIMGS=../data/cleanimgs
MAX_COUNT=100000

mkdir -p $CLEANIMGS

#cleaning images
#copy them to the clean dir
cp $RAWIMGS/*.png $CLEANIMGS
find  $RAWIMGS/ -name "*.png" -exec cp "{}" $CLEANIMGS \;

#remove the ones that didn't save correctly
find  $CLEANIMGS/ -name "*.png" -exec mogrify -format jpg "{}"\;
mogrify -format jpg $CLEANIMGS/*.png
rm $CLEANIMGS/*.png

#rename the remaining ones
x=1;
y=1;
while [ $x -lt $MAX_COUNT ];
do 
if [ -f $CLEANIMGS/$x-clipped.jpg ];
then
counter=$(printf %06d $y);
mv $CLEANIMGS/$x-clipped.jpg $CLEANIMGS/$counter.jpg;
y=$(($y+1));
fi;
x=$(($x+1));
done;
