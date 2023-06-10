import numpy as np
from scipy.interpolate import RegularGridInterpolator

from src.sda.prepare import load_dataset
from src.utils import path_root

name = 'midgrey'
data = load_dataset(name)
# data[data < 0.78] = np.nan


# xg, yg = np.meshgrid(x, y, indexing='ij')

x = data.index
y = data.columns
data = data.to_numpy()


xg, yg = np.meshgrid(x, y, indexing='ij')
# data = ff(xg, yg)

interp = RegularGridInterpolator((x, y), data, bounds_error=False, fill_value=None)

print(interp((xg,yg)))

import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_subplot(projection='3d')

# ax.scatter(xg.ravel(), yg.ravel(), data.ravel(),
#
#            s=60, c='k', label='data')



X = np.linspace(start=5, stop=70, num=100)
Y = np.linspace(start=0, stop=28, num=100)

Xg, Yg = np.meshgrid(X, Y, indexing='ij')

# interpolator
print(interp((Xg, Yg)))

ax.plot_wireframe(Xg, Yg, interp((Xg, Yg)), rstride=3, cstride=3,alpha=0.4, color='m', label=f'{name}')
ax.set_xlabel('r')
ax.set_ylabel('param 1')
ax.set_zlabel('dopasowanie')


# ground truth

# ax.plot_wireframe(X, Y, ff(X, Y), rstride=3, cstride=3,
#
#                   alpha=0.4, label='ground truth')


plt.legend()
plt.savefig(path_root('plots', 'optimum', name))
plt.show()

plt.imshow(interp((Xg, Yg)), cmap='hot')
plt.show()
