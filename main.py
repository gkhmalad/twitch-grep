import requests
from bs4 import BeautifulSoup

url = "https://www.twitch.tv/trainwreckstv/clips?filter=clips&range=24hr"

def get_video_links():
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    links = soup.findAll('a')