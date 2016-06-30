#!/bin/sh

PROJECT_PATH=/home/pi/python-stuff/auto-podcast-update
SOURCE_PATH=$PROJECT_PATH/audio/*
DEST_PATH=/media/mp3player/MUSIC/podcasts

echo ' ' >>$PROJECT_PATH/log.txt 2>&1
echo 'mount_mp3.sh executed ' >>$PROJECT_PATH/log.txt 2>&1
date >>$PROJECT_PATH/log.txt 2>&1

mount /dev/sd*1 /media/mp3player >>$PROJECT_PATH/log.txt 2>&1
cp -f  $SOURCE_PATH $DEST_PATH >>$PROJECT_PATH/log.txt 2>&1
rm $SOURCE_PATH >>$PROJECT_PATH/log.txt 2>&1
