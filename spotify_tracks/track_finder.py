from flask import Flask, request, jsonify

from .spotify_api import get_spotify_tracks
from .utils import parse_tracks


app = Flask(__name__)
app.config.from_object("spotify_tracks.settings")


@app.route("/find-tracks", methods=["GET"])
def find_tracks():
    search_term = request.args.get("search_term", "")
    limit = request.args.get("limit")
    tracks_json = get_spotify_tracks(search_term, limit=limit)
    tracks_results = parse_tracks(tracks_json)
    return jsonify(tracks_results)
