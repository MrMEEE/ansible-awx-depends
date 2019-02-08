cp ../ronny/requirements-source/*/dist/*.spec .

scl enable rh-python36 bash
for i in `ls`;do spec2scl $i > ${i::-5}-scl.spec && rm -f $i;done
exit

sed -i '1s/^/%define scl rh-python36\n/' *

for i in `ls`;do sed -i "s/%{pkg_name}/${i::-9}/g" $i;done
