# # Creates a playlist for a user

import argparse
import logging
import spotipy
from spotipy.oauth2 import SpotifyOAuth

logger = logging.getLogger('examples.create_playlist')
logging.basicConfig(level='DEBUG')


def get_args():
    parser = argparse.ArgumentParser(description='Creates a playlist for user')
    parser.add_argument('--playlist', required=True,
                        help='Name of Playlist')
    return parser.parse_args()


# python script to run the code on the command line
# python create_playlist.py --playlist "testing_testing"

def main():
    args = get_args()
    scope = "playlist-modify-public"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    user_id = sp.me()['id']
    print(user_id)
    sp.user_playlist_create(user_id, args.playlist)


if __name__ == '__main__':
    main()
