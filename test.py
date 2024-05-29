import requests
import os
from lyricsgenius import Genius
from dotenv import load_dotenv

load_dotenv()
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

genius = Genius(os.environ.get("GENIUS_ACCESS_TOKEN"))

artist = genius.search_artist("Andy Shauf", max_songs=1, sort="title")

for i in range(5): print("*" * i)
print(len(artist))
print(artist, "\n")
print(artist.name, "\n")
print(artist._body["description"]["plain"], "\n")
print(artist.songs[0])

song = genius.search_song("Like That")
print(song.lyrics)
for i in range(5): print("*" * i)

album = genius.search_album("WE DON'T TRUST YOU")
print(album._body)
print(album.artist)
print(len(album.tracks))
print(album.tracks[-1].song)
#artist.save_lyrics()

def abstract_artist():
    return [artist.name, artist._body, artist.songs]