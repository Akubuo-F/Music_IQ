from utils.savable import Savable


class Artist(Savable):

    def __init__(self, name: str, bio: str):
        self._name: str = name
        self._bio: str = bio

    def save(self, location: list[str]) -> None:
        pass

    @classmethod
    def load_from_json_str(cls, object_str: str) -> "Savable":
        pass

    @property
    def name(self) -> str:
        return self._name

    @property
    def bio(self) -> str:
        return self._bio
