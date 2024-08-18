import json

from utils.savable import Savable


class Song(Savable):

    def __init__(self, title: str, artists: list[str], preview_url: str):
        self._title: str = title
        self._artists: list[str] = artists
        self._preview_url: str = preview_url

    def save(self, location: list[str]) -> None:
        location.append(json.dumps(self.__dict__))

    @classmethod
    def load(cls, object_str: str) -> "Song":
        data: dict = json.loads(object_str)
        return cls(
            title=data["_title"],
            artists=data["_artists"],
            preview_url=data["_preview_url"]
        )

    @classmethod
    def from_object_str(cls, data: str) -> "Song":
        return cls.load(data)

    @classmethod
    def from_dict(cls, data: dict) -> "Song":
        title: str = data["name"]
        artists: list[str] = [artist["name"] for artist in data["artists"]]
        preview_url: str = data["preview_url"]
        return cls(title, artists, preview_url)

    @property
    def title(self) -> str:
        return self._title

    @property
    def artists(self) -> list[str]:
        return self._artists

    def __repr__(self):
        return f"Title: {self.title}, Artists: {self.artists}"
