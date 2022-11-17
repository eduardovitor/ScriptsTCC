#!/bin/bash

filename=$1
i=1
while read line; do
    echo $line > "cidade_$i"
    ((i++))
done < $filename
