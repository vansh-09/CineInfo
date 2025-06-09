import streamlit as st
import requests

st.set_page_config(page_title="CineInfo", page_icon="🎬", layout="centered")

st.title("🎬 CineInfo: Movie Insights (idk what to name it)")
st.markdown("Enter a movie name to get details instantly!")

#API Request 
def fetch_movie_data(movie_name):
    api_key = "517abc65"
    exact_url = f"http://www.omdbapi.com/?t={movie_name}&apikey={api_key}"
    search_url = f"http://www.omdbapi.com/?s={movie_name}&apikey={api_key}"

    exact_response = requests.get(exact_url).json()

    if exact_response.get("Response") == "True":
        return exact_response
    else:
        search_response = requests.get(search_url).json()
        if search_response.get("Response") == "True":
            first_title = search_response["Search"][0]["Title"]
            fallback_url = f"http://www.omdbapi.com/?t={first_title}&apikey={api_key}"
            fallback_response = requests.get(fallback_url).json()
            return fallback_response
        else:
            return None

#Input 
movie_name = st.text_input("Enter a movie name")

#Fetch & Display
if movie_name:
    data = fetch_movie_data(movie_name.strip())

    if data:
        st.subheader(data.get("Title", "N/A"))
        st.image(data.get("Poster"), width=250)
        st.markdown(f"**Genre:** {data.get('Genre', 'N/A')}")
        st.markdown(f"**Released:** {data.get('Released', 'N/A')}")
        st.markdown(f"**Director:** {data.get('Director', 'N/A')}")
        st.markdown(f"**Plot:** {data.get('Plot', 'N/A')}")
        st.markdown(f"**IMDB Rating:** {data.get('imdbRating', 'N/A')}")
    else:
        st.error("❌ Movie not found. Try a different title.")
