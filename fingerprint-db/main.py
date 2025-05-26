import os
import subprocess
import sys
import ffmpeg

def main():
    
    n = len(sys.argv)
    if n!=2:
        print("Incorrect number of arguments")
        return -1
    
    mp3_path = sys.argv[1]

    split_audio(mp3_path, 0, 0, "split-mp3")
    
    return 0;

def split_audio(input_path, segment_length, overlap, output_path):
    
    if not os.path.exists("split-mp3"):
        os.makedirs("split-mp3")

    song_name = input_path.split("input-mp3/")[1]
    song_name = song_name.split(".")[0] 
    print(song_name)

    if not os.path.exists("split-mp3/" + song_name):
        os.makedirs("split-mp3/"+song_name)

    return 0;

if __name__ == '__main__':
    main()

