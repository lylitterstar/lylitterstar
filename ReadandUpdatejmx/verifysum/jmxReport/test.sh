#!/bin/bash
dir=`pwd`
for line in `cat ../configData/lable.txt`
do
line1=`echo ${line}|sed -e 's/\//_/g'`
echo ${line1} 
#touch ${line}.txt
grep ${line} ${dir}/verify_home_page.jmx_50_2017-05-23-20-52-08.jtl|awk -F ',' '{print $2  $3}'|sort -t ' ' -k1 -n -o ${line1}.txt  
done
