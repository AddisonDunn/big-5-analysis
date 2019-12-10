import pandas as pd
import sys
import numpy as numpy
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import plotly
import matplotlib
import plotly.graph_objs as go
import math

# ------- Functions ---------------------------------

def load_csv_to_dataframe(filename):
    # Load from CSV file
    temp_df = pd.read_csv(filename, sep='\t', encoding = 'utf-8')
    # Shuffle rows to get rid of ordering.
    temp_df = temp_df.sample(frac=1).reset_index(drop=True)
    return temp_df

# ----------------------------------------------------

data_filename = "Big-5-Data/data.csv"
start_table = load_csv_to_dataframe(data_filename)

# Grab just the first n rows and cut out demographic data.
first_n_rows = 150
pers_trait_table = start_table.iloc[0:first_n_rows, 7:].copy()

# Average 10 extraversion columns, neuroticism columns, etc. and
#   put averages into a table.
avg_pers_trait_table = pers_trait_table.groupby(numpy.arange(len(pers_trait_table.columns))//10, axis=1).mean()

# Rename columns that got lost in averaging
avg_pers_trait_table.columns = ['E', 'N', 'A', 'C', 'O']

print(avg_pers_trait_table.head())

#------ Visualization - Scatter Plots ---------------------
# Scatter plotting failed due to data being too discrete

# Set marker properties. Put each number in avg_pers_trait_table to the power of
#   two to make differences between points more obvious. Muptiplied by 1.5 just
#   because that factor made the chart look pretty.
markersize = [math.pow(i, 2)*1.5 for i in avg_pers_trait_table['C']]
markercolor = avg_pers_trait_table['O']

#Make Plotly figure
fig1 = go.Scatter3d(x=avg_pers_trait_table['E'],
                  y=avg_pers_trait_table['N'],
                  z=avg_pers_trait_table['A'],
                  marker=dict(size=markersize,
                                color=markercolor,
                                opacity=0.9,
                                reversescale=False,
                                colorscale='Blues'),
                    line=dict (width=0.02),
                    mode='markers')

#Make Plot.ly Layout
mylayout = go.Layout(scene=dict(xaxis=dict(title="Extraversion"),
                     yaxis=dict(title="Neuroticism"),
                     zaxis=dict(title="Agreeableness")))

#Plot and save html
plotly.offline.plot({"data": [fig1],
                     "layout": mylayout},
                     auto_open=True,
                     filename=("5D-Big-5-Plot.html"))

# ------------ Visualization - Histograms -----------------

# Import the libraries
# import matplotlib.pyplot as plt
# import seaborn as sns
#
#
# num_hist_categories = 10
# # matplotlib histogram
# plt.hist(avg_pers_trait_table['E'], color = 'blue', edgecolor = 'black',
#          bins = (1))
#
# # seaborn histogram
# sns.distplot(avg_pers_trait_table['E'], hist=True, kde=False,
#              bins=(1), color = 'blue',
#              hist_kws={'edgecolor':'black'})
# # Add labels
# plt.title('Histogram of Traits')
# plt.xlabel('E')
# plt.ylabel('E Commonality')
#
# plt.tight_layout()
# plt.show()



# --------------------------------------------
exit()

num_clusters = 5

kmeans = KMeans(n_clusters = num_clusters)
kmeans.fit(avg_pers_trait_table)

print(kmeans)
