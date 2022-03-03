import QuenchedRandomness as qr
import numpy as np

def check(p=0.5, n=3):

	data = []

	j_disorder = 1
	j_order = 10
	j_new = (j_disorder+j_order)/2

	f = qr.rgTrajectory(j_new, p, n, 3, 1000, 21, 25)

	if abs(f[-1][0][0]) == 1:
		j_disorder = j_new
		print('{} is disordered'.format(j_new))
		data.append([j_new, 'disordered'])
	else:
		j_order = j_new
		print('{} is ordered'.format(j_new))
		data.append([j_new, 'ordered'])
	for i in range(39):
		j_new = (j_order + j_disorder)/2
		f = qr.rgTrajectory(j_new, p, n, 3, 1000, 21, 25)
		if abs(f[-1][0][0]) == 1:
			j_disorder = j_new
			print('{} is disordered'.format(j_new))
			data.append([j_new, 'disordered'])
		else:
			j_order = j_new
			print('{} is ordered'.format(j_new))
			data.append([j_new, 'ordered'])

	return data

def phase_diagram():

	file = open('partialdim.txt','w')
	crit_J = []

	for n in np.arange(4,28):
		crit_val = check(p=0.5, n=n)[-1][0]
		crit_J.append(crit_val)
		file.write('n:{} critical j is {} \n'.format(n,crit_val))
	file.close()
	return crit_J

phase_diagram()
