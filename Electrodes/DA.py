# Vancley Simão
# vancleys@gmail.com


# Differential Asymmetry

import numpy as np
import nolds
import pyeeg

def DA( x,y ):

	mean = np.subtract(np.mean(x), np.mean(y))
	std = np.subtract(np.std(x), np.std(y))
	# dfa = nolds.dfa(x) - nolds.dfa(y)

	fs = 128
	band = [1,4,8,12,30]

	power = np.subtract(pyeeg.bin_power(x,band,fs), pyeeg.bin_power(y,band,fs))

	return mean,std,power
