import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('BTC_data.csv')

fig = plt.figure(figsize = (16,9))

date = [k[0:10:] for k in df['time'] ]
time = []
for i in range(len(date)):
    time.append(date[i][8:10] + date[i][4:8] + date[i][2:4])


price = [j for j in df['close'] ]


TimeNumbers = []



x = np.array(time)
y = np.array(price)
for i in range(len(time)):
    TimeNumbers.append(i+1)
x1 = np.array(TimeNumbers)


plt.plot(x, y, 'g', label='Price BTC')
plt.xticks(time[::150])

coefficients = np.polyfit(x1, y, 3)

p = np.poly1d(coefficients)

x_fit = np.linspace(x1.min(), x1.max(), 1457)

y_fit = p(x_fit)

plt.plot(x_fit, y_fit)


plt.grid()
plt.legend()
plt.show()



