import pandas as pd
from matplotlib import pyplot as plt
import requests
import bs4

df = pd.read_csv('drinks.csv')
df.head()
df.dtypes

# 1. Top 10 most beer, spirits, and wine

# Find top 10 countries in each category separately
beer = df.groupby('country', sort=True).sum().sort_values('beer_servings', ascending=False)['beer_servings'].head(10)
spirit = df.groupby('country', sort=True).sum().sort_values('spirit_servings', ascending=False)['spirit_servings'].head(10)
wine = df.groupby('country', sort=True).sum().sort_values('wine_servings', ascending=False)['wine_servings'].head(10)

# Reset index to auto
beer = beer.reset_index()
spirit = spirit.reset_index()
wine = wine.reset_index()

# Renaming columns to avoid conflict
beer.rename({'country': 'country_beer'}, axis=1, inplace=True)
spirit.rename({'country': 'country_spirit'}, axis=1, inplace=True)
wine.rename({'country': 'country_wine'}, axis=1, inplace=True)

# Joining tables
new_table = beer.join(spirit).join(wine)

# Populating the cell_text list
cell_text = []
for row in range(len(new_table)):
    cell_text.append(new_table.loc[row, :])

# The fancy schmancy
fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
ax.table(cellText=cell_text, colLabels=new_table.columns, loc='center')
fig.tight_layout()
plt.show()

# 2. U.S. Alcohol Consumption
# Data: https://pubs.niaaa.nih.gov/publications/Surveillance95/tab1_10.htm

# Scrape the data off the table
res = requests.get('https://pubs.niaaa.nih.gov/publications/Surveillance95/tab1_10.htm')
res.raise_for_status()
page = bs4.BeautifulSoup(res.text, 'html.parser')
type(page)

# Column names are in thead
columns_arr = page.select('thead')
columns = []
for i in range(len(columns_arr)):
    for j in str(columns_arr[i].getText().strip()).split('\n'):
        columns.append(j)

# Create a list from to turn into a data frame
data_arr = page.select('tbody > tr')
data = []
for i in range(len(data_arr)):
    arr = []
    for j in data_arr[i].select('*'):
        if str(j.getText()) != '':
            arr.append(str(j.getText()))
    data.append(arr)

# Create DataFrame
time_series = pd.DataFrame(data=data, columns=columns)

# Regex cuz dat bish be trippin
time_series['Year'] = time_series['Year'].str[:4]
time_series = time_series[time_series.Year.str.match(r'^\d{4}$')]

# Set Year as datetime index
time_series.set_index(pd.DatetimeIndex(time_series.Year), inplace=True)
time_series = time_series.apply(pd.to_numeric)
time_series.loc[:, 'Beer':].plot(kind='line')
plt.show()
