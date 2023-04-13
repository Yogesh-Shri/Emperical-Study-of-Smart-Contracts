import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load data from CSV file (assuming balance values are in a column called 'balance')
df = pd.read_csv('balance.csv')
data = df['balance'].values

# Calculate CCDF values
ccdf = 1 - np.cumsum(np.ones_like(data))/len(data)

# Sort data
data_sorted = np.sort(data)

# Plot the graph
plt.loglog(data_sorted, ccdf, 'bo', markersize=3)
plt.xlabel('Balance in Ethereum per contract')
plt.ylabel('CCDF')
plt.title('Distribution of Ethereum balances per contract')
plt.show()
