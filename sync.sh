#!/bin/bash
SRC=~/Documents/git/copymanga
DST=root@192.168.40.62:/home/git/
trap 'exit' INT
while :
    do
        echo '----------------------------------------------------------------'
        fswatch -r -L -1 ${SRC}
        date
        rsync -av --exclude={".*","__pycache__/*"} ${SRC} ${DST}
        say 同步完成
    done