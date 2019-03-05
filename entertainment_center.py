# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 09:36:24 2019

@author: Sadarwa
"""

import media
import fresh_tomatoes


toy_story = media.Movie("Toy Story","This moview si about a toy story","https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://youtu.be/qoqG7Px6cOQ")
#print(toy_story.title)
java_pride = media.Movie("Java Trailer","A movie made for the Java devs",r"file://D:\AMINU BISHIR\AMINU BISHIR\SADARWA\Java.jpg",
                         "https://youtu.be/b-Cr0EWwaTk")

vikings = media.Movie("The Vikins","A movie about the story of the Vikins",r"image/vikings.png",
                         "https://youtu.be/8dGCvJkzQSE")

got = media.Movie("Game of Thrones","Story of the kings aspiring to rule the world!",r"image/got.jpeg",
                         "https://youtu.be/3-fiwBPyAa4")

merlin = media.Movie("Merlin","A story of a boy and a sorcera",r"image/merlin.jpg",
                         "https://youtu.be/UMiki1g5o0E")

gwaska = media.Movie("Gwaska","An award winning Kannywood movie starring Adam A Zango",r"image/gwaska.jpg",
                         "https://youtu.be/G3pVolmn-wI")

arashi = media.Movie("Arashi","Arashi song",r"image/arashi.jpg",
                         "https://youtu.be/_yEHhYLPEeQ")


print(java_pride.title)
#webbrowser.open("https://youtu.be/3UsKYsLSGpU")
#java_pride.show_trailer()
movies = {toy_story,java_pride,got,vikings,merlin,gwaska,arashi}
#fresh_tomatoes.create_movie_tiles_content(movies)
#fresh_tomatoes.open_movies_page(movies)
print(arashi.__doc__)
print(arashi.__module__)
#print(arashi.__name__)
