#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provide a cluster of the musics with features given by the h5 files
from Million Song Database
"""
import pandas as pnd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn import preprocessing


# %% Importation and first treatments ----------------------------------------
with open("db/h5.csv", 'r') as csvfile:
    table = pnd.DataFrame(pnd.read_csv(csvfile, sep=';'))

numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
dataset = table.select_dtypes(include=numerics)

# Select Lebron James from our dataset
selected_plajyer = dataset.loc[1]

# Variables description
dataset.describe()
# variance(asr) = 0 and variance(energy) = 0 so we remove them
del dataset['asr']
del dataset['energy']
dataset.fit_transform()

# ?? We didn't find Nan but this seems necessary
dataset = dataset.fillna(dataset.mean(), inplace=True)

# Correlations between lines
xcorr = np.corrcoef(dataset)
xcorr = xcorr[np.logical_not(np.isnan(xcorr))]
xcorr.min()

# Correlations between columns
ycorr = np.corrcoef(dataset, rowvar=0)
ycorr = ycorr[np.logical_not(np.isnan(ycorr))]
ycorr.min()

# We scale columns so they will be comparable
df_scaled = preprocessing.scale(dataset)

# %% knn ---------------------------------------------------------------------
# Find the distance from each player in the dataset to lebron.
# lebron_distance = dfnba.apply(euclidean_distance, axis=1)
knn = NearestNeighbors(n_neighbors=3, algorithm='ball_tree').fit(dataset)
knn.kneighbors(dataset)
