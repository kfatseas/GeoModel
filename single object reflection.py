# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 14:14:05 2018

@author: Konstantinos
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(.1, 100, .1)
y = 30
z = 2 * np.sqrt(((x/2)**2) + (y**2))

plt.subplot(2, 1, 1)
plt.plot(x,z)
plt.xlabel('Real distance (m)')
plt.ylabel('Reflection distance (m)')
plt.title('Distance of the reflected object')
plt.grid(True)

adj = x/2
hyp = z/2
angle = np.degrees(np.arccos(adj/hyp))

plt.subplot(2, 1, 2)
plt.plot(x,angle)
plt.xlabel('Real distance (m)')
plt.ylabel('Reflection\'s angle of arrival (deg)')
plt.title('AoA of the reflected object')
plt.grid(True)

plt.tight_layout()
plt.show()

"""
#y = np.arange(0, 100, 0.1)
#xx, yy = np.meshgrid(x, y, sparse=True)
z = 2 * np.sqrt(((xx/2)**2) + (yy**2))
plt.contourf(x,y,z)
"""