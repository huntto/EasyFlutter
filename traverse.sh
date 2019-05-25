#! /bin/bash

prefix=""

function traverse_dir() {
    for file in `ls $1`
    do
        if [ -d $1"/"$file ]
        then
            traverse_dir $1"/"$file
        else
            echo $prefix$1"/"$file
        fi
    done
}

function usage() {
    echo -e "Usage:\n\t\btraverse [-p prefix] [--prefix prefix] directory"
}

while [ $# -ge 2 ] ; do
        case "$1" in
                -p) prefix=$2; shift 2;;
                --prefix) prefix=$2; shift 2;;
                *) usage ; exit 1 ; break;;
        esac
done

traverse_dir $1