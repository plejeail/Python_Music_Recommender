#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module generate the fingerprint of an audio file
"""
import hashlib
import wave


def hashaudio(audio_path):
    """
        create the fingerprint of an audio file using the frames of an
        audio file and the audio and the number of channels
        the audio must be at the 16-bits Wav format
        We do a double hash in order to avoid same hash for differents files
    """
    wave_read = wave.open(audio_path, "r")
    # n > total number of frames -> n = number of frames
    n = wave_read.getnframes()
    chans = wave_read.getnchannels()
    n1 = int(n/2)
    n2 = n - n1
    hash1 = hashlib.sha256(wave_read.readframes(n1)).hexdigest()
    wave_read.setpos(n1+1)
    hash2 = hashlib.sha256(wave_read.readframes(n2)).hexdigest()
    wave_read.close()
    return str(n) + str(chans) + hash1 + hash2
