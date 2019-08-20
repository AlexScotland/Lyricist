import urllib.request, requests, sys, os
from requests.auth import HTTPBasicAuth
from urllib.parse import urlencode, quote_plus
import http.client as http_client4
from bs4 import BeautifulSoup
from html.parser import HTMLParser


class htmlStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)

def removeHTML(innerHTML):
    started=False
    for i in innerHTML:
        if i == '<':
            started=True
            temp_string = ''
        if started:
            temp_string+= i
        if i == '>':
            started=False
            innerHTML=innerHTML.replace(temp_string,'')
    return innerHTML

def writeTextFile(songText, songName):
    with open("dataset.txt", "a") as txtFile:
        txtFile.write(songName)
        txtFile.write(songText)
        txtFile.close()
