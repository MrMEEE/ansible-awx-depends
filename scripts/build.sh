#!/bin/sh
 
# Make sure rpmbuild is installed!!
 
BASEDIR=$(pwd)
REQUIREMENTS=requirements
 
mkdir -p requirements-source
mkdir -p requirements-rpms
rm -rf requirements-source/*
rm -rf requirements-rpms/*
 
for i in ${REQUIREMENTS}/*.tar.gz; do tar xzf $i -C requirements-source; done
for i in ${REQUIREMENTS}/*.tar.bz2; do tar xjf $i -C requirements-source; done
for i in ${REQUIREMENTS}/*.zip; do unzip $i -d requirements-source; done
 
for package in requirements-source/*; do cd ${BASEDIR}/${package} && scl enable rh-python36 "python3 setup.py bdist_rpm --spec-only  --packager=\"Martin Juhl <m@rtinjuhl.dk>\" --release 1"; done
 
cd ${BASEDIR}
find requirements-source/ -type f -name *.rpm ! -name *.src.rpm | xargs -i cp {} requirements-rpms/
 
echo "Number of source files:" $(ls -1 ${REQUIREMENTS} | wc -l)
echo "Number of rpm files:" $(ls -1 requirements-rpms | wc -l)
