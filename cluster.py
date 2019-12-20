import pandas as pd
from sklearn.cluster import KMeans

def get_cluster_centers(num_clusters, table):
    kmeans = KMeans(n_clusters = num_clusters)
    kmeans.fit(table)
    return kmeans.cluster_centers_

def simple_cluster(df):

    # My guess at the number of clusters is 5
    cluster_centers = get_cluster_centers(5, df)

    pers_types = []
    pers_labels = ['E', 'N', 'A', 'C', 'O']
    for cluster in cluster_centers:
        temp_string = ''
        temp_list = []
        for x in range(0, 5):
            if cluster[x] < 2.9:
                temp_string = 'low ' + pers_labels[x]
            elif cluster[x] < 3.1:
                temp_string = 'mid ' + pers_labels[x]
            else:
                temp_string = 'high ' + pers_labels[x]
            temp_list.append(temp_string)
        pers_types.append(temp_list)
    print(pers_types)


import scipy.cluster.hierarchy as shc
import matplotlib.pyplot as plt

def show_dendogram(df):
    # We'll get the dendogram of the linkage to see what the best number of
    #   clusters would likely be.
    plt.figure(figsize=(10, 7))
    plt.title("Cluster Dendograms")
    dend = shc.dendrogram(shc.linkage(df, method='ward'))
    plt.show()
