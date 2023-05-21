import requests
from bs4 import BeautifulSoup
URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(URL)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

titles = soup.find_all(name='h3', class_='title')
list_titles = [title.getText() for title in titles]


for title in list_titles:
    with open('100_movies.txt', 'a') as file:
        file.write(f'{title}\n')


