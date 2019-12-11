import pandas as pd
import sys
import numpy as numpy
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

############# Functions #############################

def load_csv_to_dataframe(filename):
    # Load from CSV file
    temp_df = pd.read_csv(filename, sep='\t', encoding = 'utf-8')
    # Shuffle rows to get rid of ordering.
    temp_df = temp_df.sample(frac=1).reset_index(drop=True)
    return temp_df

def clean_data(my_df):
    my_df = my_df.iloc[:, 7:].copy()

    # Average 10 extraversion answers, neuroticism answers, etc. and
    #   put averages into a new table.
    my_df = my_df.groupby(numpy.arange(len(my_df.columns))//10, axis=1).mean()

    # Rename columns that got lost in averaging
    my_df.columns = ['E', 'N', 'A', 'C', 'O']

    return my_df

def get_cluster_centers(num_clusters, table):
    kmeans = KMeans(n_clusters = num_clusters)
    kmeans.fit(table)
    return kmeans.cluster_centers_


############# Main #################################

from visualization import generateScatterPlot

data_filename = "Big-5-Data/data.csv"

def main():

    start_table = load_csv_to_dataframe(data_filename)

    # Cut out demographic data
    pers_trait_table = clean_data(start_table)

    # print(avg_pers_trait_table.head())

    # generateScatterPlot("5D-Big-5-Plot.html", avg_pers_trait_table)

    # My guess at the number of clusters is 5
    cluster_centers = get_cluster_centers(5, pers_trait_table)

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







if __name__ == '__main__':
    main()
