import streamlit as st
from utils.database import get_ratings

def app():
    st.title("Albums Leaderboard")

    st.header("Album of the Day")
    albums_day = get_ratings("album", "day")
    st.table(albums_day)

    st.header("Album of the Week")
    albums_week = get_ratings("album", "week")
    st.table(albums_week)

    st.header("All-time Albums")
    albums_all_time = get_ratings("album", "all-time")
    st.table(albums_all_time)