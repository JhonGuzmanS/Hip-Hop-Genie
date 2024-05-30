import requests
import os
from lyricsgenius import Genius
from dotenv import load_dotenv
from add_doc import search_json_

load_dotenv()
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

genius = Genius(os.environ.get("GENIUS_ACCESS_TOKEN"), timeout=10, retries=3)

def abstract_artist(artist_name : str, songs=3):
    artist = genius.search_artist(artist_name, max_songs=songs, sort="popularity")   
    artist.save_lyrics(filename=artist_name, overwrite=True)
    search_json_("Kendrick Lamar")
    return "saved JSON artist"


def abstract_songs(song_name : str):
    song = genius.search_song(song_name)
    song.save_lyrics(filename=song_name, overwrite=True)
    return "saved JSON song"

#abstract_artist("50Cent")