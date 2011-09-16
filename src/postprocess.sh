#!/bin/bash

FRAMES=../data/frames

#rename frames to allow for missing ones where convert err'd
x=1;
for i in $(ls $FRAMES/*jpg);
do
counter=$(printf %06d $x);
mv $i $FRAMES/$counter.jpg;
x=$(($x+1));
done;
