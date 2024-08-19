from utils.savable import Savable


class Artist(Savable):

    def __init__(self, name: str, bio: str, image_url: str) -> None:
        self._name: str = name
        self._bio: str = bio
        self._image_url: str = image_url

    @property
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "bio": self.bio,
            "image_url": self.image_url
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Artist":
        return cls(
            name=data.get("name", ""),
            bio=data.get("bio", ""),
            image_url=data.get("image_url", "")
        )

    @property
    def name(self) -> str:
        return self._name

    @property
    def bio(self) -> str:
        return self._bio

    @property
    def image_url(self) -> str:
        return self._image_url
