#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provide a class to ease the use of h5 files and convert the MSongDB
subset of 10 000 h5 files in the csv format
"""
import tables
import csv
import os


# %% H5 File
class h5file:
    """
    Cette classe contient un fichier h5 et des methodes pour nous
    simplifier la vie
    """
    def __init__(self, h5filename):
        self.h5 = tables.open_file(h5filename, mode='r')

    # @property sert à definir une propriete (fonction sans arguments)
    # on l'appelle comme ça : nom_classe.nom_propriete
    @property
    def nbsongs(self):
        """
            nombre de chansons contenues dans le fichier h5
        """
        return self.h5.root.metadata.songs.nrows

    def artist_familiarity(self, songidx=0):
        """
        Get artist familiarity by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.artist_familiarity[songidx]

    def artist_hot(self, songidx=0):
        """
        Get artist hotttnesss by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.artist_hotttnesss[songidx]

    def artist_id(self, songidx=0):
        """
        Get artist id by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.artist_id[songidx]

    def artist_latitude(self, songidx=0):
        """
        Get artist latitude by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.artist_latitude[songidx]

    def artist_longitude(self, songidx=0):
        """
        Get artist longitude by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.artist_longitude[songidx]

    def artist_location(self, songidx=0):
        """
        Get artist location by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.artist_location[songidx]

    def artist_name(self, songidx=0):
        """
        Get artist name by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.artist_name[songidx]

    def release(self, songidx=0):
        """
        Get release by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.release[songidx]

    def song_id(self, songidx=0):
        """
        Get song id by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.song_id[songidx]

    def song_hot(self, songidx=0):
        """
        Get song hotttnesss by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.song_hotttnesss[songidx]

    def title(self, songidx=0):
        """
        Get title by default the first song in it
        """
        return self.h5.root.metadata.songs.cols.title[songidx]

    def similar_artists(self, songidx=0):
        """
        Get similar artists array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.metadata.songs.nrows == songidx + 1:
            return self.h5.root.metadata.similar_artists[self.h5.root.metadata.songs.cols.idx_similar_artists[songidx]:]
        return self.h5.root.metadata.similar_artists[self.h5.root.metadata.songs.cols.idx_similar_artists[songidx]:
                                                self.h5.root.metadata.songs.cols.idx_similar_artists[songidx+1]]

    def artist_terms(self, songidx=0):
        """
        Get artist terms array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.metadata.songs.nrows == songidx + 1:
            return self.h5.root.metadata.artist_terms[self.h5.root.metadata.songs.cols.idx_artist_terms[songidx]:]
        return self.h5.root.metadata.artist_terms[self.h5.root.metadata.songs.cols.idx_artist_terms[songidx]:
                                                self.h5.root.metadata.songs.cols.idx_artist_terms[songidx+1]]

    def artist_terms_freq(self, songidx=0):
        """
        Get artist terms array frequencies. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.metadata.songs.nrows == songidx + 1:
            return self.h5.root.metadata.artist_terms_freq[self.h5.root.metadata.songs.cols.idx_artist_terms[songidx]:]
        return self.h5.root.metadata.artist_terms_freq[self.h5.root.metadata.songs.cols.idx_artist_terms[songidx]:
                                                  self.h5.root.metadata.songs.cols.idx_artist_terms[songidx+1]]

    def artist_terms_weight(self, songidx=0):
        """
        Get artist terms array frequencies. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.metadata.songs.nrows == songidx + 1:
            return self.h5.root.metadata.artist_terms_weight[self.h5.root.metadata.songs.cols.idx_artist_terms[songidx]:]
        return self.h5.root.metadata.artist_terms_weight[self.h5.root.metadata.songs.cols.idx_artist_terms[songidx]:
                                                    self.h5.root.metadata.songs.cols.idx_artist_terms[songidx+1]]

    def analysis_sample_rate(self, songidx=0):
        """
        Get analysis sample rate by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.analysis_sample_rate[songidx]

    def danceability(self, songidx=0):
        """
        Get danceability by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.danceability[songidx]

    def duration(self, songidx=0):
        """
        Get duration by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.duration[songidx]

    def end_of_fade_in(self, songidx=0):
        """
        Get end of fade in by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.end_of_fade_in[songidx]

    def energy(self, songidx=0):
        """
        Get energy by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.energy[songidx]

    def key(self, songidx=0):
        """
        Get key by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.key[songidx]

    def key_confidence(self, songidx=0):
        """
        Get key confidence by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.key_confidence[songidx]

    def loudness(self, songidx=0):
        """
        Get loudness by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.loudness[songidx]

    def mode(self, songidx=0):
        """
        Get mode by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.mode[songidx]

    def start_of_fade_out(self, songidx=0):
        """
        Get start of fade out by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.start_of_fade_out[songidx]

    def tempo(self, songidx=0):
        """
        Get tempo by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.tempo[songidx]

    def time_signature(self, songidx=0):
        """
        Get signature by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.time_signature[songidx]

    def time_signature_confidence(self, songidx=0):
        """
        Get signature confidence by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.time_signature_confidence[songidx]

    def track_id(self, songidx=0):
        """
        Get track id by default the first song in it
        """
        return self.h5.root.analysis.songs.cols.track_id[songidx]

    def segments_start(self, songidx=0):
        """
        Get segments start array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.segments_start[self.h5.root.analysis.songs.cols.idx_segments_start[songidx]:]
        return self.h5.root.analysis.segments_start[self.h5.root.analysis.songs.cols.idx_segments_start[songidx]:
                                               self.h5.root.analysis.songs.cols.idx_segments_start[songidx+1]]

    def segments_pitches(self, songidx=0):
        """
        Get segments pitches array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.segments_pitches[self.h5.root.analysis.songs.cols.idx_segments_pitches[songidx]:,:]
        return self.h5.root.analysis.segments_pitches[self.h5.root.analysis.songs.cols.idx_segments_pitches[songidx]:
                                                 self.h5.root.analysis.songs.cols.idx_segments_pitches[songidx+1],:]

    def segments_timbre(self, songidx=0):
        """
        Get segments timbre array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.segments_timbre[self.h5.root.analysis.songs.cols.idx_segments_timbre[songidx]:,:]
        return self.h5.root.analysis.segments_timbre[self.h5.root.analysis.songs.cols.idx_segments_timbre[songidx]:
                                                self.h5.root.analysis.songs.cols.idx_segments_timbre[songidx+1],:]

    def segments_loudness_max(self, songidx=0):
        """
        Get segments loudness max array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.segments_loudness_max[self.h5.root.analysis.songs.cols.idx_segments_loudness_max[songidx]:]
        return self.h5.root.analysis.segments_loudness_max[self.h5.root.analysis.songs.cols.idx_segments_loudness_max[songidx]:
                                                      self.h5.root.analysis.songs.cols.idx_segments_loudness_max[songidx+1]]

    def segments_loudness_max_time(self, songidx=0):
        """
        Get segments loudness max time array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.segments_loudness_max_time[self.h5.root.analysis.songs.cols.idx_segments_loudness_max_time[songidx]:]
        return self.h5.root.analysis.segments_loudness_max_time[self.h5.root.analysis.songs.cols.idx_segments_loudness_max_time[songidx]:
                                                           self.h5.root.analysis.songs.cols.idx_segments_loudness_max_time[songidx+1]]

    def segments_loudness_start(self, songidx=0):
        """
        Get segments loudness start array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.segments_loudness_start[self.h5.root.analysis.songs.cols.idx_segments_loudness_start[songidx]:]
        return self.h5.root.analysis.segments_loudness_start[self.h5.root.analysis.songs.cols.idx_segments_loudness_start[songidx]:
                                                        self.h5.root.analysis.songs.cols.idx_segments_loudness_start[songidx+1]]

    def sections_start(self, songidx=0):
        """
        Get sections start array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.sections_start[self.h5.root.analysis.songs.cols.idx_sections_start[songidx]:]
        return self.h5.root.analysis.sections_start[self.h5.root.analysis.songs.cols.idx_sections_start[songidx]:
                                               self.h5.root.analysis.songs.cols.idx_sections_start[songidx+1]]

    def beats_start(self, songidx=0):
        """
        Get beats start array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.beats_start[self.h5.root.analysis.songs.cols.idx_beats_start[songidx]:]
        return self.h5.root.analysis.beats_start[self.h5.root.analysis.songs.cols.idx_beats_start[songidx]:
                                            self.h5.root.analysis.songs.cols.idx_beats_start[songidx+1]]

    def bars_start(self, songidx=0):
        """
        Get bars start array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.bars_start[self.h5.root.analysis.songs.cols.idx_bars_start[songidx]:]
        return self.h5.root.analysis.bars_start[self.h5.root.analysis.songs.cols.idx_bars_start[songidx]:
                                           self.h5.root.analysis.songs.cols.idx_bars_start[songidx+1]]

    def tatums_start(self, songidx=0):
        """
        Get tatums start array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.analysis.songs.nrows == songidx + 1:
            return self.h5.root.analysis.tatums_start[self.h5.root.analysis.songs.cols.idx_tatums_start[songidx]:]
        return self.h5.root.analysis.tatums_start[self.h5.root.analysis.songs.cols.idx_tatums_start[songidx]:
                                             self.h5.root.analysis.songs.cols.idx_tatums_start[songidx+1]]

    def artist_mbtags(self, songidx=0):
        """
        Get artist musicbrainz tag array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.musicbrainz.songs.nrows == songidx + 1:
            return self.h5.root.musicbrainz.artist_mbtags[self.h5.root.musicbrainz.songs.cols.idx_artist_mbtags[songidx]:]
        return self.h5.root.musicbrainz.artist_mbtags[self.h5.root.metadata.songs.cols.idx_artist_mbtags[songidx]:
                                                 self.h5.root.metadata.songs.cols.idx_artist_mbtags[songidx+1]]

    def nb_mbtags(self, songidx=0):
        """
        Get artist musicbrainz tag count array. Takes care of the proper indexing if we are in aggregate
        file. By default, return the array for the first song in the h5 file.
        To get a regular numpy ndarray, cast the result to: numpy.array( )
        """
        if self.h5.root.musicbrainz.songs.nrows == songidx + 1:
            return self.h5.root.musicbrainz.artist_mbtags_count[self.h5.root.musicbrainz.songs.cols.idx_artist_mbtags[songidx]:]
        return self.h5.root.musicbrainz.artist_mbtags_count[self.h5.root.metadata.songs.cols.idx_artist_mbtags[songidx]:
                                                       self.h5.root.metadata.songs.cols.idx_artist_mbtags[songidx+1]]

    def year(self, songidx=0):
        """
        Get release year by default the first song in it
        """
        return self.h5.root.musicbrainz.songs.cols.year[songidx]

    def id7digital(self, songidx=0):
        return self.h5.root.metadata.songs.cols.release_7digitalid[songidx]


# %% Write to CSV

# le fichier racine contenant les h5 doit etre dans le meme dossier
# que le script, c'est le dossier avec les 2 dossiers A et B a l'interieur
h5files = []
for root, dirs, files in os.walk("h5/", topdown=False):
    for name in files:
        h5files.append(os.path.join(root, name))
# h5files contient l'adresse de tous les fichiers h5

with open('db/h5.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile,
                            delimiter=';',
                            quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)

    spamwriter.writerow(['track_id', 'mbtags',
                         'title', 'artist_name', 'release', 'artist_hot', 'song_hot',
                         'danceability', 'year', 'tempo', 'time_signature', 'asr',
                         'mean_section_start', 'mean_beats_start', 'mean_bars_start',
                         'mean_tatums_start', 'key', 'mode', 'mean_segments_loudness_start',
                         'mean_segments_loudness_max_time', 'max_segments_loudness',
                         'mean_segments_timbre', 'mean_segments_pitches', 'first_segments_start',
                         'start_of_fade_out', 'loudness',
                         'energy'])

    for file in h5files:
        myh5 = h5file(file)
        a = i = -1
        while a <= 0:
            i = i + 1
            a = myh5.segments_start(0)[i]

        if len(myh5.artist_mbtags(0)) > 0:
            tag = myh5.artist_mbtags(0)[0]
        else:
            tag = "NA"

        row = [myh5.track_id(0), tag,
               myh5.title(0), myh5.artist_name(0), myh5.release(0),
               myh5.artist_hot(0), myh5.song_hot(0), myh5.danceability(0),
               myh5.year(0), myh5.tempo(0),
               myh5.time_signature(0),
               myh5.analysis_sample_rate(0), mean(myh5.sections_start(0)),
               mean(myh5.beats_start(0)), mean(myh5.bars_start(0)),
               mean(myh5.tatums_start(0)), myh5.key(0), myh5.mode(0),
               mean(myh5.segments_loudness_start(0)),
               mean(myh5.segments_loudness_max_time(0)),
               max(myh5.segments_loudness_max(0)),
               mean(myh5.segments_timbre(0)), mean(myh5.segments_pitches(0)),
               a, myh5.start_of_fade_out(0), myh5.loudness(0),
               myh5.energy(0)]
        spamwriter.writerow(row)
        myh5.h5.close()
