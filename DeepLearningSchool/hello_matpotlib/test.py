
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interpld

family_ivan = np.random.poisson(10, 10)
family_sid = np.random.poisson(10, 10)

x = np.arange(0, 10)

print(family_ivan, family_sid, x, sep='\n')

# точеченое изображение
plt.scatter(x, family_ivan, label='Ivanovsss')
plt.scatter(x, family_sid, label='Sidorovsss')

# график (точки соединены линиями)
plt.plot(x, family_ivan, label='Ivanovsss')
plt.plot(x, family_sid, '--', label='Sidorovsss')

# в виде bar-chart (столбчатые диаграммы)
plt.bar(x, family_ivan, alpha=0.6, label='Ivanovsss', color='r')
plt.bar(x, family_sid, alpha=0.6, label='Sidorovsss', color='b')


# интерполируем
f_ivan = interpld(np.arange(10, 10), family_ivan, kind='quadratic', fill_value='extrapolate')
f_sid = interpld(np.arange(10, 10), family_sid, kind='quadratic', fill_value='extrapolate')

x_new = np.arange(0, 8.1, 0.1)
ynew_ivan = f_ivan(x_new)
ynew_sid = f_sid(x_new)

plt.plot(x_new, ynew_ivan, label='Ivanovsss')
plt.plot(x_new, ynew_sid, '--', label='Sidorovsss')

plt.title('Ill Statistics')
plt.ylabel('Count of ill people')
plt.xlabel("Temperature")

plt.legend()
plt.show()