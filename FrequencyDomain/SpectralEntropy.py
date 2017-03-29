# Vancley Simão
# vancleys@gmail.com


# Spectral Entropy

import pyeeg
import math

def SpectralEntropy( x ):

	fs = 128
	band = [1,4,8,12,30]
	b = pyeeg.bin_power(x,band,fs)
	resp = pyeeg.spectral_entropy(x,band,fs,Power_Ratio=b)

	resp = [0 if math.isnan(x) else x for x in resp]

	return resp
