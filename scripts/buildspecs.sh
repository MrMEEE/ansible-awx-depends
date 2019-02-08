#!/bin/bash

ln -s /opt/rh/rh-python36/root/usr/bin/python3 /usr/bin/python3.6

yum -y install centos-release-scl

yum clean all

yum -y install python3-rpm-macros python-rpm-macros rh-python36-build rh-python36-python rh-python36-python-devel gcc make libffi-devel openssl-devel libxml2-devel libxslt-devel gcc-c++ rh-postgresql10-postgresql-devel openldap-devel xmlsec1-devel libxml2-devel xmlsec1-openssl-devel libtool-ltdl-devel rh-python36-python-sphinx rh-python36-python-six

yum -y install https://cbs.centos.org/kojifiles/packages/scl-utils-build-helpers/0/7.el7/noarch/scl-utils-build-helpers-0-7.el7.noarch.rpm

ln -s /opt/rh/rh-python36/root/usr/bin/sphinx-build /opt/rh/rh-python36/root/usr/bin/sphinx-build-3

ln -s /opt/rh/rh-postgresql10/root/usr/bin/pg_config /usr/bin/pg_config

yum -y install /root/rpmbuild/RPMS/noarch/* /root/rpmbuild/RPMS/x86_64/*

ln -s /usr/include/libxml2/libxml /usr/include/libxml

export LC_CTYPE=en_US.UTF-8

PACKAGESBUILT=1
while [[ $PACKAGESBUILT > 0  ]];do

rm -f /source/buildlog.log

PACKAGESBUILT=0

for i in `ls /source/SPECS/`;do 
	echo "!!!!!!!!!!!!!! BUILDING $i !!!!!!!!!!!!!!" >> /source/buildlog.log
        rpmbuild -ba /source/SPECS/$i >> /source/buildlog.log 2>&1
	if [[ $? == 0 ]];then
		echo "$i was built successfully!!" 
		mv /source/SPECS/$i /source/ansible-awx-depends/BUILT/
		((PACKAGESBUILT++))
	else

		echo "$i failed to build"
	fi
done

if [[ $PACKAGESBUILT > 0 ]];then
echo "Number of packages built: $PACKAGESBUILT, installing and trying more"
yum -y install /root/rpmbuild/RPMS/noarch/* /root/rpmbuild/RPMS/x86_64/*
fi

done

echo "No packages was built during last run, stopping"
