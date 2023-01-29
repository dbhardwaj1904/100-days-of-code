from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

day = True
month = True
year = True

dd = input("Enter day (1-31) you would like to go: ")
mm = input("Enter month (1-12) in numeric you would like to go: ")
yyyy = input("Enter 4 digit year you would like to go: ")
date = f"{dd}-{mm}-{yyyy}"

url = "https://www.billboard.com/charts/hot-100/"+date
response = requests.get(url)
content = response.text

soup = BeautifulSoup(content, 'html.parser')
song_name_spans = soup.findAll(name="span", class_="chart-element_information_song")
song_names = [song.getText()
              for song in song_name_spans]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id="UNIQUE_CLIENT_ID",
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

song_uris = []
for song in song_names:
    result = sp.search(q=f"track:{song} year:{yyyy}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
    except IndexError:
        print(f"{song} doesn't exists in Spotify, Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
