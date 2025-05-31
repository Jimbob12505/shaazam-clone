import os
import re
import subprocess
import sys
import ffmpeg
from pydub import AudioSegment
import numpy as np

from hamming import hamming_window
from split_audio import split_audio
from scipy.fft import fft
from plot_ftt import plot_fft_magnitude

def main():
    
    n = len(sys.argv)
    if n!=2:
        print("Incorrect number of arguments")
        return -1
    
    mp3_path = sys.argv[1]

    output_path = split_audio(mp3_path, 10, 0)
    print(f"Output Path: {output_path}")

    smoothed_chunks = apply_hamming_function(output_path)
    print(smoothed_chunks)

    all_fft_results = apply_fft(smoothed_chunks)

    for i, fft_chunk in enumerate(all_fft_results):
        plot_fft_magnitude(fft_chunk, 44100, output_path, chunk_index=i)

    return 0;

def apply_fft(file_array):
    
    fft_results = []
    

    print(f"file_array: {file_array}")

    for file in file_array:
        #result = [] 
        print(f"file: {file}")

        chunk = AudioSegment.from_file(file, format="mp3")
        samples = np.array(chunk.get_array_of_samples())

        # Normalizing the chunk
        max_val = np.iinfo(samples.dtype).max
        samples = samples.astype(np.float32) / max_val
        
        # Perform FFT
        spectrum = np.abs(fft(samples))[:len(samples)//2]
        #result.append(spectrum)
        fft_results.append(spectrum)
    
    return fft_results;

def apply_hamming_function(path):

    files = all_files_in_directory("chunk_", path)
    print(files)    
    smoothed_chunks = []

    for file in files: 
        path_to_file = path + '/' + str(file)
        chunk = AudioSegment.from_file(path_to_file, format="mp3")
        smoothed_chunk = hamming_window(chunk)

        output = f"{path}/smoothed_{str(file)}"
        smoothed_chunks.append(output)
        smoothed_chunk.export(path + '/' + "smoothed_" + str(file), format="mp3")

    return smoothed_chunks

def all_files_in_directory(substring, directory):

    try:
        files = [
            file for file in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, file)) and file.startswith(substring)
        ]
        return files
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
        return []



if __name__ == '__main__':
    main()

