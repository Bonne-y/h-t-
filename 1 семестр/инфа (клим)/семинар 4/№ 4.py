import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('iris_data.csv')

fig = plt.figure(figsize = (16,9))
a1 = fig.add_subplot(631)
a2 = fig.add_subplot(632)
a3 = fig.add_subplot(633)
a4 = fig.add_subplot(634)
a5 = fig.add_subplot(635)
a6 = fig.add_subplot(636)

SL = [l for l in df['SepalLengthCm'] ]
SW = [k for k in df['SepalWidthCm'] ]
PL = [m for m in df['PetalLengthCm'] ]
PW = [n for n in df['PetalWidthCm'] ]

a1.plot(SL, SW, label = '1')
a2.plot(SL, PW, label = '2')
a3.plot(SW, SL, label = '3')
a4.plot(SW, PL, label = '4')
a5.plot(PL, PW, label = '5')
a6.plot(PW, PL, label = '6')

a1.legend()
a2.legend()
a3.legend()
a4.legend()
a5.legend()
a6.legend()

plt.show()
