import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('BTC_data.csv')

fig = plt.figure(figsize = (16,9))

date = [k[0:10:] for k in df['time'] ]
price = [j for j in df['close'] ]

plt.plot(date[10::], price[10::])

plt.grid()

plt.show()
