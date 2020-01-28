import os

import requests


BASE_URL = "https://api.spotify.com/v1"
AUTH_TOKEN = os.getenv("SPOTIFY_AUTH_TOKEN")


def get_spotify_response(search_term, limit=None, search_type=None):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AUTH_TOKEN}"
    }

    url = f"{BASE_URL}/search"
    params = {
        "q": search_term,
        "type": search_type or "track",
        "limit": limit or 10,
    }

    response = requests.get(url, params=params, headers=headers)
    return response.json()
