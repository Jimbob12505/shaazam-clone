import os
import subprocess
import sys
import ffmpeg
from pydub import AudioSegment
import numpy as np 


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


