#!/bin/bash
for i in {1..28}
do
   printf "Fetching image $i\n"
   curl -O -L "http://fullterrain.com/images/ss/egpb/$i.jpg"
   printf "\n\n"
done
