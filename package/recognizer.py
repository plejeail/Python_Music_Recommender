#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module is used for the recognition of audio files. Files must be read by
the program.
"""
import fingerprinter as fp
import dbtools as dbtools
import glob

DB_FOLDER = "db/"


# %% get track name and infos
def get_track(file):
    # open the fingerprints database
    sqldb = dbtools.Dbread(DB_FOLDER + "fingers.db")

    fingerprint = fp.hashaudio(file)

    sql = "SELECT * FROM fingerprints WHERE fingerprint = '" + \
          fingerprint + "'"
    track_id, title, artist = sqldb.request(sql)[0][:3]
    sqldb.close()

    return {"track_id": track_id, "title": title, "artist": artist}


# %% get all ids from a directory
def get_folder_id(folder):
    if folder[-1:] not in ("/", "\\"):
        folder = folder + "/"

    folder = folder + "*.wav"
    files = glob.glob(folder)
    return [get_track(f)["track_id"] for f in files]


# %% get infos from track_metadata.db
def get_metadata(file):
    track_id = get_track(file)["track_id"]
    # open the track_metadata.db
    sqldb = dbtools.Dbread(DB_FOLDER + "track_metadata.db")
    colnames = [col[1] for col in sqldb.columns("songs")]

    query = sqldb.request("SELECT * from songs WHERE track_id = '" + track_id +
                          "'")[0]

    data = {}
    for i in range(len(query)):
        c = colnames[i]
        q = query[i]
        data[c] = q
    return data


# %% Test
if __name__ == "__main__":
    audiofile = "/home/gevisk/Programs/Python/Python_Music_Recommender/package/wav/Gold Panda - Fifth Ave.mp3.wav"
    folder = "/home/gevisk/Programs/Python/Python_Music_Recommender/package/wav"

    print(get_track(audiofile))
    trackid = get_track(audiofile)["track_id"]  # get id of a track
    get_folder_id(folder)  # get the id for all files of a folder
    # get_metadata(audiofile)
