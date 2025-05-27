import os
import subprocess
import sys
import ffmpeg
from pydub import AudioSegment
import numpy as np

def main():
    
    n = len(sys.argv)
    if n!=2:
        print("Incorrect number of arguments")
        return -1
    
    mp3_path = sys.argv[1]

    split_audio(mp3_path, 10, 0)
    
    chunk = AudioSegment.from_file("split-mp3/Doechii-Anxiety/chunk_000.mp3", format="mp3")
    smoothed_chunk = hamming_window(chunk)
    smoothed_chunk.export("smoothed_chunk_000.wav", format="wav")

    return 0;

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
    
    return 0;

def hamming_window(chunk: AudioSegment) -> AudioSegment:

    samples = np.array(chunk.get_array_of_samples())

    # Reshape audio if stereo
    if chunk.channels == 2:
        samples = samples.reshape((-1, 2))

    # Apply hamming window function
    window = np.hamming(len(samples))
    
    if chunk.channels == 2:
        samples = (samples * window[:, None]).astype(np.int16)
    else:
        samples = (samples * window).astype(np.int16)

    # Convert back to AudioSegment
    processed_chunk = chunk._spawn(samples.tobytes())
    return processed_chunk

if __name__ == '__main__':
    main()

