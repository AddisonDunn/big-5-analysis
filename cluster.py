import pandas as pd
import sys
import numpy as numpy
from sklearn.cluster import KMeans

start_table = pd.read_csv("Big-5-Data/data.csv", sep='\t', encoding = 'utf-8')

# print first 5 rows of data
# print(start_table.head())

pers_trait_table = start_table.iloc[:, 7:].copy()

# Average 10 extraversion columns, neuroticism columns, etc. and
#   put averages into a table.

avg_pers_trait_table = pers_trait_table.groupby(numpy.arange(len(pers_trait_table.columns))//10, axis=1).mean())

exit()

num_clusters = 5

kmeans = KMeans(n_clusters = num_clusters)
kmeans.fit(pers_trait_table)

print(kmeans.labels_)
