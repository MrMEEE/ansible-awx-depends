#!/bin/bash

for i in `ls /home/awx/depends/python3/SRPMS/`;do echo "Send $i" && /home/awx/depends/python3/send-build $i /home/awx/depends/python3/SRPMS/$i;done
