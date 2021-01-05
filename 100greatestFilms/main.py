import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
data = response.text

soup = BeautifulSoup(data, 'html.parser')
titles = [title.get_text() for title in soup.findAll(name='h3', class_='title')]

titles = titles[::-1]

with open ('100_greatest_films.txt', 'a') as film_file:

     for title in titles:
         film_file.write(title + '\n')


