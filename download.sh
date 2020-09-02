#/bin/bash
start=0
end=1000
count=1000
if [ $# -eq 2 ];then
    start=$1
    end=$2
    count=`expr ${end} - ${start}`
fi
mkdir -p download
script_path=script
scripts=`ls ${script_path}|head -n ${end}|tail -n ${count}`
cd download
for file in $scripts:
do
    cmd="sh ../${script_path}/${file}"
    echo $cmd
    $cmd
done
