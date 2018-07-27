import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv('airline-safety.csv')
df.head()

# 1. 1985 - 1999 vs 2000 - 2014 Incidents, Fatal Accidents, and Fatalities Table
df[['airline', 'incidents_85_99', 'fatal_accidents_85_99', 'fatalities_85_99']]
df[['airline', 'incidents_00_14', 'fatal_accidents_00_14', 'fatalities_00_14']]

# 2. Fatalities by Airline Correlation between two sets
# Calculate: Deaths per trillion seat kilometers
df['fat_per_km_85_99'] = df.fatalities_85_99 / (df.avail_seat_km_per_week / 1000000000)
df['fat_per_km_00_14'] = df.fatalities_00_14 / (df.avail_seat_km_per_week / 1000000000)

x = df.fat_per_km_85_99
y = df.fat_per_km_00_14
plt.scatter(x, y)

# Draw best fit line
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), 'r--')

plt.grid(True)
plt.xlabel('Fatalities 85 - 99')
plt.ylabel('Fatalities 00 - 14')
plt.show()

# 3. Incidents by airline
df['inc_per_km_85_99'] = df.incidents_85_99 / (df.avail_seat_km_per_week / 1000000000)
df['inc_per_km_00_14'] = df.incidents_00_14 / (df.avail_seat_km_per_week / 1000000000)
x = df.inc_per_km_85_99
y = df.inc_per_km_00_14
plt.scatter(x, y)

# Draw best fit line
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), 'r--')

plt.grid(True)
plt.xlabel('Incidents 85 - 99')
plt.xlabel('Incidents 00 - 14')
plt.show()

# 4. First-World Airlines and Safety Score
