# Vancley Simão
# vancleys@gmail.com


# Discret Wavelet Transform

import pywt

def DWT( x ):

	resp = pywt.dwt(x, 'db4')

	return resp
