# pages/song_of_the_day.py
import streamlit as st
from utils.database import record_vote

def app():
    st.title("Vote for Song of the Day")

    song_name = st.text_input("Enter the song name:")
    if st.button("Vote"):
        if song_name:
            record_vote('song', song_name)
            st.success("Thank you for your vote!")
        else:
            st.error("Please enter a song name.")
