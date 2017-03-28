# Vancley Simão
# vancleys@gmail.com


# Spectral Entropy

import pyeeg

def SpectralEntropy( x ):

	b = pyeeg.bin_power(x)
	resp = pyeeg.spectral_entropy(x,Power_Ratio=b)

	return resp
