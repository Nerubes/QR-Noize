#!/bin/bash

rm -r build
cmake -S. -Bbuild

cd build 

make

cd ..

#g - Служит для передачи пути до конфига генерации (generate_config)
#d - Слудит для передачи пути для вывода данных (dest)
#с - Служит для передачи пути к кофигу для зашумления (noize_config)
#
#После этого по пути dest будут созданы файлы изображений, сгенерированные, а потом зашумленные в соответствии с generate_config и noize_config соответственно

#while getopts g:d:c: flag
#do 
#  case "${flag}" in
#    g) generate_config=${OPTARG};;
#    d) dest=${OPTARG};;
#    c) noize_config=${OPTARG};;
#
pip install -r requirements.txt
#
#./build/imgen $generate_config $dest $noize_config 
