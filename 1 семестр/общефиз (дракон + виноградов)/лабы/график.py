import matplotlib.pyplot as plt
import numpy as np

# абсциссы
x1 = np.array([1012.7*9.8, 1351.7*9.8, 1844.9*9.8, 2327.3*9.8, 2821.7*9.8])
#x2 = np.array([0, 0.5, 1.2, 1.7, 2.3, 2.8, 3.3, 3.8, 4.2, 4.7])

# ординаты
y1 = [137.4**2, 158.1**2, 182.8**2, 203.9**2, 225**2]
#y2 = [158.2, 315.4, 474.3, 632.5, 789.2, 948.2, 1110, 1266, 1427]
#y3 = [181, 364, 548.3, 731.9, 915.5, 1098, 1284, 1469, 1651]

# создать график
plt.figure()

yerr = [0.038*137.4**2, 0.034*158.1**2, 0.024*182.8**2, 0.017*203.9**2, 0.019*225**2]

# линии  (y^(или v) - желтые треугольники, gs - зеленые квадраты)
plt.errorbar(x1, y1, xerr=0.05*9.8, yerr=yerr, fmt='yo', markersize=4)   # желтый 
#plt.errorbar(x1, y2, xerr=0, yerr=0, label='m = 1351,7 г', fmt='bo', markersize=4)    # синий
#plt.errorbar(x1, y3, xerr=0, yerr=0, label='m = 1844,9 г', fmt='go', markersize=4)   # зеленый
#plt.errorbar(x1, y4, xerr=0, yerr=0, label='m = 2327,3 г', fmt='ro', markersize=4)    # красный
#plt.errorbar(x1, y5, xerr=0, yerr=0, label='m = 2821,7 г', fmt='mo', markersize=4)   # фиолетовый

# заголовок и метки осей
plt.xlabel('сила F')
plt.ylabel('квадрат скорости')


# Вычисление коэффициентов линейной регрессии
A = np.vstack([x1, np.ones(len(x1))]).T
m1, c1 = np.linalg.lstsq(A, y1, rcond=None)[0]
#m2, c2 = np.linalg.lstsq(A, y2, rcond=None)[0]
#m3, c3 = np.linalg.lstsq(A, y3, rcond=None)[0]

# Построение графика
plt.plot(x1, m1*x1 + c1, 'y'.format(m1, c1))
#plt.plot(x1, m2*x1 + c2, 'b'.format(m2, c2))
#plt.plot(x1, m3*x1 + c3, 'g'.format(m3, c3))

# вывод
plt.legend() # легенда
plt.grid()

plt.show()
