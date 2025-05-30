import os
import subprocess
import sys
import ffmpeg
from pydub import AudioSegment
import numpy as np
from hamming import hamming_window

def split_audio(input_path, segment_length, overlap):
    
    if not os.path.exists("split-mp3"):
        os.makedirs("split-mp3")

    song_name = input_path.split("input-mp3/")[1]
    song_name = song_name.split(".")[0] 
    print(song_name)

    output_path = "split-mp3/" + song_name

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    probe = ffmpeg.probe(input_path)
    duration = float(probe['format']['duration'])

    step = segment_length - overlap
    start = 0
    count = 0

    while start < duration:
        out_file = os.path.join(output_path, f'chunk_{count:03d}.mp3')
        ffmpeg.input(input_path, ss=start, t=segment_length).output(out_file, acodec='copy').run(overwrite_output=True)
        start += step
        count += 1

    print(f'Done. {count} overlapping segments created.')
    
    return output_path;


