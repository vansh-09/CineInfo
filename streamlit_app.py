import streamlit as st
import requests
from util import fetch_movie_data

st.set_page_config(page_title="🎬 CineInfo", layout="centered")

st.title("🎬 CineInfo: Movie Insights Provider (idk what else to name it)")

movie_title = st.text_input("Enter a movie name")

if movie_title:
    data = fetch_movie_data(movie_title)
    
    if data:
        st.subheader(data.get("Title", "Unknown Title"))
        st.image(data.get("Poster"), width=200)
        st.markdown(f"**Year:** {data.get('Year')}")
        st.markdown(f"**Genre:** {data.get('Genre')}")
        st.markdown(f"**Director:** {data.get('Director')}")
        st.markdown(f"**Actors:** {data.get('Actors')}")
        st.markdown(f"**Plot:** {data.get('Plot')}")
        st.markdown(f"**IMDb Rating:** {data.get('imdbRating')}")
    else:
        st.error("Movie not found. Try a different title.")
