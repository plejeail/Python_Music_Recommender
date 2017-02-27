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


# %% Importation and first treatments
with open("db/h5.csv", 'r') as csvfile:
    table = pnd.DataFrame(pnd.read_csv(csvfile, sep=';'))

# index=range(0,10000,1)
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
dataset = table.select_dtypes(include=numerics)

# Select Lebron James from our dataset
selected_player = dataset.loc[1]

# Find the distance from each player in the dataset to lebron.
# lebron_distance = dfnba.apply(euclidean_distance, axis=1)

knn = NearestNeighbors(n_neighbors=3, algorithm='ball_tree').fit(dataset)
knn.kneighbors(dataset)

# BUG SEARCH ---------------------------------------------------------------- #
# Input contains NaN, infinity or a value too large for dtype('float64').
# Check na for all variables
np.isnan(np.sum(dataset))
# Check infinite values for all variables
np.isinf(np.sum(dataset))
# value to large ???
dataset2 = np.round(dataset, 2)
knn = NearestNeighbors(n_neighbors=3, algorithm='ball_tree').fit(dataset2)
# no
# Try with scaled variables
df_scaled = preprocessing.scale(dataset)
# same problem
for i in range(dataset.shape[1]):
    preprocessing.scale(dataset.iloc[:, i])
# variable by variable doesn't seems to cause problems
for i in range(dataset.shape[1]):
    try:
        preprocessing.scale(dataset.iloc[:, -i])
    except:
        print(i)
# problems when we remove 12, 13, 14, 15 but not the others
# works whithout year
preprocessing.scale(dataset.iloc[:, -1])
# Therefore, I will continue without year
