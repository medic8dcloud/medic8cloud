import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys

# Load .env
load_dotenv()

# Setup client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
))

# Playlist fetcher
def get_user_playlists(user_id):
    playlists = sp.user_playlists(user_id)
    for p in playlists['items']:
        print(f"{p['name']} - {p['external_urls']['spotify']}")

# Use CLI arg or fallback
user = sys.argv[1] if len(sys.argv) > 1 else "spotify"
get_user_playlists(user)
