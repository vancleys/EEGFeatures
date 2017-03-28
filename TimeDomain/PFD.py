# Vancley Simão
# vancleys@gmail.com


# Petrosian Fractal Dimension

import pyeeg

def PFD( x ):

	d =  pyeeg.first_order_diff(x)
	resp = pyeeg.pfd(x, D=d)

	return resp
