#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provide a cluster of the musics with features given by the h5 files
from Million Song Database
"""
import pandas as pnd
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
from sklearn.neighbors import NearestNeighbors
from sklearn import preprocessing
from sklearn.cluster import MeanShift, estimate_bandwidth, KMeans
from sklearn.metrics import silhouette_score
from scipy.spatial import distance

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
knn = NearestNeighbors(n_neighbors=3, algorithm='ball_tree')
knn.fit(df_scaled)

def euclidean_distance(row):
    """
    A simple euclidean distance function
    """
    inner_value = 0
    for k in distance_columns:
        inner_value += (row[k] - selected_player[k]) ** 2
    return math.sqrt(inner_value)

lebron_distance = dataset.apply(euclidean_distance, axis=1)

# Select only the numeric columns from the NBA dataset
dataset_numeric = dataset[distance_columns]

# Normalize all of the numeric columns
dataset_normalized = (dataset_numeric - dataset_numeric.mean()) / dataset_numeric.std()

# Fill in NA values in nba_normalized
dataset_normalized.fillna(0, inplace=True)

# Find the normalized vector for lebron james.
lebron_normalized = dataset_normalized[table["title"] == "b'Sincerely'"]

# Find the distance between lebron james and everyone else.
euclidean_distances = dataset_normalized.apply(lambda row: distance.euclidean(row, lebron_normalized), axis=1)

# Create a new dataframe with distances.
distance_frame = pnd.DataFrame(data={"dist": euclidean_distances, "idx": euclidean_distances.index})
distance_frame.sort("dist", inplace=True)
# Find the most similar player to lebron (the lowest distance to lebron is lebron, the second smallest is the most similar non-lebron player)
second_smallest = distance_frame.iloc[1]["idx"]
#most_similar_to_lebron = dataset.loc[int(second_smallest)]["title"]


# %% MeanShift ---------------------------------------------------------------
# The following bandwidth can be automatically detected using
bandwidth = estimate_bandwidth(df_scaled, quantile=0.2, n_samples=500)

ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(df_scaled)
labels = ms.labels_
cluster_centers = ms.cluster_centers_

labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)

print("number of estimated clusters : %d" % n_clusters_)

plt.figure(1)
plt.clf()

colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    my_members = labels == k
    cluster_center = cluster_centers[k]
    plt.plot(df_scaled[my_members, 0], df_scaled[my_members, 1], col + '.')
    plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)
plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()
# le plot est chelou mais il est fait sur deux variable et y en a 18

# %% kmeans, une methode brutale ----------------------------------------------
mykmean = KMeans(n_clusters=2, random_state=0)
mykmean.fit(df_scaled)
# l'erreur d'une vie en approche
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!DANGER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
# silhouette_score(df_scaled, mykmean.labels_) # Attention instruction merdique
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
