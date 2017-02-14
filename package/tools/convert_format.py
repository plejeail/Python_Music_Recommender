# -*- coding: utf-8 -*-
# Music Recommender
# tools.convert_format

# importation des modules
from os import listdir, makedirs
from pydub import AudioSegment

######MUSIC CONVERSION###############################

# tous les genres disponibles
genre_list = ["blues", "classical", "country", "disco", "hiphop", "jazz",
              "metal", "pop", "reggae", "rock"]


def convert_format(dir_in,
                   dir_out,
                   location,
                   format_file):
    for folder in location: 
       #parcours de la liste des genres
       new_path = ((dir_out + location)) 
       #definition du nouveau chamin
       makedirs(new_path)
       
       for file in listdir(dir_in + location):
          # Recupere contenu fichier audio
          sound_file =  AudioSegment.from_file(dir_in + location + "/" + file)
          temp_file = file.split(".")
          name = temp_file[0] + "." + temp_file[1]
          # stockage des sons dans le nouveau directory
          sound_file.export(new_path + "/" + name + ".wav", format=format_file)


directory_input = "genres/genres_raw/"
genres = genre_list

directory_output = "genres/genres_converted/"
convert_format(directory_input = directory_input,
               directory_output = directory_output,
               repositories = genre_list,
               format_file = "wav")
