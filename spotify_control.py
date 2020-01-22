import sys

import spotipy
import spotipy.util as util
import os
import pprint

SPOTIPY_CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
SPOTIPY_REDIRECT_URI = os.environ["SPOTIPY_REDIRECT_URI"]

# if len(sys.argv) > 3:
#     username = sys.argv[1]
#     playlist_id = sys.argv[2]
#     track_ids = sys.argv[3:]
# else:
#     print("Usage: %s username playlist_id track_id ..." % (sys.argv[0],))
#     sys.exit()

username = "kchu6666"
scope = "playlist-modify-public"
token = util.prompt_for_user_token(
    username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, "http://127.0.0.1"
)
playlist_id = "5cfr6TeXBbtaad1ZeqGSOd"
track_ids = ["2GpBrAoCwt48fxjgjlzMd4","2374M0fQpWi3dLnB54qaLX"]

# https://open.spotify.com/playlist/5cfr6TeXBbtaad1ZeqGSOd
# https://open.spotify.com/track/6ttsH99vfvkAPF3s1tIPqB
# util.prompt_for_user_token(username,scope,client_id='5d00a3845e8e4a389229c0bf260c82b7',client_secret='https://localhost:3000',redirect_uri='your-app-redirect-url')
# https://open.spotify.com/track/6ttsH99vfvkAPF3s1tIPqB
# https://open.spotify.com/track/2GpBrAoCwt48fxjgjlzMd4
if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
    print(results)
    search_result = sp.search("Africa", limit=10, offset=0, type="track")
    pprint.pprint(search_result['tracks']['items'][0]['id'])
else:
    print("Can't get token for", username)
