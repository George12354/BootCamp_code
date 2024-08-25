import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

# Write your code below this line 👇

spotify_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
formatted_date = ""

# This section is for the spotify date
try:
    # Attempt to convert the input string to a datetime object with the specified format
    formatted_date = datetime.strptime(spotify_date, '%Y-%m-%d')

    # Format the datetime object to display only YYYY-MM-DD
    formatted_date_str = formatted_date.strftime('%Y-%m-%d')
    formatted_date = formatted_date_str
except ValueError:
    print("Incorrect format. Please enter the date in YYYY-MM-DD format.")

# Section to scrape spotify web page
URL = f"https://www.billboard.com/charts/hot-100/{formatted_date}"

response = requests.get(url=URL)
spotify_web_page = response.text

soup = BeautifulSoup(spotify_web_page, "html.parser")

spotify_artist = soup.find_all(class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max "
                                      "u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block "
                                      "a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")

spotify_song = soup.find_all(class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size"
                                    "-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-"
                                    "truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

artist = []
song = []

for artists in spotify_artist:
    artist.append(artists.getText().strip())
for songs in spotify_song:
    song.append(songs.getText().strip())

print(artist)
print(song)

# This section is for getting the artist uri for the playlist--using spotipy

client_credentials_manager = SpotifyClientCredentials()
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

artist_uri = []

for artist_song in song:
    result = sp.search(artist_song)
    # pprint(result)
    artist_uri.append(result['tracks']['items'][0]['album']['artists'][0]['uri'])

print(artist_uri)

# try:
#     if artist_name == artist:
#         print("Is a match, add to playlist")
# except ValueError:
#     pass

# This part is to create a playlist

user_id = sp.me()['id']
playlist = sp.user_playlist_create(user=user_id, name=f"{formatted_date} Billboard 100")
print(playlist)

# This part is for adding items to a playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=artist_uri)


# client_credentials_manager: Ideal for applications that only need to fetch public data from Spotify without
# involving user accounts.
# auth_manager=SpotifyOAuth: Necessary for applications that need to perform actions on
# behalf of a user, such as creating or modifying playlists, accessing user libraries, etc.
#
# client_credentials_manager: No scopes needed since it only accesses public data.
# auth_manager=SpotifyOAuth: Requires specific scopes to access user data or perform user-specific actions.
# Scopes define the permissions your application requests.
