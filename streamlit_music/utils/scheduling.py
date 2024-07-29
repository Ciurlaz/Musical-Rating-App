# utils/scheduling.py
import schedule
import time
import threading
from utils.database import get_winner
from utils.discord import post_to_discord

def announce_winner():
    song_winner = get_winner('song')
    album_winner = get_winner('album')

    if song_winner:
        post_to_discord(f"Song of the Day: {song_winner[0]}")
    
    if album_winner:
        post_to_discord(f"Album of the Day: {album_winner[0]}")

def schedule_winner_announcement():
    schedule.every().day.at("23:59").do(announce_winner)

    def run_schedule():
        while True:
            schedule.run_pending()
            time.sleep(1)

    threading.Thread(target=run_schedule).start()
