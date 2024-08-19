import json

from models.song import Song


class SongBuilder:

    @staticmethod
    def build_from_local(local_data: list[str]) -> list[Song]:
        songs: list[Song] = []
        for json_str in local_data:
            song_data: dict = json.loads(json_str)
            song: Song = Song.from_dict(song_data)
            songs.append(song)
        return songs

    @staticmethod
    def build_from_api(api_data: list[dict]) -> list[Song]:
        songs: list[Song] = []
        for song_data in api_data:
            song: Song = Song.from_dict(song_data)
            songs.append(song)
        return songs
