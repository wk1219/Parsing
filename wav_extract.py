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
        chunksize = data[4] * data[5] * data[6] * data[7]
        return chunksize

    def getFormat(self):
        fmt = data[8:12]
        return fmt

    # def PrintInfo(self):
    #     print(self.getChunkId())
    #     print(self.getChunkSize())
    #     print(self.getFormat())

data = Wav.read(wav)
chunkid = Wav.getChunkId(data)
size = Wav.getSize(file)
chunksize = Wav.getChunkSize(data)
format = Wav.getFormat(data)

print(chunkid)
print(size)
print(chunksize)
print(format)
