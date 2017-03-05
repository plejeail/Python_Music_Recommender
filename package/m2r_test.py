#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
M2R test : recognition and recommendation,
This module test the program with a randomly selected music
"""
# %% Import and initialization
import recognizer
import fingerprint as fp
import clustering
from random import randint
import os, webbrowser


WAV_FOLDER = "./wav/"


def stripb(string):
    return string[2:-1]


def browse_yt(file):
    search = stripb(file[3]).split(" ")
    search.extend(stripb(file[2]).split(" "))
    return "+".join(search)


# %% Randomly select a file
index = randint(0, 29)
musics = [file for file in os.listdir(WAV_FOLDER)]
audio = musics[index]


# %% Recognition
print(audio + "------------------------------", end="\n\n")
# fingerprint (useless, only for demo purpose)
print("Fingerprint: " + fp.hashaudio(WAV_FOLDER + audio))
print("---")
# recognition
recognition = recognizer.get_track(WAV_FOLDER + audio)
print("Id track: " + recognition["track_id"])
print("  Titre : " + recognition["title"])
print("Artiste : " + recognition["artist"], end="\n\n")


# %% recommendation
print("Recommendation")
recos = clustering.recommendation(recognition["track_id"])
print("recommendation 1: " + stripb(recos[0][3]) + " - " + stripb(recos[0][2]))
print("recommendation 2: " + stripb(recos[1][3]) + " - " + stripb(recos[1][2]))
print("recommendation 3: " + stripb(recos[2][3]) + " - " + stripb(recos[2][2]))

# %% ecoute

# Listening to original
search = recognition["artist"].split(" ")
search.extend(recognition["title"].split(" "))
webbrowser.open("https://www.youtube.com/results?search_query=" +
                "+".join(search))

# %% Reco 1
webbrowser.open("https://www.youtube.com/results?search_query=" +
                browse_yt(recos[0]))
# %% Reco 2
webbrowser.open("https://www.youtube.com/results?search_query=" +
                browse_yt(recos[1]))
# %% Reco 3
webbrowser.open("https://www.youtube.com/results?search_query=" +
                browse_yt(recos[2]))
