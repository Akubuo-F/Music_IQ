import json
from typing import Any

from utils.savable import Savable


class Song(Savable):

    def __init__(self, title: str, artists: list[str]):
        self._title: str = title
        self._artists: list[str] = artists

    def save(self, location: list[str]) -> None:
        location.append(
            json.dumps(
                {
                    "title": self.title,
                    "artists": self.artists
                }
            )
        )

    @classmethod
    def load(cls, object_str: str) -> Any:
        data: dict = json.loads(object_str)
        return cls(
            title=data["title"],
            artists=data["artists"]
        )

    @classmethod
    def from_object_str(cls, data: str) -> 'Song':
        return cls.load(data)

    @classmethod
    def from_dict(cls, data: dict) -> 'Song':
        title = data["name"]
        artists = [artist["name"] for artist in data["artists"]]
        return cls(title, artists)

    @property
    def title(self) -> str:
        return self._title

    @property
    def artists(self) -> list[str]:
        return self._artists

    def __repr__(self):
        return f"Title: {self.title}, Artists: {self.artists}"
