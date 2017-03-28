# Vancley Simão
# vancleys@gmail.com


# Power Feature

import numpy as np

def Power( x ):

	F = np.fft(x)
	P = F * np.conjugate(F)
	resp = sum(P)

	return resp
