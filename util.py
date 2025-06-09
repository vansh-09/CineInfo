import requests

def fetch_movie_data(movie_name):
    api_key = "517abc65"  # Already noted
    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={api_key}"

    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True":
        return data
    else:
        return None
