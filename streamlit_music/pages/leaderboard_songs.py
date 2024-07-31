import streamlit as st
from utils.database import get_ratings, get_songs
import pandas as pd

def app():
    st.title("Songs Leaderboard")

    st.header("Song of the Day")
    ratings_day = get_ratings("song", "day")
    songs_day = get_songs("day")
    avg_ratings = {}
    for rating in ratings_day:
        if rating['item_id'] in avg_ratings:
            avg_ratings[rating['item_id']]['rating'] += rating['rating']
            avg_ratings[rating['item_id']]['count'] += 1
        else:
            avg_ratings[rating['item_id']] = {
                'rating': rating['rating'],
                'count': 1
            }
    songs_with_avg = []
    for song in songs_day:
        if song['id'] in avg_ratings:
            avg = avg_ratings[song['id']]['rating'] / avg_ratings[song['id']]['count']
            songs_with_avg.append({
                'title': song['title'],
                'user_id': song['user_id'],
                'avg_rating': avg
            })
    songs_with_avg_sorted = sorted(songs_with_avg, key=lambda x: x['avg_rating'], reverse=True)
    df = pd.DataFrame(songs_with_avg_sorted)
    st.table(df[['title', 'avg_rating', 'user_id']])

    st.header("Song of the Week")
    ratings_week = get_ratings("song", "week")
    songs_week = get_songs("week")
    avg_ratings = {}
    for rating in ratings_week:
        if rating['item_id'] in avg_ratings:
            avg_ratings[rating['item_id']]['rating'] += rating['rating']
            avg_ratings[rating['item_id']]['count'] += 1
        else:
            avg_ratings[rating['item_id']] = {
                'rating': rating['rating'],
                'count': 1
            }
    songs_with_avg = []
    for song in songs_week:
        if song['id'] in avg_ratings:
            avg = avg_ratings[song['id']]['rating'] / avg_ratings[song['id']]['count']
            songs_with_avg.append({
                'title': song['title'],
                'user_id': song['user_id'],
                'avg_rating': avg
            })
    songs_with_avg_sorted = sorted(songs_with_avg, key=lambda x: x['avg_rating'], reverse=True)
    df = pd.DataFrame(songs_with_avg_sorted)
    st.table(df[['title', 'avg_rating', 'user_id']])

    st.header("All-Time Song")
    ratings_all_time = get_ratings("song", "all-time")
    songs_all_time = get_songs("all-time")
    avg_ratings = {}
    for rating in ratings_all_time:
        if rating['item_id'] in avg_ratings:
            avg_ratings[rating['item_id']]['rating'] += rating['rating']
            avg_ratings[rating['item_id']]['count'] += 1
        else:
            avg_ratings[rating['item_id']] = {
                'rating': rating['rating'],
                'count': 1
            }
    songs_with_avg = []
    for song in songs_all_time:
        if song['id'] in avg_ratings:
            avg = avg_ratings[song['id']]['rating'] / avg_ratings[song['id']]['count']
            songs_with_avg.append({
                'title': song['title'],
                'user_id': song['user_id'],
                'avg_rating': avg
            })
    songs_with_avg_sorted = sorted(songs_with_avg, key=lambda x: x['avg_rating'], reverse=True)
    df = pd.DataFrame(songs_with_avg_sorted)
    st.table(df[['title', 'avg_rating', 'user_id']])