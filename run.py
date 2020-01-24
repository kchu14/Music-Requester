# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import logging
import pprint
from spotify_controller import SpotifyController

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


@app.route("/sms", methods=["GET", "POST"])
def receive_message():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    data = request.form
    # pprint.pprint(data)
    body = data.get("Body")
    resp = MessagingResponse()
    _parse_message(body)
    resp.message("Ahoy! Thanks so much for your message.")
    return str(resp)


def _parse_message(message_body: str):
    logging.debug(message_body)
    if message_body.lower().lstrip().startswith("!add"):
        song_title = message_body.split("!add", 1)[1]
        sc.add_track(song_title)


if __name__ == "__main__":
    app.run(debug=True)
