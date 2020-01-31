import sys

import spotipy
import spotipy.util as util
import os
import pprint
import time
from exceptions import DuplicateSongError


class SpotifyController:
    def __init__(self):
        SPOTIPY_CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
        SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
        # SPOTIPY_REDIRECT_URI = os.environ["SPOTIPY_REDIRECT_URI"]
        # TODO make env variable
        self.username = "kchu6666"
        self.playlist_id = "5cfr6TeXBbtaad1ZeqGSOd"
        scope = "playlist-modify-public"

        self.token = util.prompt_for_user_token(
            self.username,
            scope,
            SPOTIPY_CLIENT_ID,
            SPOTIPY_CLIENT_SECRET,
            "http://127.0.0.1",
        )
        self.added_tracks = []
        self.tracks = set()
        if self.token:
            self.sp = spotipy.Spotify(auth=self.token)
            self.sp.trace = False
        else:
            print("Can't get token for", username)

    def add_track(self, song_title: str):
        # TODO add try catch
        self.tracks_in_playlist()
        search_result = self.sp.search(song_title, limit=10, offset=0, type="track")
        song_id = search_result["tracks"]["items"][0]["id"]
        if song_id in self.tracks:
            raise DuplicateSongError
        results = self.sp.user_playlist_add_tracks(
            self.username, self.playlist_id, [song_id]
        )
        name = search_result["tracks"]["items"][0]["name"]
        artist = search_result["tracks"]["items"][0]["artists"][0]["name"]
        self.added_tracks.append(song_id)
        return name, artist

    def tracks_in_playlist(self):
        results = self.sp.playlist(self.playlist_id, fields="tracks,next")
        tracks = results["tracks"]

        self.show_update_tracks(tracks)
        while tracks["next"]:
            tracks = sp.next(tracks)
            self.show_update_tracks(tracks)

    def show_update_tracks(self, tracks):
        for i, item in enumerate(tracks["items"]):
            track = item["track"]
            print(
                "   %d %32.32s %s %s"
                % (i, track["artists"][0]["name"], track["name"], track["id"])
            )
            # TODO add song info and artist for display
            self.tracks.add(track["id"])

    def remove_added(self):
        results = self.sp.user_playlist_remove_all_occurrences_of_tracks(
            self.username, self.playlist_id, self.added_tracks, snapshot_id=None
        )

    def start_playback(self):
        results = self.sp.start_playback(
            device_id=None, context_uri=playlist_id, offset=0
        )
        print(results)
        # sp.next_track()


if __name__ == "__main__":
    sc = SpotifyController()
    sc.add_track("Stop Loving You")
    sc.tracks_in_playlist()
    sc.remove_added()
    sc.tracks_in_playlist()
    # spotify:track:73bzcsDjx9FqzqKWcPLMiH
