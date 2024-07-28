import streamlit as st
from utils.database import get_ratings

def app():
    st.title("Albums Leaderboard")

    st.header("Album of the Day")
    albums_day = get_ratings("album", "day")
    for album in albums_day:
        st.write(f"{album['title']} by {album['artist']} - Average Rating: {album['avg_rating']:.2f}")

    st.header("Album of the Week")
    albums_week = get_ratings("album", "week")
    for album in albums_week:
        st.write(f"{album['title']} by {album['artist']} - Average Rating: {album['avg_rating']:.2f}")

    st.header("All-time Albums")
    albums_all_time = get_ratings("album", "all-time")
    for album in albums_all_time:
        st.write(f"{album['title']} by {album['artist']} - Average Rating: {album['avg_rating']:.2f}")
