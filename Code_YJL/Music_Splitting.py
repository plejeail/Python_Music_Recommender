# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 22:38:31 2017

@author: yjl20
"""
#importation de modules
import os
import shutil as sh
import random as rnd

directory_input = "genres/genres_converted/"
directory_output = "genres/genres_converted/test_files/"

genre_list = ["blues" , "classical","country","disco","hiphop","jazz","metal","pop","reggae","rock"]

size_file = []
numb_file = 0
for genre in genre_list :
    
   for files in os.listdir(directory_input + genre):
       numb_file = numb_file + 1
       #comptage du nombre de fichiers par dossiers
       
   size_file.append(numb_file)
   numb_file = 0

test_percentage = 0.1

size_test_file = round(test_percentage * sum(size_file)/len(genre_list))
#nombre de sons preleves par genres 
print(size_test_file)

def splitting_genres(directory_input , directory_output , genres , format_file):
    
    newpath = ((directory_output))
    os.makedirs(newpath)
    #creation d un nouveau dossier
    for genre in genre_list :
        the_dir = directory_input + genre
        all_files = filter(lambda x : x.endswith(format_file), os.listdir(the_dir))
        res = list(all_files)
        #recuperation d un ensemble de fichiers du mm genre
        for index in range(size_test_file):
            sound = rnd.choice(res)
            #choix aleatoires des fichers par genres
            sh.copy(src = the_dir + "/" + sound , dst = newpath + sound)
            
splitting_genres(directory_input = directory_input , directory_output = directory_output , genres = genre_list , format_file  = ".mp3")


 

    
