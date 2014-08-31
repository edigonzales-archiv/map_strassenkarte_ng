#!/bin/bash

for file in *.tif
    do gdaldem hillshade -co COMPRESS=LZW -compute_edges -az 270 -alt 40 $file relief-$file
done
