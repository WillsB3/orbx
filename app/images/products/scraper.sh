#!/bin/bash
for i in {45..47}
do
   printf "Fetching image $i\n"
   curl -O -L "http://fullterrain.com/images/ss/nanca/$i.jpg"
   printf "\n\n"
done
