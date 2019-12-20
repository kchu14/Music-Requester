import soco
from soco.discovery import by_name
from soco.music_services import MusicService
from json import dumps

# speakers = soco.discover()
# for speaker in speakers:
#     print(speaker.player_name, speaker.ip_address)
device = by_name("Rear Deck")

# device.play()
print(device.get_queue())
print(MusicService.get_all_music_services_names())
print(MusicService.get_subscribed_services_names())
# spotify = MusicService('Spotify 4')
# result = spotify.search(category='tracks', term='Baby Shark')
# print(result)

device.add_uri_to_queue("https://open.spotify.com/track/4HAMLlAK7VVRRZDSOJTv6U")
print(device.get_queue())

# https://open.spotify.com/track/4HAMLlAK7VVRRZDSOJTv6U
