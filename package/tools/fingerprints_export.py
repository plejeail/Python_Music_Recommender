

#modules importation
from fingerprint import fingerprinter
import os
import pandas as pd
#directory where the audios are
path_audios = 'genres/genres_converted/test_files'

def fingerprints_exports(path_files):
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
    dataframe_fingerprints.to_csv('audios_fingerprints.csv' , sep = ';')

    #functions calls
fingerprints_audios = fingerprints_exports(path_audios)
storage_fingerprints(fingerprints_audios)
