# Vancley Simão
# vancleys@gmail.com


# Hjorth Features

import numpy as np

def Hjorth( x ):

	complexity = np.sqrt(np.mean(pow(np.diff(np.diff(x)),2)))
	mobility = np.sqrt(np.mean(pow(diff(x),2))/np.mean(pow(x,2)))

	return complexity,mobility
