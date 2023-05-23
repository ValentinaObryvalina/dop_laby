import wave
import struct
import os


dir_name = os.path.dirname(__file__)
path_to_file1 = os.path.join(dir_name, 'sample-15s.wav')
path_to_file2 = os.path.join(dir_name, 'new_sample.wav')

source = wave.open(path_to_file1, mode='rb')
dest = wave.open(path_to_file2, mode='wb')
dest.setparams(source.getparams())

frames_count = source.getnframes()
data = source.readframes(frames_count)

data = struct.unpack("<" + str(frames_count * 2) + "h", data)
new_data = list(data)

del new_data[::5]

new_frames = struct.pack("<" + str(len(new_data)) + "h", *new_data)
dest.writeframes(new_frames)

source.close()
dest.close()



