rhelpackages() {
    grep -F -q -x "$1" <<EOF
jinja2
markupsafe
EOF
}
if [ -f $1 ]; then

for i in `cat $1 |awk '{print $1}' |sed '/^#/d'`
do PACKAGE=`echo $i|cut -f1 -d=|cut -f1 -d[|cut -f1 -d\<|cut -f1 -d\>` && \
VERSION=`echo "$i" |cut -f2- -d= |sed '/=/s/^.//'` && \
if [[ `find /home/awx/depends/python3/RPMS/ |grep rpm |cut -f8 -d/ |cut -f3- -d- |grep -v debuginfo |rev | cut -f2- -d.|rev |grep -i $PACKAGE-$VERSION-1 | wc -l` == 0 ]];then
  PACKAGEMOD=`echo $PACKAGE |sed 's/-/_/g'`
  #echo "!!! $PACKAGEMOD"
  if [[ `find /home/awx/depends/python3/RPMS/ |grep rpm |cut -f8 -d/ |cut -f3- -d- |grep -v debuginfo |rev | cut -f2- -d.|rev |grep -i $PACKAGEMOD-$VERSION-1 | wc -l` == 0 ]];then
   if [[ `rhelpackages "$PACKAGE" && echo 0 || echo 1` == 1 ]];then
  #echo "Package $PACKAGE-$VERSION doesn't exist"
  echo "$PACKAGE==$VERSION"
   fi
  fi
#else
  #echo "Package $PACKAGE-$VERSION already exists"
fi

done

#mv SPECS/*.tar.gz /var/lib/awx/rpmbuild/SOURCES/
#mv SPECS/*.zip /var/lib/awx/rpmbuild/SOURCES

else

echo "File $1 doesn't exist"

fi
