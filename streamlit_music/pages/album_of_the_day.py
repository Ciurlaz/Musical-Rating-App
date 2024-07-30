import streamlit as st
from utils.database import add_album, get_albums, add_rating, get_ratings

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
    link = st.text_input("Link (optional)")
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

    daily_ratings = get_ratings("album", "day")
    st.header("Album of the Day")
    if not today_albums:
        st.write("No album added today.")
    else:
        for album in today_albums:
            st.write("---")
            st.write(f"**{album['title']}** by {album['artist']}")
            if album['link']:
                st.write(f"[Link]({album['link']})")
            if album['favorite_song']:
                st.write("**Favorite song:**")
                st.write(f"{album['favorite_song']}")
            if album['songs_list']:
                st.write("**List of songs:**")
                st.write(f"{album['songs_list']}")
            st.write(f"Album added by **{album["user_id"]}**")

            st.write(f"Rate the album: **{album['title']}**")
            rating = st.slider(
                "Select a rating",
                key=album['id'],
                min_value=0.0,
                max_value=10.0,
                step=0.1
            )
            st.write(f"Selected rating: {rating:.1f}")
            if st.button("Submit Rating", key=f"{album['id']}+a"):
                if album['user_id'] == st.session_state.user_id:
                    st.error("You cannot rate your own album.")
                else:
                    if daily_ratings:
                        i_ids = []
                        u_ids = []
                        for rated in daily_ratings:
                            i_id = rated['item_id']
                            u_id = rated['user_id']
                            i_ids.append(i_id)
                            u_ids.append(u_id)
                        if album['id'] in i_ids and st.session_state.user_id in u_ids:
                            st.error("You have already rated this album.")
                        else:
                            add_rating(album['id'], 'album', rating, st.session_state.user_id)
                            st.write(f"Rating of {rating:.1f} submitted for {album['title']}!")
                                
                    else:
                        add_rating(album['id'], 'album', rating, st.session_state.user_id)
                        st.write(f"Rating of {rating:.1f} submitted for {album['title']}!")
