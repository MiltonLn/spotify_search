from importlib import import_module

from flask import Flask, request, jsonify

from .spotify_api import get_spotify_response


app = Flask(__name__)
app.config.from_object("spotify_search.settings")


@app.route("/search", methods=["GET"])
def search():
    search_term = request.args.get("search_term", "")
    limit = request.args.get("limit")
    search_type = request.args.get("type")
    assert search_type in ["artist", "track", "album"]

    json_response = get_spotify_response(
        search_term,
        limit=limit,
        search_type=search_type
    )

    parse_method = import_module(f"spotify_search.utils.parse_{search_type}s")
    search_results = parse_method(json_response)
    return jsonify(search_results)
