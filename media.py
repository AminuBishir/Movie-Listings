# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 09:30:49 2019

@author: Sadarwa
"""
import webbrowser
import random

class Movie:
    """This is a movie class """
    def __init__(self,movie_title,movie_story_line,movie_poster,movie_trailer):
        self.title = movie_title
        self.story_line = movie_story_line
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
        self.hit = random.randint(0,1000)
    def show_trailer(self):
        
        webbrowser.open(self.trailer)
    