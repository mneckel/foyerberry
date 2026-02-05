#!/bin/bash 
pkill -9 feh
/usr/bin/python /root/5mcd.pyw
/usr/bin/feh -Y -F --zoom fill -. -D 7 /mnt/samba/AudioVisual/PreSlides/ -R 300
