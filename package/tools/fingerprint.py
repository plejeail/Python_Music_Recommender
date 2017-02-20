#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
    title  : untitled.py
    date   : dd/mm/yyyy
    author : Pierre Lejeail
    DOC_STRING
"""
# import librosa
import hashlib
# import numpy as np
import wave


def fingerprinter(audio_path, n=100000):
    """
        create the fingerprint of an audio file using the first 100 000 frames
        audio file must be at the 16-bits Wav format
    """
    wave_read = wave.open(audio_path, "r")
    # n > total number of frames -> n = number of frames
    if n > wave_read.getnframes():
        n = wave_read.getnframes()

    audio_hash = hashlib.sha256(wave_read.readframes(n)).hexdigest()
    wave_read.close()
    return audio_hash

if __name__ == '__main__':
    audio1 = '/home/gevisk/Programs/Python/Python_Music_Recommender/test.wav'
    audio2 = '/home/gevisk/Programs/Python/Python_Music_Recommender/test2.wav'

    fingerprinter(audio1)
    fingerprinter(audio2)
