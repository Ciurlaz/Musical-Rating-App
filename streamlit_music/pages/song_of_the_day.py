import streamlit as st
from utils.database import add_song, get_songs, add_rating, get_ratings

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
    youtube_link = st.text_input("Link (optional)")
    favorite_parts = st.text_area("Favorite Bars (optional)")
    lyrics = st.text_area("Lyrics (optional)")

    already = False
    all_time_songs = get_songs("all-time")
    for song in all_time_songs:
        if song["title"] == title and song["artist"] == artist:
            already = True
    
    if st.button("Add Song"):
        if added:
            st.error("You already added a song today.")
        else:
            if already:
                st.error("Song already exists in the database. Try with another one.")
            else:
                if title and artist and youtube_link:
                    add_song(title, artist, youtube_link, favorite_parts, lyrics, st.session_state.user_id)
                    st.success("Song added successfully.")
                else:
                    st.error("Please fill in the required fields.")

    daily_ratings = get_ratings("song", "day")
    st.header("Songs of the Day")
    if not today_songs:
        st.write("No songs added today.")
    else:
        i = 0
        for song in today_songs:
            st.write("---")
            st.write(f"**{song['title']}** by {song['artist']}")
            if song['youtube_link']:
                st.write(f"[Link]({song['youtube_link']})")
            if song['favorite_parts']:
                st.write("**Favorite bars:**")
                st.write(f"{song['favorite_bars']}")
            if song['lyrics']:
                st.write("**Lyrics:**")
                st.write(f"{song['lyrics']}")
            st.write(f"Song added by **{song["user_id"]}**")

            st.write(f"Rate the song: **{song['title']}**")
            rating = float(st.slider(
                "Select a rating",
                key=song['id'],
                min_value=0.0,
                max_value=10.0,
                step=0.1
            ))
            st.write(f"Selected rating: {rating:.1f}")

            if st.button("Submit Rating", key=f"{song['id']}+s"):
                if song['user_id'] == st.session_state.user_id:
                    st.error("You cannot rate your own song.")
                else:
                    if daily_ratings:
                        i_ids = []
                        u_ids = []
                        for rated in daily_ratings:
                            i_id = rated["item_id"]
                            u_id = rated["user_id"]
                            i_ids.append(i_id)
                            u_ids.append(u_id)
                        if song['id'] in i_ids and st.session_state.user_id in u_ids:
                            st.error("You have already rated this song.")
                        else:
                            add_rating(song['id'], 'song', rating, st.session_state.user_id)
                            st.write(f"Rating of {rating:.1f} submitted for {song['title']}!")
                    else:
                        add_rating(song['id'], 'song', rating, st.session_state.user_id)
                        st.write(f"Rating of {rating:.1f} submitted for {song['title']}!")
            i += 1
