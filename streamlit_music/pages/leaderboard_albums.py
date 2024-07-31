import streamlit as st
from utils.database import get_ratings, get_albums
import pandas as pd

def app():
    st.title("Albums Leaderboard")

    st.header("Album of the Day")
    ratings_day = get_ratings("album", "day")
    albums_day = get_albums("day")
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
    albums_with_avg = []
    for album in albums_day:
        if album['id'] in avg_ratings:
            avg = avg_ratings[album['id']]['rating'] / avg_ratings[album['id']]['count']
            albums_with_avg.append({
                'title': album['title'],
                'user_id': album['user_id'],
                'avg_rating': avg
            })
    albums_with_avg_sorted = sorted(albums_with_avg, key=lambda x: x['avg_rating'], reverse=True)
    df = pd.DataFrame(albums_with_avg_sorted)
    st.table(df[['title', 'avg_rating', 'user_id']])

    st.header("Album of the Week")
    ratings_week = get_ratings("album", "week")
    albums_week = get_albums("week")
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
    albums_with_avg = []
    for album in albums_week:
        if album['id'] in avg_ratings:
            avg = avg_ratings[album['id']]['rating'] / avg_ratings[album['id']]['count']
            albums_with_avg.append({
                'title': album['title'],
                'user_id': album['user_id'],
                'avg_rating': avg
            })
    albums_with_avg_sorted = sorted(albums_with_avg, key=lambda x: x['avg_rating'], reverse=True)
    df = pd.DataFrame(albums_with_avg_sorted)
    st.table(df[['title', 'avg_rating', 'user_id']])

    st.header("All-Time Album")
    ratings_all_time = get_ratings("album", "all-time")
    albums_all_time = get_albums("all-time")
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
    albums_with_avg = []
    for album in albums_all_time:
        if album['id'] in avg_ratings:
            avg = avg_ratings[album['id']]['rating'] / avg_ratings[album['id']]['count']
            albums_with_avg.append({
                'title': album['title'],
                'user_id': album['user_id'],
                'avg_rating': avg
            })
    albums_with_avg_sorted = sorted(albums_with_avg, key=lambda x: x['avg_rating'], reverse=True)
    df = pd.DataFrame(albums_with_avg_sorted)
    st.table(df[['title', 'avg_rating', 'user_id']])
