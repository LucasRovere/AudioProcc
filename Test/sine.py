import numpy as np
 
import wave
 
import struct
 
import matplotlib.pyplot as plt

def save_wav_channel(fn, wav, channel):
	nch   = wav.getnchannels()
	depth = wav.getsampwidth()
	wav.setpos(0)
	sdata = wav.readframes(wav.getnframes())

	typ = { 1: np.uint8, 2: np.uint16, 4: np.uint32 }.get(depth)
	print ("Extracting channel {} out of {} channels, {}-bit depth".format(channel+1, nch, depth*8))
	data = np.fromstring(sdata, dtype=typ)
	ch_data = data[channel::nch]

	# Save channel to a separate file
	outwav = wave.open(fn, 'w')
	outwav.setparams(wav.getparams())
	outwav.setnchannels(1)
	outwav.writeframes(ch_data.tostring())
	outwav.close()

#sine_wave = [np.sin(2 * np.pi * frequency * x/sampling_rate) for x in range(num_samples)]

#wav_file=wave.open(file, 'w')
 
#wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

wav_file = wave.open('test.wav', 'r')

save_wav_channel('ch1.wav', wav_file, 0)
save_wav_channel('ch2.wav', wav_file, 1)

#for s in sine_wave:
	# o struck.pack escreve os valores em hexa
#	wav_file.writeframes(struct.pack('h', int(s*amplitude)))
