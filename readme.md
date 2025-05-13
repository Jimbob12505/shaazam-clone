# How does Shazam Work
- The basic gist of how Shazam works is by creating a unique digital footprint for every song
- The song (mp3) is converted into a spectogram
    - This spectogram depicts the frequency content of the audio over time
    - Essentially, it shows which frequencies are present at each moment in time, and how intense they are
- From the spectogram, Shazam pinpoints frequencies with high intensity
    - These are the beats/notes that stand out in the song
- These frequencies, known as Peaks, are the songs unique features that make it recognisable 
- Shazam encodes the relationship between these Peaks into unique hashes and links them to the songs metadata (title, artist, etc), and the exact time each Peak occured in the spectogram
- Thousands of these hashes come together to form the songs fingerprint
- The fingerprint is stored in a database, where each hash serves as a quick reference point for searches
- When you use Shazam, it records a short snippet of the audio. It then runs this exact digital footprint algorithm
- Rather than it being saved into a database, they are used to query the database for matches
- The results are then grouped by song id, i.e, if the query resulted in hashes 0231, 1231, 4921, 0923 and 8731, where 0231, 1231, 4921 were all part of song A and 0923 and 8731 were part of song B, the results would be split into 2 songs A and B, each containing their hashes
- Although it might seem logical to assume to song with the most results (matches) is the correct one, however, this is not always the case
- Shazam analyses the time coherence of the candidates, evaluating how well snippets timestamps align with those of each candidates
- The song with the highest time coherence is chosen as the correct match

# TODO
## Function 1 - Spectogram Conversion
- [] Take raw mp3 and convert into spectogram
    - [] Split audio into overlapping segments
    - [] Apply Hamming Window function to taper of signal jumps at each split cut of audio to create smooth transition
    - [] Apply Fast Fourier Transform to each audio segment
 
