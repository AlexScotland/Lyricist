import urllib.request, requests, sys, os
from requests.auth import HTTPBasicAuth
from urllib.parse import urlencode, quote_plus
import http.client as http_client4
from bs4 import BeautifulSoup
from html.parser import HTMLParser


hello = webSession()
### GET THE RAPPERS MAIYNNE
try:
    if os.stat("artist.txt").st_size == 0:
        hello.getArtists('https://en.wikipedia.org/wiki/List_of_hip_hop_musicians')
        hello.writeArtistsToFile()
    else:
        hello.getListFromFile()

except Exception as msg:
    if 'cannot find the file specified' in str(msg):
        hello.getArtists('https://en.wikipedia.org/wiki/List_of_hip_hop_musicians')
        hello.writeArtistsToFile()
finally:
    print(hello.artists)

#### LETS START SCRAPING, MAYN

for name in hello.artists:
   try:
        artist_url = hello.concatURL(name)
        song_list = hello.getSongList(artist_url)
        counter = 0
        for song in song_list:
            song_lyrics = hello.getLyrics(song)
            if song_lyrics == None:
                pass
            else:
                writeTextFile(song_lyrics, str(song_list[counter][0]))
                counter +=1
   except Exception as err:
       print('[ERR ]  Artist could not be parsed.')
       print(str(err))
   finally:
       pass
