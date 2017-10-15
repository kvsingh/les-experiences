# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from utils import *
from wordcloud import WordCloud

def index(request):
    return render(request, 'lyrics/index.html')

    #return HttpResponse("Hello, world. You're at the lyrics index.")

def analysis(request):
    artist = request.GET['artist']
    client_access_token = "wP-X9-H4IzwidnKGW7-zqd6ARMlJpisjYSi-OQpVi_gEyfmKRNfDjJUjJs6f8ZCu"
    a = search(artist, client_access_token)

    songs = map(lambda t: t[2], a)
    urls = map(lambda t: t[3], a)
    print urls

    all_lyrics = ""
    for url in urls:
        lyrics = get_lyrics(url, client_access_token)
        all_lyrics += lyrics

    all_lyrics = clean_lyrics(all_lyrics)
    request.session['lyrics'] = all_lyrics

    return render(request, 'lyrics/analysis.html', {
        'artist': artist,
        'songs': songs,
        'lyrics': all_lyrics,
    })

def word_cloud(request):
    lyrics = request.session.get('lyrics')
    word_cloud = WordCloud(width=1000, height=500).generate(lyrics.lower())
    #word_cloud.to_file('wordclouds/' + artist + ".png")
    image = word_cloud.to_image()
    response = HttpResponse(image, content_type="image/png")
    #image.save(response, "PNG")
    return response
