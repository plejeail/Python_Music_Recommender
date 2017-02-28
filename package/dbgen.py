#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module is used for generation of the recognition database associating
the fingerprint of an audio file with the id of the corresponding track
"""
import fingerprinter as fp
import m2r.dbtools as dbtools
import os

DB_FOLDER = "db/"
WAV_FOLDER = "wav/"

# %% Open Data base (creation if don't exist)
if not os.path.isfile(DB_FOLDER + "fingers.db"):
    sqldb = dbtools.Dbread(DB_FOLDER + "fingers.db")
    sqldb.request("""CREATE TABLE fingerprints
                (trackid text, title text, artist text,
                fingerprint text PRIMARY KEY)""")
    sqldb.commit()
else:
    # connect cree le fichier fingers.db s'il n'existe pas
    # c'est pourquoi il ne peut pas précéder la condition
    print("Database already exist")
    sqldb = dbtools.Dbread("fingers.db")

# %% research of informations and insert
metadata = dbtools.Dbtracks(DB_FOLDER + "track_metadata.db")


def traksearch(track="", artist=""):
    where = "WHERE 1"
    if track != "":
        where = where + " AND title LIKE '%" + track + "%'"
    if artist != "":
        where = where + " AND artist_name LIKE '%" + artist + "%'"
    return metadata.request("SELECT track_id, title, artist_name " +
                            "FROM songs """ + where)


def add(key, res):
    sqldb.request("INSERT INTO fingerprints VALUES(\"" +
                  res[0] + "\",\"" + res[1] + "\",\"" + res[2] + "\",\"" +
                  key + "\")")


def getfp(file):
    return fp.hashaudio(WAV_FOLDER + file)

# %% applications
no = []  # contains file with no match or more than one
print("Fingerprinting start")
print("File not found in database -------------------------")
for file in os.listdir(WAV_FOLDER):
    key = getfp(file)
    file2 = file.replace("'", "")
    file2 = file2.replace('"', '')
    if " - " in file2:
        art, song = file2.split(" - ", 1)
    elif " " in file2:
        art, song = file2.split(" ", 1)
    else:
        no.append(file)
        print(file)
        continue

    song = song.split(".", 2)[0]

    res = traksearch(song, art)
    if len(res) == 1:
        try:
            add(key, res[0])
        except:  # if same fingerprints for differents files
            print("Data insertion error ------------------------------------")
            print(file)
            print(sqldb.request("SELECT * FROM fingerprints " +
                                "WHERE fingerprint='"+key+"'"))
            break
    else:
        no.append(file)
        print(file)

if 0:
    # %% manual doing for not founded files
    print(len(no))
    file = no[11]; print(file)
    # key = getfp(file)
    art = "Weather"
    song = "Hold On"
    traksearch(song, art)

    # If duplicates in msong database
    metadata.request("DELETE FROM songs WHERE track_id='TRTIFGB128F93107E3'")


    # If correction of the name
    new_name = WAV_FOLDER + art + " - " + song + ".mp3.wav"
    # rename (on linux)
    os.system("mv '" + WAV_FOLDER + file + "' '" + new_name + "'")
    # or input directly in database
    # add(key, traksearch(song, art)[0])

    # %% close db & commmit results
    sqldb.request("SELECT count(*) FROM fingerprints")

metadata.close()
sqldb.commit()
sqldb.close()
