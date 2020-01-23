def parse_tracks(tracks_json):
    parsed_tracks = []
    tracks = tracks_json.get("items")

    for track in tracks:
        artists = ", ".join([artist.get("name") for artist in track.get("artists")])
        parsed_tracks.append({
            "id": track.get("id"),
            "name": track.get("name"),
            "artist": artists,
            "duration": track.get("duration_ms") / 60000,
            "preview_url": track.get("preview_url")
        })

    return parsed_tracks
