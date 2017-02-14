# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:02:59 2017

@author: yjl20
"""
#importation des modules
import os
from pydub import AudioSegment

######MUSIC CONVERSION###############################

# tous les genres disponibles
genre_list = ["blues","classical" , "country","disco","hiphop","jazz","metal","pop","reggae","rock"]



def convert_format(directory_input , directory_output , genres , format_file):
    for genre in genres: 
        #parcours de la liste des genres
       newpath = ((directory_output + genre)) 
       #definition du nouveau chamin
       os.makedirs(newpath)
       
       for file in os.listdir(directory_input + genre):
          sound_file =  AudioSegment.from_file(directory_input + genre + "/" + file)
          temp_file = file.split(".")
          new_name_file = temp_file[0] + "." + temp_file[1]
          #reecriture des noms des sons
          new_sound_file =  sound_file.export(newpath + "/" + new_name_file + ".mp3", format=format_file)
          #stockage des sons dans le nouveau directory
           

directory_input = "genres/genres_raw/"
genres = genre_list

directory_output = "genres/genres_converted/"
convert_format(directory_input = directory_input , directory_output = directory_output , genres = genre_list , format_file = "mp3")

