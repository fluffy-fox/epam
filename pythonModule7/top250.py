import requests
from bs4 import BeautifulSoup
import json, codecs
'''

Для прохождения теста добавил encoding="utf-8" к строке cls.mock_data = open("mockImdb.html")

'''
def parse_top_250(file_name: str):
    resp = requests.get("https://imdb.com/chart/top", headers={"Accept-Language": "En-us"})
    soup = BeautifulSoup(resp.text, 'lxml')
    crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    movies = [b.contents[0] for b in soup.select('td.titleColumn a')]
    year = [b.contents[0].replace('(', '').replace(')', '') for b in soup.select('td.titleColumn span')]
    position = [b.contents[0].replace('.', '').replace('\n', '').strip() for b in soup.select('td.titleColumn')]
    ratings = [b.contents[0] for b in soup.select('td.ratingColumn.imdbRating strong')]
    imdb = []
    with open(file_name, 'wb') as new_file:
        for index in range(0, len(movies)):
            director = crew[index].split(",")[0]
            crews_list = crew[index].split(",")[1:]
            crews = ','.join(crews_list)
            data = {movies[index]: {
                    "Position": position[index],
                    "Year": year[index],
                    "Director": director[:-7],
                    "Crew": crews.strip(),
                    "Rating": ratings[index]}}
            imdb.append(data)
        json.dump(imdb, codecs.getwriter('utf-8')(new_file), ensure_ascii=False)