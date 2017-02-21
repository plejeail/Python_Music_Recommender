#modules importation
from fingerprint import fingerprinter
import os
import pandas as pd


def fingerprints_exports(path_files):
    """
        Create dataframe_fingerprints which contains the fingerprint of all the audio files in the given path
    """
    list_fingerprints = []

    for files in os.listdir(path_files):
        audio = path_files + "/" + files
        #storage of the audios files as 'audio.wav'
        list_fingerprints.append(fingerprinter(audio))
        
        #sotrage as a dataframe (to ease the exportation)
    dataframe_fingerprints = pd.DataFrame(list_fingerprints)
    dataframe_fingerprints.columns = ['fingerprints']
    return dataframe_fingerprints
    


def storage_fingerprints(dataframe_fingerprints):
    """
        write a dataframe to csv 
    """
    dataframe_fingerprints.to_csv('audios_fingerprints.csv' , sep = ';')

    
if __name__ == "__main__":
    # path of the audio files directory 
    audiopath = 'genres/genres_converted/test_files'
    fingerprints_audios = fingerprints_exports(path_audios)
    storage_fingerprints(fingerprints_audios)
