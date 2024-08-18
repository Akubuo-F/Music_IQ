from typing import Type

from models.artist import Artist
from models.song import Song
from utils.helper import Helper
from utils.savable import Savable


class StorageHandler:

    @staticmethod
    def _save_object(obj: Savable, key: str, json_path: str):
        """Generic method to save an object to the specified JSON path under the given key."""
        full_json_path: str = Helper.get_filepath(json_path)
        data: dict[str, list[str]] = Helper.get_json_data(full_json_path)
        value = data.get(key, [])
        obj.save(location=value)
        data[key] = value
        Helper.save_json_data(data, full_json_path)

    @staticmethod
    def save_song(obj: Savable, key: str, song_datapath: str = "data/song.json"):
        """Saves a song inside a json file"""
        StorageHandler._save_object(obj, key, song_datapath)

    @staticmethod
    def save_artist(obj: Savable, key: str, artist_datapath: str = "data/artist.json"):
        """Saves a song inside a json file"""
        StorageHandler._save_object(obj, key, artist_datapath)

    @staticmethod
    def _search(query: str, datapath: str, obj: Type[Song | Artist]) -> list[Song | Artist]:
        """Generic method to search for objects from stored data."""
        results: list[Song | Artist] = []
        stored_data: dict[str, list[str]] = Helper.get_json_data(Helper.get_filepath(datapath))
        if query in stored_data:
            for obj_str in stored_data[query]:
                obj: Song | Artist = obj.load(obj_str)
                if obj:
                    results.append(obj)
                else:
                    raise ValueError(
                        f"{obj.__name__} object is None after attempting to build from object string."
                    )
        return results

    @staticmethod
    def search_song(query: str, song_datapath: str = "data/song.json") -> list[Song]:
        """Search for songs from stored data."""
        return StorageHandler._search(query, song_datapath, Song)

    @staticmethod
    def search_artist(query: str, artist_datapath: str = "data/artist.json") -> list[Artist]:
        """Search for artists from stored data."""
        return StorageHandler._search(query, artist_datapath, Artist)
