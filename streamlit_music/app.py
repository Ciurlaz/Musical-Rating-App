import streamlit as st
from multiapp import MultiApp
from pages import home, song_of_the_day, album_of_the_day, leaderboard_songs, leaderboard_albums, login, signup
from utils.database import init_db

# Inizializzazione del database
init_db()

app = MultiApp()

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    login_option = st.sidebar.radio("Login or Sign Up", ("Login", "Sign Up"))
    if login_option == "Login":
        if login.app():
            st.session_state.authenticated = True
            st.experimental_rerun()
    else:
        signup.app()
else:
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.experimental_rerun()

    st.sidebar.title("Music Rating App")
    app.add_app("Home", home.app)
    app.add_app("Song of the Day", song_of_the_day.app)
    app.add_app("Album of the Day", album_of_the_day.app)
    app.add_app("Songs Leaderboard", leaderboard_songs.app)
    app.add_app("Albums Leaderboard", leaderboard_albums.app)

    app.run()
