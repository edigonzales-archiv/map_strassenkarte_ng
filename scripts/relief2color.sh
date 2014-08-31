#!/bin/bash

for file in *.tif
    do gdaldem color-relief -co COMPRESS=LZW $file ramp.txt hellgrau-$file
done


