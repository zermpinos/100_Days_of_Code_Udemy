import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the titles and store them in a list.
movie_titles = []
for title in soup.find_all('h3', class_='title'):
    movie_titles.append(title.text.strip())

# Since the movie titles list may contain extra elements, you need to filter out the top 100 movie titles.
top_100_movies = movie_titles[:100]
top_100_movies.reverse()

# Create a text file called movies.txt and write the top 100 movie titles in ascending order.
with open('movies.txt', 'w', encoding='utf-8') as file:
    for i, movie in enumerate(top_100_movies, 1):
        file.write(f'{movie}\n')
