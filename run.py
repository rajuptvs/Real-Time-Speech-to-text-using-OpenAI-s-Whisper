import pyaudio
from pydub import AudioSegment

import ffmpeg
import sys
import os
import whisper

from helperfunctions import whisper_gpt
nfile="normaltranscipt.txt"
realtimefile="realtimetranscript.txt"
def realtime():
    audiofile="audio.mp3"

    chunk_size = 16384
    whispers = whisper_gpt("base",audiofile)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True,output=True, frames_per_buffer=chunk_size)
    audio = AudioSegment.empty()

    try:
        while True:
            chunk = stream.read(chunk_size)
            audio += AudioSegment(data=chunk, sample_width=2, frame_rate=44100, channels=1)
            audio.export('audio.mp3', format='mp3')
            
            transcript=whispers.transcribe()
    
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
        print("Transcription completed.\nPlease find the transcription below.\n",transcript)
        whispers.save_transcript(transcript,realtimefile)
        print("\n Transcription has also been written to %s file"%realtimefile)


def normal_transcription(file):
    whispers = whisper_gpt("small",file)
    transcript=whispers.ntranscribe()
    whispers.save_transcript(transcript,nfile)
    print("Transcription completed.\nPlease find the transcription below.\n",transcript)
    print("\n Transcription has also been written to %s file"%nfile)
     
if __name__ == "__main__":
    try:
        user=int(input("Do you want a real time transciption or from a saved audio file. (1/2) \n"))
        if user == 1:
            realtime()
        elif user ==2:
            file=str(input("Enter the file path. \n"))
            normal_transcription(file)
        else:
            print("invalid option")
    except KeyboardInterrupt:
        print("Terminated")