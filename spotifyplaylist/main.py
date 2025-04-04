from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("enter the date in the format of YYYY-MM-DD")
url = 'https://www.billboard.com/charts/hot-100/'
url = url + date
response = requests.get(url=url)
website = response.text
soup = BeautifulSoup(website, 'html.parser')

''' songslist = soup.find_all(name='h3',id="title-of-a-story")
    with id="title-of-a-story in h3 there are around 400 + items are there instead use select function
'''

songslist = soup.select("li ul li h3")
list = []
for song in songslist:
    list.append(song.get_text(strip=True))
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='',
                                               client_secret='',
                                               redirect_uri='http://example.com', ))
