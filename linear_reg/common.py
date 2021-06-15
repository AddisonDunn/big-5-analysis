
import pandas as pd
import sys
import numpy as numpy

############# Functions #############################

def load_csv_to_dataframe(filename):
    # Load from CSV file
    temp_df = pd.read_csv(filename, sep='\t')
    # Shuffle rows to get rid of ordering.
    # temp_df = temp_df.sample(frac=1).reset_index(drop=True)
    return temp_df

def pers_averages(df):
    df = df.iloc[:, 7:].copy()

    # Average 10 extraversion answers, neuroticism answers, etc. and
    #   put averages into a new table.
    df = df.groupby(numpy.arange(len(df.columns))//10, axis=1).mean()

    # Rename columns that got lost in averaging
    df.columns = ['E', 'N', 'A', 'C', 'O']

    return df
