# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from utils import *
from wordcloud import WordCloud
from django.templatetags.static import static
from lesexperiences.settings import MEDIA_ROOT
from lyrics.models import Artist, Song

def index(request):
    return render(request, 'lyrics/index.html')

    #return HttpResponse("Hello, world. You're at the lyrics index.")

def on_song(song, client_access_token, artist):
    song_name = song[2]
    url = song[3]
    lyrics = get_lyrics(url, client_access_token)
    this_song = Song(name=song_name, lyrics=lyrics, artist=artist)
    this_song.save()
    return lyrics, this_song

def analysis(request):
    artist = request.GET['artist']
    client_access_token = "wP-X9-H4IzwidnKGW7-zqd6ARMlJpisjYSi-OQpVi_gEyfmKRNfDjJUjJs6f8ZCu"

    #Check if artist is already there in db
    try:
        this_artist = Artist.objects.get(name=artist)
        all_lyrics = this_artist.lyrics
    except:
        this_artist = Artist(name=artist)
        this_artist.save()

        a = search(artist, client_access_token)
        all_lyrics = ""
        for song in a:
            lyrics, this_song = on_song(song, client_access_token, this_artist)
            all_lyrics += lyrics
            this_artist.song_set.add(this_song)

        all_lyrics = clean_lyrics(all_lyrics)
        request.session['lyrics'] = all_lyrics
        this_artist.lyrics = all_lyrics
        #word_cloud = WordCloud(width=1000, height=500).generate(all_lyrics.lower())
        #image = word_cloud.to_image()
#        this_artist.artist_wordcloud = image
        this_artist.save()

        print "here"
        #image.save(MEDIA_ROOT + "/wordclouds/" + artist + ".png")


    #img_location = STATIC_ROOT + '/wordclouds/' + artist + ".png"
    #img_location = static('wordclouds/' + artist + ".png")

    #print img_location
    #word_cloud.to_file(img_location)

    return render(request, 'lyrics/analysis.html', {
        'artist': artist,
        #'songs': songs,
        'lyrics': all_lyrics,
    })

#def word_cloud(request):
 #   lyrics = request.session.get('lyrics')
    #image = word_cloud.to_image()
    #response = HttpResponse(image, content_type="image/png")
    #image.save(response, "PNG")
    #return response
