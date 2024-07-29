import streamlit as st
from utils.database import add_song, get_songs

def app():
    st.title("Song of the Day")

    if 'authenticated' not in st.session_state or not st.session_state.authenticated:
        st.error("Please login to add a song.")
        return
    
    added = False
    today_songs = get_songs("day")
    for song in today_songs:
        if song['user_id'] == st.session_state.user_id:
            added = True

    st.header("Add a Song")
    title = st.text_input("Song Name")
    artist = st.text_input("Artist")
    youtube_link = st.text_input("Link (YouTube or other)")
    favorite_parts = st.text_input("Favorite Parts (optional)")
    lyrics = st.text_area("Lyrics (optional)")

    if st.button("Add Song"):
        if added:
            st.error("You already added a song today.")
        else:
            if title and artist and youtube_link:
                add_song(title, artist, youtube_link, favorite_parts, lyrics, st.session_state.user_id)
                st.success("Song added successfully.")
            else:
                st.error("Please fill in the required fields.")

    st.header("Songs of the Day")
    if not today_songs:
        st.write("No songs added today.")
    else:
        for song in today_songs:
            st.write("---")
            st.write(f"{song['title']} by {song['artist']} - [Link]({song['youtube_link']})")
            if song['favorite_parts']:
                st.write(f"**Favorite Parts:** {song['favorite_parts']}")
            if song['lyrics']:
                st.write(f"**Lyrics:** {song['lyrics']}")
            st.write(f"Song added by **{song["user_id"]}**")
