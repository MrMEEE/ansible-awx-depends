#!/bin/bash
cat $1 |awk '{print $1}' > $1-tuned.txt
sed -i '/^#/d' $1-tuned.txt
