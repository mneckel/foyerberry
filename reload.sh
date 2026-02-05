#!/bin/bash
pkill -9 feh
export DISPLAY=:0; /usr/bin/feh -Y -F --zoom fill -. -D 7 /mnt/samba/AudioVisual/PreSlides/ -R 300
