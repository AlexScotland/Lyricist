class webSession:
    def __init__(self):
        self.session = requests.Session()
        self.artists = []
        self.proxies = {
        "https":"93.125.121.98:8081",
        "http":"167.71.176.202:8080",
            }

    def getArtists(self,url):
        page = self.session.get(url, proxies = self.proxies)
        self.scraper = BeautifulSoup(page.content,'html.parser')
        for i in self.scraper.find_all('div',{'class':'div-col columns column-width'}):
            list_descendants = i.descendants
            for artist in list_descendants:
                if artist.name == 'a':
                    if artist.text == '[1]':
                        pass
                    elif artist.text == '[2]':
                        pass
                    else:
                        self.artists.append(artist.text)

    def writeArtistsToFile(self):
        with open("artist.txt", "w") as txtFile:
            for i in self.artists:
                try:
                    txtFile.write(i+'\n')
                except:
                    print('Error importing')
                finally:
                    pass
            txtFile.close()

    def stripTags(html):
        s = htmlStripper()
        s.feed(html)
        return s.get_data()

    def concatURL(self,artist_name):
        if not artist_name[0].isalpha():
            artist_name=artist_name.lower()
            first_letter = '19'
        else:
            artist_name=artist_name.lower()
            first_letter = artist_name[0]
        url = "http://www.azlyrics.com/"+first_letter+"/"+artist_name.replace(" ", "")+".html"
        return url

    def getListFromFile(self):
        with open("artist.txt", "r") as txtFile:
            for i in txtFile:
                try:
                    i= i.replace('\n','')
                    i = i.replace('/','')
                    i= i.replace(':','')
                    self.artists.append(i)
                except:
                    print('Error importing')
                finally:
                    pass
            txtFile.close()


    def getSongList(self,url):
        song_list = []
        page = self.session.get(url, proxies = self.proxies)
        soup = BeautifulSoup(page,"html.parser")
        for song in soup.find_all('div',{'id':'listAlbum'}):
            for link in song.find_all('a'):
                song_link=link.get('href')
                song_name=link.get_text()
                song_link=SongLink[3:]
                generated_link='http://www.azlyrics.com/'+song_link
                song_list.append((song_name,generated_link))
        return song_list

    def getLyrics(self,song_url):
        try:
            page=self.session.get(song[1], proxies = self.proxies)
        except Exception as msg:
            print("[ERR ] Cannot Navigate to link:  "+str(msg))
            print("[Cont] Skipping Song.")
        else:
            soup=BeautifulSoup(page,'lxml')
            soup=soup.find_all('div', class_="")
            text=soup[1]
            text=str(text)
            text=stripTags(text)
            text=text.replace("<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->","")
            return text
