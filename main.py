# Part 0 - Import
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

# Part 1 - Getting Data
start = datetime.datetime(2017, 1, 1)
end = datetime.datetime(2022, 1, 1)
TSLA = web.get_data_yahoo('TSLA', start=start, end=end)
TSLA.to_csv('TSLA.csv')
F = web.get_data_yahoo('F', start=start, end=end)
F.to_csv('F.csv')
GM = web.get_data_yahoo('GM', start=start, end=end)
GM.to_csv('GM.csv')


# Part 2 - Visualizing Data
# Trend
TSLA['Close'].plot(label='TSLA', figsize=(16, 8), title='Closing Prices')
GM['Close'].plot(label='GM')
F['Close'].plot(label='F')
plt.legend()
plt.show()

# Volume
TSLA['Volume'].plot(label='TSLA', figsize=(16, 8), title='Volume Traded')
GM['Volume'].plot(label='GM')
F['Volume'].plot(label='F')
plt.legend()
plt.show()
# What happened that day
print(TSLA['Volume'].argmax())
print(GM['Volume'].argmax())
print(F['Volume'].argmax())

