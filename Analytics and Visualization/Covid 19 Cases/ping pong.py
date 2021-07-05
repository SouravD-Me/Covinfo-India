import plotly
import matplotlib.pyplot as plt
import pandas as pd

#plt.style.use('bmh')
df = pd.read_csv('Covid 19 Active Cases.csv')

x=df['Date']
y=df['Active_Cases']

plt.xlable('DATE')
plt.ylable('ACTIVE CASES')
plt.bar(x,y)

plt.show()
