import QuenchedRandomness as qr
import numpy as np



def check(p):

	j_disorder = 1/8
	j_order = 10
	j_new = (j_disorder+j_order)/2

	f = qr.rgTrajectory(j_new, p, 9, 3, 25, 21, 25)

	if f[-1][0][0] == 1:
		j_dis = j_new
		print('{} is disordered'.format(j_new))
		data.append([j_new, 'disordered'])
	else:
		j_order = j_new
		print('{} is ordered'.format(j_new))
		data.append([j_new, 'ordered'])
	for i in range(39):
		j_new = (j_order + j_dis)/2
		f = qr.rgTrajectory(j_new, p, 9, 3, 25, 21, 25)
		if f[-1][0][0] == 1:
			j_dis = j_new
			print('{} is disordered'.format(j_new))
			data.append([j_new, 'disordered'])
		else:
			j_order = j_new
			print('{} is ordered'.format(j_new))
			data.append([j_new, 'ordered'])

	return data

def phase_diagram():

	file = open('phasediagram.txt','w')
	crit_J = []

	for p in np.linspace(0.05,.5,100):
		crit_val = check(p)[-1][0]
		crit_J.append(crit_val)
		file.write('p:{} critical j is {} \n'.format(p,crit_val))
	file.close()
	return crit_J
