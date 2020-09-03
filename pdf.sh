#/bin/bash
mkdir -p pdf
download_path=download
files=`ls ${download_path}`
cd pdf
for file in $files:
do
    mkdir -p ${file}
    cs=`ls ../${download_path}/${file}`
    for c in $cs:
    do
        cmd="python3 ../im2pdf.py ../${download_path}/${file}/${c} ${file}/${c}.pdf"
        echo $cmd
        $cmd
    done
done
