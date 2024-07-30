import streamlit as st
from utils.database import get_ratings

def app():
    st.title("Songs Leaderboard")

    st.header("Song of the Day")
    songs_day = get_ratings("song", "day")
    st.table(songs_day)

    st.header("Song of the Week")
    songs_week = get_ratings("song", "week")
    st.table(songs_week)

    st.header("All-time Songs")
    songs_all_time = get_ratings("song", "all-time")
    st.table(songs_all_time)