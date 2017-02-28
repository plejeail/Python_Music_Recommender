#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main module :
    recognition + recommendation
"""

import recognizer
import clustering
import pandas as pnd

def recoreco(file):
    file_id = "TRAUYKN128F933067A"  # {'track_id': recognizer.get_track(file)["track_id"]}
    return clustering.recommendation(file_id)

audio = "/home/gevisk/Programs/Python/Python_Music_Recommender/package/wav/Gold Panda - Fifth Ave.mp3.wav"
print(recoreco(audio))
