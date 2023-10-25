#!/bin/bash
export SOUNDCLOUD_RSS=https://feeds.soundcloud.com/users/soundcloud:users:76950/sounds.rss
export DOWNLOAD_DIR=/home/bonce/Music/n-type/
source venv/bin/activate
python src/main.py
