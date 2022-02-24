"""
This file contains essential functions required for Renormalization Group
trajectory initialization and tracking.

It can be used for Classical Heisenberg Model on Hierarchical Lattice with Hamiltonian
including only nearest neighbour interactions and performs (in theory) exact scaling.

Both pure and random bond calculations are executed on other scripts.
"""

import numpy as np
from scipy.special import spherical_jn
import numba

#Clebsch Gordan coefficients tracked up to (l1,l2,l)==(50,50,50)
clebsch_gordan = np.load('cleb.npy')

#Creates Legendre Fourier coefficients with given J to
#express our exponantiated hamiltonian in series form.
def lfc_initialize(J, l_prec):
	x = np.arange(l_prec)
	x = np.real((2*x+1)*(1j**(x))*spherical_jn(x,-1j*J))
	y = np.amax(np.abs(x))
	return x/y

#Bond Move Process of Renormalization Group
#Takes 2 LFC groups and returns "bond-moved" LFC group
@numba.jit
def bond_move(lfc1, lfc2, l_prec):
	lfc_bond_moved = np.zeros(l_prec)
	for l in range(l_prec):
		val = 0
		for l1 in range(l_prec):
			for l2 in range(l_prec):
				x = lfc1[l1]*lfc2[l2]*clebsch_gordan[l1,l2,l]
				val += x
		lfc_bond_moved[l] += val
	return lfc_bond_moved

#Decimation Process of Renormalization Group
#Takes 2 LFC groups and returns decimated LFC group
@numba.jit
def decimate(lfc1, lfc2):
	l_prec = len(lfc1)
	lfc_decimated = np.arange(l_prec, dtype=np.float64)
	lfc_decimated = (lfc1*lfc2)/(2*lfc_decimated+1)
	x = np.amax(np.abs(lfc_decimated))
	return lfc_decimated/x
