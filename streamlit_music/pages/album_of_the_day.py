import streamlit as st
from utils.database import add_album, get_albums

def app():
    st.title("Album of the Day")

    if 'authenticated' not in st.session_state or not st.session_state.authenticated:
        st.error("Please login to add an album.")
        return

    st.header("Add an Album")
    title = st.text_input("Album Name")
    artist = st.text_input("Artist")
    link = st.text_input("Link (YouTube or other)")
    favorite_song = st.text_input("Favorite Song (optional)")
    songs_list = st.text_area("Songs List (optional)")

    if st.button("Add Album"):
        if title and artist and link:
            add_album(title, artist, link, favorite_song, songs_list, st.session_state.user_id)
            st.success("Album added successfully.")
        else:
            st.error("Please fill in the required fields.")

    st.header("Albums of the Day")
    today_albums = get_albums("day")
    if not today_albums:
        st.write("No albums added today.")
    else:
        for album in today_albums:
            st.write(f"{album['title']} by {album['artist']} - [Link]({album['link']})")
            if album['favorite_song']:
                st.write(f"**Favorite Song:** {album['favorite_song']}")
            if album['songs_list']:
                st.write(f"**Songs List:** {album['songs_list']}")
