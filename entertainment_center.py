'''
import media.py containing class Movie and
import fresh_tomatoes containing the website format
import requests and json for using an API
'''
import media
import fresh_tomatoes
import requests
import json

# API and JSON handling
url = "https://api.themoviedb.org/3/movie/popular?api_key=d9816f29499efbdb064\
c8c9834350411&language=en-US"
payload = "{}"
response = requests.request("GET", url, data=payload)
response = response.json()
response = json.dumps(response)
parsed_data = json.loads(response)

# lists to store required data
movies_id = []
movies_title = []
movies_trailer = []
movies_poster = []
movies = []

# retrieve data from dataset provided by API
for i in range(0, 20):
    id = parsed_data['results'][i]['id']
    movies_id.append(id)
    title = parsed_data['results'][i]['title']
    movies_title.append(title)

# Configuration URL required for retrieval of Images
# (done using base_url and poster_size)
config_url = "https://api.themoviedb.org/3/configuration?api_key=d9816f2949\
9efbdb064c8c9834350411"
config_response = requests.request("GET", config_url)
config_response = config_response.json()
base_url = config_response['images']['base_url']
poster_size = config_response['images']['poster_sizes']
poster_size = poster_size.pop()

# collect all required data from database provided
for i in movies_id:
    video_url = "https://api.themoviedb.org/3/movie/" + str(i) + \
                "/videos?api_key=d9816f29499efbdb064c8c9834350411&language\
                =en-US"
    video_response = requests.request("GET", video_url)
    video_response = video_response.json()
    video_response = json.dumps(video_response)
    parsed_video = json.loads(video_response)
    # use the first video
    video_key = parsed_video['results'][0]['key']
    movies_trailer.append("https://www.youtube.com/watch?v="+video_key)

    poster_url = "https://api.themoviedb.org/3/movie/" + str(i) + \
                 "/images?api_key=d9816f29499efbdb064c8c9834350411"
    poster_response = requests.request("GET", poster_url)
    poster_response = poster_response.json()
    poster_response = json.dumps(poster_response)
    parsed_poster = json.loads(poster_response)
    # use the first trailer
    poster_path = parsed_poster['posters'][0]['file_path']
    movies_poster.append(base_url+poster_size+poster_path)

# create instance of favorite movies
for i in range(0, 20):
    movie = media.Movie(movies_title[i], movies_poster[i], movies_trailer[i])
    movies.append(movie)

# use fresh_tomatoes function for rendering webpage
fresh_tomatoes.open_movies_page(movies)
