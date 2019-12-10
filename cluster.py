import pandas as pd
import sys
import numpy as numpy
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import plotly
import matplotlib
import plotly.graph_objs as go

# ------- Functions ---------------------------------

def load_csv_to_dataframe(filename):
    return pd.read_csv(filename, sep='\t', encoding = 'utf-8')

# ----------------------------------------------------

data_filename = "Big-5-Data/data.csv"
start_table = load_csv_to_dataframe(data_filename)


# print first 5 rows of data
# print(start_table.head())

# Grab just the first n rows and cut out demographic data.
first_n_rows = 10000
pers_trait_table = start_table.iloc[0:first_n_rows, 7:].copy()

# Average 10 extraversion columns, neuroticism columns, etc. and
#   put averages into a table.
avg_pers_trait_table = pers_trait_table.groupby(numpy.arange(len(pers_trait_table.columns))//10, axis=1).mean()

# Rename columns that got lost in averaging
avg_pers_trait_table.columns = ['E', 'N', 'A', 'C', 'O']

print(avg_pers_trait_table.head())

#------ Scatter Plot ---------------------
# Scatter plotting failed due to data being too discrete

#Set marker properties
markersize = avg_pers_trait_table['C']
markercolor = avg_pers_trait_table['O']

#Make Plotly figure
fig1 = go.Scatter3d(x=avg_pers_trait_table['E'],
                  y=avg_pers_trait_table['N'],
                  z=avg_pers_trait_table['A'],
                  marker=dict(size=markersize,
                                color=markercolor,
                                opacity=0.9,
                                reversescale=True,
                                colorscale='Blues'),
                    line=dict (width=0.02),
                    mode='markers')

#Make Plot.ly Layout
mylayout = go.Layout(scene=dict(xaxis=dict(title="E"),
                     yaxis=dict(title="N"),
                     zaxis=dict(title="A")))

#Plot and save html
plotly.offline.plot({"data": [fig1],
                     "layout": mylayout},
                     auto_open=True,
                     filename=("5D Plot.html"))

# ------------ Visualization -----------------



# --------------------------------------------
exit()

num_clusters = 5

kmeans = KMeans(n_clusters = num_clusters)
kmeans.fit(avg_pers_trait_table)

print(kmeans)
