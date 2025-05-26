import os
import subprocess
import sys
import ffmpeg

def main():
    
    n = len(sys.argv)
    if(n!=2):
        print("Incorrect number of arguments")
        return -1
    
    mp3_path = argv[1]

    split_audio(input_path, segment_length, overlap, output_path)
    
    return 0;

def split_audio(input_path, segment_length, overlap, output_path):
    return 0;

if __name__ == '__main__':
    main()

