import json

from builders.model_builder import ModelBuilder
from models.artist import Artist


class ArtistBuilder(ModelBuilder):

    @staticmethod
    def build_from_local(local_data: list[str]) -> list[Artist]:
        artists: list[Artist] = []
        for json_str in local_data:
            as_dict: dict = json.loads(json_str)
            artist: Artist = Artist.from_dict(as_dict)
            artists.append(artist)
        return artists

    @staticmethod
    def build_from_api(api_data: list[dict]) -> list[Artist]:
        artists: list[Artist] = []
        for artist_data in api_data:
            artist: Artist = Artist.from_dict(artist_data)
            artists.append(artist)
        return artists
