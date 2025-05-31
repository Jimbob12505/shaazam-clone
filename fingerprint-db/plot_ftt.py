import matplotlib.pyplot as plt
import numpy as np

def plot_fft_magnitude(fft_result, sample_rate, output_path, chunk_index=0):
    N = len(fft_result)
    freq = np.fft.fftfreq(N, d=1/sample_rate)
    
    # Only take the positive half (real signal symmetry)
    half_N = N // 2
    freq = freq[:half_N]
    magnitude = np.abs(fft_result[:half_N])

    plt.figure(figsize=(10, 4))
    plt.plot(freq, magnitude)
    plt.title(f"FFT Magnitude Spectrum - Chunk {chunk_index}")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid(True)
    plt.tight_layout()
    
    plt.savefig(f"{output_path}/fft_chunk_{chunk_index}.png") 
    plt.close()
