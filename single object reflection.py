# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:14:05 2018

@author: Konstantinos
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(.1, 100, .1)
y = 10
z = 2 * np.sqrt(((x/2)**2) + (y**2))

plt.subplot(3, 1, 1)
plt.plot(x,z)
plt.plot(x,x)
plt.xlabel('Real range (m)')
plt.ylabel('Reflection range (m)')
plt.title('Range of the reflected object')
plt.subplots_adjust(hspace = 1)
plt.grid(True)

dzdx = np.gradient(z, .1)

plt.subplot(3, 1, 2)
plt.plot(x,dzdx)
plt.xlabel('Real range (m)')
plt.ylabel('Reflection\'s speed (m)')
plt.title('Relative speed of the reflected object')
plt.subplots_adjust(hspace = 1)
plt.grid(True)

adj = x/2
hyp = z/2
angle = np.degrees(np.arccos(adj/hyp))

plt.subplot(3, 1, 3)
plt.plot(x,angle)
plt.xlabel('Real distance (m)')
plt.ylabel('Reflection\'s angle of arrival (deg)')
plt.title('AoA of the reflected object')
plt.subplots_adjust(hspace = .5)
plt.grid(True)

#plt.tight_layout()
plt.show()

"""
#y = np.arange(0, 100, 0.1)
#xx, yy = np.meshgrid(x, y, sparse=True)
z = 2 * np.sqrt(((xx/2)**2) + (yy**2))
plt.contourf(x,y,z)
"""