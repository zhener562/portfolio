import poloniex
import time
import datetime
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt

polo = poloniex.Poloniex()
period = polo.DAY # period of data
end = time.time()
start = end - period * 365*10 # 1 year

chart = polo.returnChartData('USDT_BTC', period=period, start=start, end=end)
df = DataFrame.from_dict(chart)
df.head()
timestamp = df['date'].values.tolist() # Series -> ndarray -> list
# timestamp -> year/month/day
date = [datetime.datetime.fromtimestamp(timestamp[i]).date() for i in range(len(timestamp))]

price = df['close'].astype(float)

plt.figure(figsize=(15, 4))
plt.plot(date, price)
plt.show()
#print(price)