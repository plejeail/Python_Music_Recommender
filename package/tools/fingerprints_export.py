

#modules importation
from fingerprints import fingerprinter
import os
import pandas as pd
#directory where the audios are
path_audios = 'genres/genres_converted/test_files'

def fingerprints_exports(path_files):
    list_fingerprints = []
   # dataframe_fingerprints = pd.DataFrame()
    for files in os.listdir(path_files):
        audio = path_files + "/" + files
        list_fingerprints.append(fingerprinter(audio))
        
        
    dataframe_fingerprints = pd.DataFrame(list_fingerprints)
    dataframe_fingerprints.columns = ['fingerprints']
    
    return dataframe_fingerprints
    


def storage_fingerprints(dataframe_fingerprints):
    dataframe_fingerprints.to_csv('audios_fingerprints.csv' , sep = ';')

fingerprints_audios = fingerprints_exports(path_audios)
storage_fingerprints(fingerprints_audios)