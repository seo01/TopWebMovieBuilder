#!/bin/bash
FROM=1
TO=4000
ALEXA_FILE=../data/alexa/top-1m.csv
WEBKIT2PNG=../python paulhammond-webkit2png-9c4265a/webkit2png
WIDTH=800
HEIGHT=600
RAWIMGS=../data/rawimgs

mkdir -p $RAWIMGS

cat $ALEXA_FILE | while read f; 
do
page=`echo $f | cut -d, -f2`; 
rank=`echo $f | cut -d, -f1`; 
if [ $rank -ge $FROM -a $rank -lt $TO ];
then echo $page;
./timeout3 -t 30 $WEBKIT2PNG -s 1 --clipwidth=$WIDTH --clipheight=$HEIGHT -C -o $rank -D $RAWIMGS http://$page;
fi;
if [ $rank -ge $TO ];
then break;
fi;
done;
