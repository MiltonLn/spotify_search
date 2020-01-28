def parse_tracks(tracks_json):
    parsed_tracks = []
    tracks = tracks_json.get("tracks").get("items")

    for track in tracks:
        artists = ", ".join([
            artist.get("name") for artist in track.get("artists")
        ])
        parsed_tracks.append({
            "id": track.get("id"),
            "name": track.get("name"),
            "artist": artists,
            "duration": track.get("duration_ms") / 60000,
            "preview_url": track.get("preview_url")
        })
    return parsed_tracks


def parse_albums(albums_json):
    parsed_albums = []
    albums = albums_json.get("albums").get("items")

    for album in albums:
        artists = ", ".join([
            artist.get("name") for artist in album.get("artists")
        ])
        parsed_albums.append({
            "id": album.get("id"),
            "name": album.get("name"),
            "artist": artists,
            "release_date": album.get("release_date")
            "total_tracks": album.get("total_tracks")
        })
    return parsed_albums


def parse_artists(artists_json):
    parsed_artists = []
    artists = artists_json.get("artists").get("items")

    for artist in artists:
        parsed_artists.append({
            "id": artist.get("id"),
            "name": artist.get("name"),
            "genres": artist.get("genres"),
            "followers": artist.get("followers").get("total")
        })
    return parsed_artists
