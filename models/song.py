import json

from utils.savable import Savable


class Song(Savable):
    """
    A class representing a song.

    Attributes:
        _title (str): The title of the song.
        _artists (list[str]): A list of artists for the song.
        _preview_url (str): A URL for a preview of the song.
    """

    def __init__(self, title: str, artists: list[str], preview_url: str) -> None:
        """
        Initializes a new instance of the Song class.

        Parameters:
            title (str): The title of the song.
            artists (list[str]): A list of artists for the song.
            preview_url (str): A URL for a preview of the song.
        """
        self._title: str = title
        self._artists: list[str] = artists
        self._preview_url: str = preview_url

    def save(self, location: list[str]) -> None:
        """
        Saves the song object as a JSON string to the specified location.

        Parameters:
            location (list[str]): A list to which the JSON string representation of the song
                                  will be appended.
        """
        location.append(json.dumps(self.__dict__))

    @classmethod
    def load_from_json_str(cls, json_str: str) -> "Song":
        """
        Loads a Song instance from a JSON string representation of the object.

        Parameters:
            json_str (str): A JSON string representing the song object.

        Returns:
            Song: A new instance of the Song class.
        """
        data: dict = json.loads(json_str)
        return cls(
            title=data["_title"],
            artists=data["_artists"],
            preview_url=data["_preview_url"]
        )

    @classmethod
    def load_from_dict(cls, data: dict) -> "Song":
        """
        Loads a Song instance from a dictionary representation.

        Parameters:
            data (dict): A dictionary containing the song's data with keys
                         'name', 'artists', and 'preview_url'.

        Returns:
            Song: A new instance of the Song class.
        """
        title: str = data["name"]
        artists: list[str] = [artist["name"] for artist in data["artists"]]
        preview_url: str = data["preview_url"]
        return cls(title, artists, preview_url)

    @property
    def title(self) -> str:
        """str: The title of the song."""
        return self._title

    @property
    def artists(self) -> list[str]:
        """list[str]: A list of artists for the song."""
        return self._artists

    def __repr__(self) -> str:
        """Returns a string representation of the song."""
        return f"Title: {self.title}, Artists: {', '.join(self.artists)}"
