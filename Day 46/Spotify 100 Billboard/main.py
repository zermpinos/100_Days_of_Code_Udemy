import os
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
import os


def get_billboard_hot_100(date):
    response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
    soup = BeautifulSoup(response.text, 'html.parser')
    song_names_spans = soup.select("li ul li h3")
    return [song.getText().strip() for song in song_names_spans]


def get_song_uris(song_names, year):
    song_uris = []
    for song_name in song_names:
        try:
            query = f"track:{song_name} year:{year}"
            result = sp.search(query, type="track", limit=1)
            song_uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(song_uri)
        except IndexError:
            print(f"Song '{song_name}' not found on Spotify. Skipping.")
    return song_uris


def create_playlist_and_add_songs(user_id, playlist_name, song_uris):
    new_playlist = sp.user_playlist_create(user_id, playlist_name, public=False, description="Billboard Hot 100 songs for the specified date")
    playlist_id = new_playlist["id"]
    sp.playlist_add_items(playlist_id, song_uris)
    return playlist_id


if __name__ == "__main__":
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    song_names = get_billboard_hot_100(date)
    print("Top 100 songs:")
    for index, song in enumerate(song_names, start=1):
        print(f"{index}. {song}")

    client_ID = "YOUR_SPOTIFY_ID"
    client_SECRET = "YOUR_SPOTIFY_SECRET"
    client_USERNAME = "YOUR_SPOTIFY_USERNAME"
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="https://example.com",
            client_id=client_ID,
            client_secret=client_SECRET,
            show_dialog=True,
            cache_path="token.txt",
            username=client_USERNAME
        )
    )
    user_id = sp.current_user()["id"]
    year = date.split("-")[0]
    song_uris = get_song_uris(song_names, year)
    pprint(song_uris)

    playlist_name = f"{date} Billboard 100"
    playlist_id = create_playlist_and_add_songs(user_id, playlist_name, song_uris)
    print(f"Successfully created the playlist '{playlist_name}' and added {len(song_uris)} songs.")
