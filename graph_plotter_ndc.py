import pandas as pd
import matplotlib.pyplot as plt

# read CSV file into a pandas dataframe
# df = pd.read_csv('filename.csv')
df = pd.read_csv('./matrix_data/contract_count_ndc.csv')

# create a histogram of the values in the column you want to graph
plt.hist(df['Contracts'], bins=range(min(df['Contracts']), max(df['Contracts']) + 1, 1),edgecolor='black')

# set the title and axis labels
plt.title('Histogram')
plt.xlabel('Number of contract declarations')
plt.ylabel('Frequency')

# display the graph
plt.show()