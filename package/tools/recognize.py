# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 14:18:44 2017

@author: yjl20
"""

#modules importation
from fingerprints import fingerprinter
import pandas as pd 
import os
import random as rnd

#fingerprints stored in a csv file importation
fingerprints_audios = pd.read_csv('audios_fingerprints.csv' , sep = ';' , header = 0)

#importation of the all testing files
def import_audios(path_files):
    list_audios = []
    for file in os.listdir(path_files):
        audio = path_files + "/" + file
        list_audios.append(audio)
    return list_audios

#camparison of the fingerprints
def comparison_audios(audios , numbcomaprison , file_fingerprints , name_column = 'fingerprints'):
    number_audios = len(audios)
    
    #randomly choose file to compare
    indexes = [rnd.randint(0,number_audios) for k in range(numbcomaprison)]
    list_output = []
    for index in indexes:
        choosen_audio = audios[index]
        for fingerprint in file_fingerprints[name_column]:
            if fingerprinter(choosen_audio) == fingerprint:
                temp_file = choosen_audio.split("/")
                list_output.extend([[temp_file[3] , fingerprinter(choosen_audio) , fingerprint]])
    #storage as dataframe for a better view
    comparison = pd.DataFrame(list_output)  
    comparison.columns = ['name_audio' , 'fingerprint_genereated' , 'fingerprint_stored_file']          
    print(comparison)
        


path_audios = 'genres/genres_converted/test_files'

list_audios = import_audios(path_audios)
exp = comparison_audios(list_audios , 5 , fingerprints_audios)


    
    


