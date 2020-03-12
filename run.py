# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import logging
import pprint
from spotify_controller import SpotifyController
from exceptions import DuplicateSongError

blank_space = "______\n\n"

app = Flask(__name__)
sc = SpotifyController()
# twilio phone-numbers:update "+12056196866" --sms-url="http://localhost:5000/sms"
logging.basicConfig(
    filename="twilio_log",
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)

admins = set(["+18609873868"])

@app.route('/')
def swag():
    return 'swaggggg'

@app.route("/sms", methods=["GET", "POST"])
def receive_message():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    data = request.form
    # pprint.pprint(data)
    body = data.get("Body")
    messengers_num = data.get("From")
    resp = MessagingResponse()

    _execute_command(body, messengers_num, resp)

    return str(resp)


def _execute_command(message_body, messengers_num, resp):
    logging.debug(message_body)
    if message_body.lower().lstrip().startswith("!add"):
        song_title = message_body.split("!add", 1)[1]
        try:
            name, artist = sc.add_track(song_title)
            resp.message(f"{blank_space}Added {name} by {artist} to the queue.")
        except DuplicateSongError:
            resp.message(
                f"{blank_space}Song is already in the queue. Didn't add duplicate song."
            )
    if message_body.lower().lstrip().startswith("!playlist"):
        tracks = sc.tracks_in_playlist()
        resp.message(tracks)

    if (
        message_body.lower().lstrip().startswith("!remove_added")
        and messengers_num in admins
    ):
        sc.remove_added()
        resp.message(f"{blank_space}Removed added songs.")

    else:
        resp.message(f"{blank_space}Unknown command. Commands are !add.")


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
