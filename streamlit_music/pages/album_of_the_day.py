import streamlit as st
from utils.database import add_album, get_albums

def app():
    st.title("Album of the Day")

    if 'authenticated' not in st.session_state or not st.session_state.authenticated:
        st.error("Please login to add an album.")
        return
    
    added = False
    today_albums = get_albums("day")
    for album in today_albums:
        if album['user_id'] == st.session_state.user_id:
            added = True
    
    st.header("Add an Album")
    title = st.text_input("Album Name")
    artist = st.text_input("Artist")
    link = st.text_input("Link (YouTube or other)")
    favorite_song = st.text_input("Favorite Song (optional)")
    songs_list = st.text_area("Songs List (optional)")

    already = False
    all_time_albums = get_albums("all-time")
    for album in all_time_albums:
        if album["title"] == title and album["artist"] == artist:
            already = True

    if st.button("Add Album"):
        if added:
            st.error("You already added an album today.")
        else:
            if already:
                st.error("An album with the same name and artist already exists.")
            else:
                if title and artist and link:
                    add_album(title, artist, link, favorite_song, songs_list, st.session_state.user_id)
                    st.success("Album added successfully.")
                else:
                    st.error("Please fill in the required fields.")

    st.header("Albums of the Day")
    if not today_albums:
        st.write("No albums added today.")
    else:
        for album in today_albums:
            st.write("---")
            st.write(f"{album['title']} by {album['artist']} - [Link]({album['link']})")
            if album['favorite_song']:
                st.write(f"**Favorite Song:** {album['favorite_song']}")
            if album['songs_list']:
                st.write(f"**Songs List:** {album['songs_list']}")
            st.write(f"Album added by: **{album['user_id']}**")

            st.write(f"Rate the album: **{album['title']}**")
            rating = st.slider(
                "Select a rating",
                key=album['id'],
                min_value=0.0,
                max_value=10.0,
                step=0.1
            )

            st.write(f"Selected rating: {rating:.1f}")

            if st.button("Submit Rating", key=album['id']):
                # Qui dovresti aggiungere la logica per gestire l'invio della valutazione
                st.write(f"Rating of {rating:.1f} submitted for {album['title']}!")
            
