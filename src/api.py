# Welccome To project Api Bot
# In this file, we send a request to the site with 
# the ID or name of the movie to get the movie information.




# imports
import requests


def get_info_movie_byid(movie_id):
    url = f"http://moviesapi.ir/api/v1/movies/{movie_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return "Error"
    else:
        response = response.json()
        title = response['title']
        country = response['country']
        year = response['year']
        imdb_rating = response['imdb_rating']
        return title, country, year, imdb_rating


def get_info_movie_moviename(movie_name):
    url = f"http://moviesapi.ir/api/v1/movies"
    parameters = {
        'q' : movie_name
    }
    response = requests.get(url, params=parameters)
    if response.status_code != 200:
        return "Error"
    response = response.json()
    result = response.get('data', [])
    if not result:
        return "Error"
    else:
        movie_info = result[0]
        title = movie_info['title']
        country = movie_info['country']
        year = movie_info['year']
        imdb_rating = movie_info['imdb_rating']
        return title, country, year, imdb_rating
    



if __name__ == "__main__":
    result = get_info_movie_moviename("batman")
    if result == "Error":
        print("Error")
    else:
        t, c, y, i = result
        print(t)
        print(c)
        print(y)
        print(i)
