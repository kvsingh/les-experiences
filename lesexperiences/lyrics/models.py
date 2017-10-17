# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=200)
    #The following are the cleaned lyrics
    lyrics = models.CharField(max_length=10000)
    #artist_wordcloud = models.ImageField(upload_to='wordclouds')

#Store each song's uncleaned lyrics
class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    lyrics = models.CharField(max_length=10000)