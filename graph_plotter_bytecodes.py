import pandas as pd
import matplotlib.pyplot as plt

# read CSV file into a pandas dataframe
# df = pd.read_csv('filename.csv')
df = pd.read_csv('./matrix_data/bytecode_length.csv')

# create a histogram of the values in the column you want to graph
plt.hist(df['Byte Code Length'], bins=range(min(df['Byte Code Length']), max(df['Byte Code Length']) + 500, 500),edgecolor='black')

# set the title and axis labels
plt.title('Histogram')
plt.xlabel('Byte Code Length')
plt.ylabel('Frequency')

# display the graph
plt.show()


