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

############# Main #################################

from visualization import generateScatterPlot

def main():

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

    # generateScatterPlot("5D-Big-5-Plot.html", avg_pers_trait_table)



    # --------------------------------------------
    exit()

    num_clusters = 5

    kmeans = KMeans(n_clusters = num_clusters)
    kmeans.fit(avg_pers_trait_table)

    print(kmeans)


if __name__ == '__main__':
    main()
