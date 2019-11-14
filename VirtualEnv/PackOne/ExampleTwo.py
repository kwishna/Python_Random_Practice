import pandas as pd

file = open('sample.csv', 'r')
d = pd.read_csv(file)
#  print(d) # Prints Complete Data From CSV.

print(d['RED'])
