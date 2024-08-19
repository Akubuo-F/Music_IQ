from typing import Type

from models.artist import Artist
from models.song import Song
from utils.helper import Helper
from utils.savable import Savable


class StorageHandler:
    @staticmethod
    def _save_object(obj: Savable, key: str, json_path: str):
        """
        Saves a given object to the specified JSON file under the provided key.

        Args:
            obj (Savable): The object to be saved, which must implement a save method.
            key (str): The key under which the object will be saved in the JSON file.
            json_path (str): The path to the JSON file.

        Raises:
            Exception: If there is an error retrieving or saving data.
        """
        full_json_path: str = Helper.get_filepath(json_path)
        data: dict[str, list[str]] = Helper.get_json_data(full_json_path)
        value = data.get(key, [])

        obj.save(location=value)
        data[key] = value
        Helper.save_json_data(data, full_json_path)

    @staticmethod
    def save_song(obj: Song, key: str, song_datapath: str = "data/song.json"):
        """
        Saves a song object to the specified JSON file.

        Args:
            obj (Savable): The song object to be saved.
            key (str): The key under which the song will be saved in the JSON file.
            song_datapath (str): The path to the song JSON file. Defaults to "data/song.json".
        """
        StorageHandler._save_object(obj, key, song_datapath)

    @staticmethod
    def save_artist(obj: Artist, key: str, artist_datapath: str = "data/artist.json"):
        """
        Saves an artist object to the specified JSON file.

        Args:
            obj (Savable): The artist object to be saved.
            key (str): The key under which the artist will be saved in the JSON file.
            artist_datapath (str): The path to the artist JSON file. Defaults to "data/artist.json".
        """
        StorageHandler._save_object(obj, key, artist_datapath)

    @staticmethod
    def _search(query: str, datapath: str, obj: Type[Song | Artist]) -> list[Song | Artist]:
        """
        Searches for objects in stored data based on a query.

        Args:
            query (str): The query string used to search for objects.
            datapath (str): The path to the JSON file containing stored data.
            obj (Type[Song | Artist]): The class type of the objects to search for (Song or Artist).

        Returns:
            list[Song | Artist]: A list of matching objects based on the query.

        Raises:
            ValueError: If an object string cannot be converted into a valid object.
        """
        results: list[Song | Artist] = []
        stored_data: dict[str, list[str]] = Helper.get_json_data(Helper.get_filepath(datapath))

        if query in stored_data:
            for obj_str in stored_data[query]:
                obj_instance: Song | Artist = obj.load_from_json_str(obj_str)
                if obj_instance:
                    results.append(obj_instance)
                else:
                    raise ValueError(
                        f"{obj.__name__} object is None after attempting to build from object string."
                    )
        return results

    @staticmethod
    def search_song(query: str, song_datapath: str = "data/song.json") -> list[Song]:
        """
        Searches for songs based on a query string.

        Args:
            query (str): The query string used to search for songs.
            song_datapath (str): The path to the song JSON file. Defaults to "data/song.json".

        Returns:
            list[Song]: A list of matching Song objects.
        """
        return StorageHandler._search(query, song_datapath, Song)

    @staticmethod
    def search_artist(query: str, artist_datapath: str = "data/artist.json") -> list[Artist]:
        """
        Searches for artists based on a query string.

        Args:
            query (str): The query string used to search for artists.
            artist_datapath (str): The path to the artist JSON file. Defaults to "data/artist.json".

        Returns:
            list[Artist]: A list of matching Artist objects.
        """
        return StorageHandler._search(query, artist_datapath, Artist)
