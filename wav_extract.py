import struct
import os

file = '../data/music.wav'
wav = open(file, 'rb')

class Wav:
    def __init__(self):
        self.data = data
        self.wav = wav
        self.file = file

    def getChunkId(self):
        ChunkId = data[0:4]
        return ChunkId

    def read(self):
        data = wav.read()
        return data

    def getSize(self):
        size = os.path.getsize(file)
        return size

    def getChunkSize(self):
        ChunkSize = data[4] * data[5] * data[6] * data[7]
        return ChunkSize

    def getFormat(self):
        fmt = data[8:12]
        return fmt

    def getChunk(self):
        Chunk_ = data[12:16]
        return Chunk_

    def getCSize(self):
        ChunkSize_ = data[16:20]
        return ChunkSize_

    def getAudioFmt(self):
        AudioFmt = data[20:22]
        return AudioFmt

    def getNumChannels(self):
        NumChannels = data[22:24]
        return NumChannels

data = Wav.read(wav)
chunkid = Wav.getChunkId(data)
size = Wav.getSize(file)
chunksize = Wav.getChunkSize(data)
format = Wav.getFormat(data)
chunk = Wav.getChunk(data)
chusize = Wav.getCSize(data)
audiofmt = Wav.getAudioFmt(data)
numchannels = Wav.getNumChannels(data)

print(chunkid)
print(size)
print(chunksize)
print(format)
print(chunk)
print(chusize)
print(audiofmt)
print(numchannels)