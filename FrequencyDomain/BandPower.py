# Vancley Simão
# vancleys@gmail.com


# Band Power for each frequency range

import pyeeg

def BandPower( x ):

	fs = 128
	band = [1,4,8,12,30]

	resp = pyeeg.bin_power(x,band,fs)

	return resp
