import streamlit as st
import requests

# Page config
st.set_page_config(page_title="🎬 CineInfo", layout="centered")

# OMDb API key
API_KEY = "517abc65"

# Title
st.title("🎬 CineInfo: Movie Insights (idk what to name it)")
st.subheader("Get instant details about any movie!")

# Input
movie_title = st.text_input("Enter a movie name")

# Fetch function
def fetch_movie_data(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
    response = requests.get(url)
    return response.json()

# Handle search
if movie_title:
    data = fetch_movie_data(movie_title)

    if data.get("Response") == "True":
        # Display Poster with safety check
        poster_url = data.get("Poster")
        if poster_url and poster_url != "N/A":
            st.image(poster_url, width=250)
        else:
            fallback_poster = "https://via.placeholder.com/250x370.png?text=No+Poster+Available"
            st.image(fallback_poster, width=250)

        # Display Details
        st.markdown("### 🎥 Title: " + data.get("Title", "N/A"))
        st.markdown("**Year:** " + data.get("Year", "N/A"))
        st.markdown("**Genre:** " + data.get("Genre", "N/A"))
        st.markdown("**Director:** " + data.get("Director", "N/A"))
        st.markdown("**Actors:** " + data.get("Actors", "N/A"))
        st.markdown("**Plot:** " + data.get("Plot", "N/A"))
        st.markdown("**IMDB Rating:** " + data.get("imdbRating", "N/A"))
        st.markdown("**Runtime:** " + data.get("Runtime", "N/A"))
        st.markdown("**Language:** " + data.get("Language", "N/A"))
        st.markdown("**Awards:** " + data.get("Awards", "N/A"))
    else:
        st.error("❌ Movie not found. Try a different title.")
