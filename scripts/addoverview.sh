#!/bin/bash

for file in *.tif
    do gdaladdo -r average $file 2 4 8 16 32 64
done
