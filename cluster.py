import pandas as pd
import sys
import numpy as numpy
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import plotly
import matplotlib
import plotly.graph_objs as go

start_table = pd.read_csv("Big-5-Data/data.csv", sep='\t', encoding = 'utf-8')

# print first 5 rows of data
# print(start_table.head())

pers_trait_table = start_table.iloc[:, 7:].copy()

# Average 10 extraversion columns, neuroticism columns, etc. and
#   put averages into a table.
avg_pers_trait_table = pers_trait_table.groupby(numpy.arange(len(pers_trait_table.columns))//10, axis=1).mean()

# Rename columns that got lost in averaging
avg_pers_trait_table.columns = ['E', 'N', 'A', 'C', 'O']

print(avg_pers_trait_table.head())

#------ Visualization ---------------------

#Make Plotly figure
fig1 = go.Scatter3d(x=avg_pers_trait_table['E'],
                  y=avg_pers_trait_table['N'],
                  z=avg_pers_trait_table['A'],
                  mode='markers')

#Make Plot.ly Layout
mylayout = go.Layout(scene=dict(xaxis=dict(title="E"),
                     yaxis=dict(title="N"),
                     zaxis=dict(title="A")))

#Plot and save html
plotly.offline.plot({"data": [fig1],
                     "layout": mylayout},
                     auto_open=True)

# ----------------------------------------


exit()

num_clusters = 5

kmeans = KMeans(n_clusters = num_clusters)
kmeans.fit(avg_pers_trait_table)

print(kmeans)
