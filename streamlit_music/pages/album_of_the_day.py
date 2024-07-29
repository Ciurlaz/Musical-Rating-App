# pages/album_of_the_day.py
import streamlit as st
from utils.database import record_vote

def app():
    st.title("Vote for Album of the Day")

    album_name = st.text_input("Enter the album name:")
    if st.button("Vote"):
        if album_name:
            record_vote('album', album_name)
            st.success("Thank you for your vote!")
        else:
            st.error("Please enter an album name.")
