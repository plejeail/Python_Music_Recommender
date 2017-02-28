#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provide a cluster of the musics with features given by the h5 files
from Million Song Database
"""
import pandas as pnd
import matplotlib.pyplot as plt
import matplotlib
from scipy.spatial import distance
import math


matplotlib.style.use('ggplot')

# %% Importation and first treatments ----------------------------------------
with open("db/h5.csv", 'r') as csvfile:
    table = pnd.DataFrame(pnd.read_csv(csvfile, sep=';'))

info = table.iloc[:, :5]
numerics = table.iloc[:, 5:]

"""
# Variables description
# numerics.describe()
# variance(asr) = 0 and variance(energy) = 0 so we remove them
del numerics['danceability']
del numerics['asr']
del numerics['energy']

# ?? We didn't find Nan but this seems necessary
numerics = numerics.fillna(numerics.mean(), inplace=True)

# Correlations between lines
xcorr = np.corrcoef(numerics)
xcorr = xcorr[np.logical_not(np.isnan(xcorr))]
xcorr.min()

# Correlations between columns
ycorr = np.corrcoef(numerics, rowvar=0)
ycorr = ycorr[np.logical_not(np.isnan(ycorr))]
ycorr.min()

# We scale columns so they will be comparable
df_scaled = preprocessing.scale(numerics)
"""

# %% knn ---------------------------------------------------------------------
# Find the distance from each player in the dataset to lebron.
# lebron_distance = dfnba.apply(euclidean_distance, axis=1)
# knn = NearestNeighbors(n_neighbors=3, algorithm='ball_tree')
# knn.fit(df_scaled)

# Select Lebron James from our dataset
# track_id = .iloc[1,0]


def recommendation(track_id):
    """
    recommendation using
    """
    # columns used for recommendation
    distance_columns = ['tempo', 'mean_section_start', 'mean_beats_start',
                        'mean_bars_start', 'mean_tatums_start', 'key', 'mode',
                        'mean_segments_loudness_start',
                        'mean_segments_loudness_max_time',
                        'max_segments_loudness', 'mean_segments_timbre',
                        'mean_segments_pitches', 'first_segments_start',
                        'start_of_fade_out', 'loudness',
                        'artist_hot', 'song_hot', 'time_signature']

    def euclidean_distance(row, track):
        """
        A simple euclidean distance function
        """
        inner_value = 0
        for k in distance_columns:
            inner_value += (row[k] - track[k]) ** 2
        return math.sqrt(inner_value)

    # Select only the numeric columns from the NBA dataset
    dataset_numeric = numerics[distance_columns]

    # Normalize all of the numeric columns
    df_scaled = (dataset_numeric - dataset_numeric.mean()) / dataset_numeric.std()
    # use df_scaled

    # Fill in NA values in nba_normalized
    df_scaled.fillna(0, inplace=True)

    # Find the normalized vector for track.
    track_val = df_scaled[info["track_id"] == "b'" + track_id + "'"]

    # Find the distance between lebron james and everyone else.
    euclidean_distances = df_scaled.apply(lambda row: distance.euclidean(row, track_val),
                                          axis=1)

    # Create a new dataframe with distances.
    distance_frame = pnd.DataFrame(data={"dist": euclidean_distances,
                                         "idx": euclidean_distances.index})
    distance_frame.sort("dist", inplace=True)
    # Find the most similar player to track (the lowest distance to track is
    # lebron, the second smallest is the most similar non-lebron player)
    # 0 is the music
    first = distance_frame.iloc[1]
    second = distance_frame.iloc[2]
    third = distance_frame.iloc[3]
    dist_values = pnd.DataFrame(data={"id": [1, 2, 3],
                                      "dist": [first["dist"], second["dist"],
                                               third["dist"]]})
    dist_values.plot(kind="scatter")

    return (info.loc[int(first["idx"])],
            info.loc[int(second["idx"])],
            info.loc[int(third["idx"])])

"""
obsolete code
#  MeanShift ---------------------------------------------------------------
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
# le plot est "special" mais il est fait sur deux variable et y en a 18

#  kmeans, une methode brutale ----------------------------------------------
mykmean = KMeans(n_clusters=2, random_state=0)
mykmean.fit(df_scaled)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!DANGER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
# silhouette_score(df_scaled, mykmean.labels_) # Attention instruction merdique
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
"""
