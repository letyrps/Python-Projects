import requests
from bs4 import BeautifulSoup
import spotipy



date = input('What year you would like to travel to? Type in YYYY-MM-DD: ')

ENDPOINT_URL = 'https://www.billboard.com/charts/hot-100/'
url_date = f'{ENDPOINT_URL}{date}'

response = requests.get(url_date)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

titles = soup.find_all(name='h3', class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only", id="title-of-a-story")
list_songs = [title.getText() for title in titles]
ed_list_songs = []
for item in list_songs:
    result = item.replace('\t', '')
    result_2 = result.replace('\n', '')
    ed_list_songs.append(result_2)

print(ed_list_songs)

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id='c5760bee636f4468a578d134dbf334a5',
        client_secret='48be43acc27742f2b68735daf9b50614',
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]