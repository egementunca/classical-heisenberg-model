import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 20
plt.rcParams['axes.linewidth'] = 1.5

x = (np.log(np.arange(4,28,dtype=np.float64))/np.log(3))+1
y=1/np.array([7.237445944115279,5.9169815691066106,5.095249179467828,4.410946437345956,3.7375871385529535,3.584521087160283,3.4105628570459885,3.268921625692201,3.144026659420888,2.599609240881364,2.5081135922000612,2.5971803979891774,2.6781896793099804,2.6601499169655654,2.4237682415323434,2.247482999989188,2.358569443250417,2.163390261940549,1.9166632537535406,1.0000000000081855,1.8592848349444466,1.9818600547196183,1.7558940430835719,1.7989023905292925],dtype=np.float64)
fig, axs = plt.subplots(1,1)

axs.tick_params(axis='x',which='major',size=8,width=1,direction='in',top='on')
axs.tick_params(axis='y',which='major',size=8,width=1,direction='in',right='on')

axs.set_ylabel(r'$T_c$', fontsize='large')
axs.set_xlabel('dimension, d', fontsize='large')

axs.scatter(x, y, color='mediumblue')
plt.show()