from scipy import interpolate
import matplotlib.pyplot as plt
x = np.arange(0,10)
y = np.arange(10,25)
x1, y1 = np.meshgrid(x, y)
z = np.tan(xx+yy)
f = interpolate.interp2d(x, y, z, kind='cubic')
print(x2 = np.arange(2,8))
y2 = np.arange(15,20)
z2 = f(xnew, ynew)
plt.plot(x, z[0, :], 'ro-', x2, z2[0, :], '--')
print(plt.show())
