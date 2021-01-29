import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import numpy as np

start = dt.datetime(2000, 1, 1)
end = dt.datetime.now()
df = web.DataReader('TSLA', 'yahoo', start, end)  # collects data

print(df.tail())
