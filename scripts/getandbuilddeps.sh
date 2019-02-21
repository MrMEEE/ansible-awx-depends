#!/bin/bash

for i in `./comparereqtorpms.sh $1`;do

echo "Couldn't find package: $i, downloading and building..."

PACKAGE=`echo $i |cut -f1 -d=`
VERSION=`echo $i |cut -f3 -d=`

if [[ -n `find ../BUILT/ -maxdepth 1 -iname $PACKAGE-scl.spec` ]];then

	echo "Earlier version of package has already been built"
	echo
else
	echo "Could not find existing spec file for $PACKAGE"
	echo
fi

done
