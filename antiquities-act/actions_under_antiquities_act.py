import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('actions_under_antiquities_act.csv')

# Too many NaN's on the dancefloor
df.isnull().sum()

# Data wrangling this bish
df.acres_affected = df.acres_affected.str.replace(r'[\D]', '').astype('float64')
df.groupby('pres_or_congress', sort=True)['acres_affected'].sum().sort_values(ascending=False).head().plot(kind='barh')

# Plot upside-down? Flip dat bish
plt.gca().invert_yaxis()  # gca stands for 'get current axis' https://matplotlib.org/api/_as_gen/matplotlib.pyplot.gca.html, https://stackoverflow.com/questions/34076177/matplotlib-horizontal-bar-chart-barh-is-upside-down
