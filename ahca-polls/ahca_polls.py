import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('ahca_polls.csv', encoding='latin-1')

print(df.head())
print(df.describe)
print(df.dtypes)
print(df.columns)
print(df.shape)

# 1. Rolling Average for Net Approval Rating over Time
pd.to_datetime(df["Start_dt"])
df['Net_approval'] = df.Favor - df.Oppose
df.groupby('Start_dt').Net_approval.mean().plot()
plt.show()
# df.plot.scatter(x="Start_dt", y="Net_approval")
df.plot(x="Start_dt", y="Net_approval", style=".")
plt.show()

# 5 Rolling Average: https://stackoverflow.com/questions/40060842/moving-average-pandas

# Method 1 - I don't think this is what I'm looking for
df['Roll_avg'] = df['Net_approval'].rolling(window=5).mean()
df.plot(x="Start_dt", y="Roll_avg", style=".")
plt.show()

# Method 2 - not what I'm looking for, either
plt.plot(df['Net_approval'].rolling(window=5).mean(), label="Net Approval")
plt.show()

# Method 3 - https://stackoverflow.com/questions/15771472/pandas-rolling-mean-by-time-interval
pd.rolling_mean(df.resample('1D', fill_method='ffill'), window=5, min_period=1)

# as of pandas 0.18.0...
df1 = df.set_index('Start_dt')
df1.resample('1d').sum().fillna(0).rolling(window=5, min_periods=1).mean().plot()

# Method that works
ser = df.sort_values('Start_dt', ascending=True)[['Start_dt', 'Net_approval']].set_index('Start_dt').dropna()
plt.scatter(ser.index, ser)
plt.xticks(rotation=90)
plt.show()
