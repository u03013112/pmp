#/bin/bash
mkdir -p download
script_path=script
scripts=`ls ${script_path}`
cd download
for file in $scripts:
do
    cmd="sh ../${script_path}/${file}"
    echo $cmd
    $cmd
done
