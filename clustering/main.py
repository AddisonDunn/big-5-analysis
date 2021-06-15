
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

def clean_data(df):
    df = df.iloc[:, 7:].copy()

    # Average 10 extraversion answers, neuroticism answers, etc. and
    #   put averages into a new table.
    df = df.groupby(numpy.arange(len(df.columns))//10, axis=1).mean()

    # Rename columns that got lost in averaging
    df.columns = ['E', 'N', 'A', 'C', 'O']

    return df

############# Main #################################

from visualization import generateScatterPlot
from cluster import simple_cluster
from cluster import show_dendogram
from sklearn.cluster import AgglomerativeClustering


data_filename = "../Big-5-Data/data.csv"

def main():
    start_table = load_csv_to_dataframe(data_filename)

    # Cut out demographic data
    pers_trait_table = clean_data(start_table)

    print(pers_trait_table.head())

    # generateScatterPlot("5D-Big-5-Plot.html", pers_trait_table)

    # simple_cluster(pers_trait_table)

    # show_dendogram(pers_trait_table)

    # According to dendogram, 4 or even clusters look like the most effective
    #   option (longing vertical distance without a horizontal line).
    # aggl_cluster = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='ward')
    # aggl_cluster.fit_predict(pers_trait_table)






if __name__ == '__main__':
    main()
