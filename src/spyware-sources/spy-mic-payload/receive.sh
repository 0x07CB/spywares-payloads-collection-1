#!/bin/bash
while true; do     
netcat -lnvp 8080 -w 30 > last_record.wav.gz && gzip -d last_record.wav.gz && rm -f last_record.wav.gz
done