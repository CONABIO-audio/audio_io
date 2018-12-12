
import os
import hashlib
import wave
import librosa
import librosa.display
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

def read_info(path):
    wav = wave.open(path)
    
    return wav.getframerate(), wav.getnchannels(), wav.getsampwidth(), wav.getnframes()
    
def read(path,sr,offset=0.0,duration=None):
    return librosa.load(path,sr=sr,offset=offset,duration=duration)

def write(path,sig,sr,nchannels,aformat="wav"):
    if nchannels > 1:
        sig = np.transpose(sig,(1,0))
    sf.write(path,sig,sr,format=aformat)

def binaryMD5(path):
    if path is not None:
        if os.path.isfile(path):
            BLOCKSIZE = 65536
            hasher = hashlib.md5()
            with open(path,"rb") as media:
                buf = media.read(BLOCKSIZE)
                while len(buf) > 0:
                    hasher.update(buf)
                    buf = media.read(BLOCKSIZE)
            return hasher.hexdigest()
        else:
            return None
    else:
        return None

def media_size(path):
    if path is not None:
        if os.path.isfile(path):
            return os.path.getsize(path)
        else:
            return None
    else:
        return None

def stft(sig,n_fft,hop_length):
    return librosa.stft(sig,n_fft,hop_length)

def spectrogram(sig,n_fft,hop_length):
    return np.abs(stft(sig,n_fft,hop_length))

def plot_power_spec(spec,ax):
    return librosa.display.specshow(librosa.amplitude_to_db(spec,ref=np.max),ax=ax,y_axis='linear',x_axis='time')
