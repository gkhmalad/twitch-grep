import requests
from bs4 import BeautifulSoup

url = "https://www.twitch.tv/trainwreckstv/clips?filter=clips&range=24hr"

def get_video_links():
    #Response Object
    r = requests.get(url)

    #BS object
    soup = BeautifulSoup(r.content, 'html5lib')

    #Find all links
    links = soup.findAll('a')

    #Filter the link ending with .mp43
    