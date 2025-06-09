import requests

API_KEY = "517abc65"
OMDB_URL = "http://www.omdbapi.com/"

def fetch_movie_data(title):
    params = {"t": title, "apikey": API_KEY}
    response = requests.get(OMDB_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            return data
    return None