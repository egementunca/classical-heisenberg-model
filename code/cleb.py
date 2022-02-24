import numpy as np
from sympy.physics.wigner import clebsch_gordan

cleb = np.zeros(50**3).reshape(50,50,50).astype(np.float64)
for l1 in range(50):
	for l2 in range(50):
		for l in range(50):
			val = (clebsch_gordan(l1,l2,l,0,0,0).n(20))**2
			cleb[l1,l2,l] = val

np.save('cleb.npy',cleb)
print('done...')