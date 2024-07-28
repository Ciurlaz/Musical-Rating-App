import streamlit as st
from utils.database import get_ratings

def app():
    st.title("Songs Leaderboard")

    st.header("Song of the Day")
    songs_day = get_ratings("song", "day")
    for song in songs_day:
        st.write(f"{song['title']} by {song['artist']} - Average Rating: {song['avg_rating']:.2f}")

    st.header("Song of the Week")
    songs_week = get_ratings("song", "week")
    for song in songs_week:
        st.write(f"{song['title']} by {song['artist']} - Average Rating: {song['avg_rating']:.2f}")

    st.header("All-time Songs")
    songs_all_time = get_ratings("song", "all-time")
    for song in songs_all_time:
        st.write(f"{song['title']} by {song['artist']} - Average Rating: {song['avg_rating']:.2f}")
