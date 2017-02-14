# -*- coding: utf-8 -*-
# Music Recommender
# tools.sampler
""" this module contains tool functions for statistics """

#importation de modules
from os import makedirs, listdir
import shutil as sh
import random as rnd


def sampler(dir_in , dir_out , genres , format_file, size_test_file):
    """ sampler choose a given number of files randomly """ 
    newpath = ((dir_out))
    makedirs(newpath)
    #creation d un nouveau dossier
    for genre in genre_list :
        the_dir = dir_in + genre
        files = filter(lambda x : x.endswith(format_file), listdir(the_dir))
        res = list(files)
        #recuperation d un ensemble de fichiers du mm genre
        for index in range(size_test_file):
            sound = rnd.choice(res)
            #choix aleatoires des fichers par genres
            sh.copy(src = the_dir + "/" + sound , dst = newpath + sound)

            
if __name__ == "__main__":
    directory_input = "genres/genres_converted/"
    directory_output = "genres/genres_converted/test_files/"
    size_file = []
    genre_list = ["blues", "classical", "country", "disco", "hiphop", "jazz",
              "metal", "pop", "reggae", "rock"]

    # comptage du nombre de fichiers
    numb_file = 0
    for genre in genre_list :
       for files in listdir(directory_input + genre):
           numb_file = numb_file + 1
       size_file.append(numb_file)
       numb_file = 0
    
    test_percentage = 0.1
    
    size_test_file = round(test_percentage * sum(size_file)/len(genre_list))
    
    #nombre de sons preleves par genres
    print(size_test_file)

    sampler(directory_input = directory_input,
                     directory_output = directory_output,
                     genres = genre_list,
                     format_file  = ".wav")
