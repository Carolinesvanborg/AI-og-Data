"""Recording Audio"""

# Pyaudio
import pyaudio
import wave

chunk = 1024 # record in chunks of 1024 samples
sample_format =pyaudio.paInt16 # 16 bits per sample
channels = 2
fs = 44100 # Rocord at 44100 samples per secons
seconds = 3
filename = "output.wav"

p = pyaudio.PyAudio() # Create in interface to PortAudio

print("Recording")

stream =p.open(format =sample_format,
               channels=channels,
               rate=fs,
               frames_per_buffer=chunk,
               input=True)

frames = [] # initialize array to store frames

# Store data in shunks for 3 seconds
for i in range(0,int(fs / chunk * seconds)):
    data =stream.read(chunk)
    frames.append(data)

# Stop and close the stream
stream.stop_stream()
stream.close()
#Terminate the PortAudio interface
p.terminate()

print("finished recording")

# Save the recorded data as a wav file
wf = wave.open(filename,'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()