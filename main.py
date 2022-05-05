import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

empire_web_page = response.text
soup = BeautifulSoup(empire_web_page, "html.parser")

all_movie_titles = soup.find_all(name="h3", class_="title")
movie_names = [movie.getText() for movie in all_movie_titles]
# print(movie_names[::-1]) will also reverse the list.
movie_names.reverse()

with open("movies.txt", "w") as movies:
    for each_film in movie_names:
        movies.write(f"{each_film}\n")
