#!/bin/bash

for file in *.tif
    do gdaldem color-relief -co COMPRESS=LZW $file ramp.txt ramp-$file
    do gdaladdo -r average ramp-$file 2 4 8 16 32 64
done
