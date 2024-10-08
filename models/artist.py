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
            "images": [{"url": self.image_url}]
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Artist":
        return cls(
            name=data.get("name", ""),
            bio=data.get("bio", ""),
            image_url=data.get("images", [{}])[0].get("url", "")
        )

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def bio(self) -> str:
        return self._bio

    @bio.setter
    def bio(self, bio: str) -> None:
        self._bio = bio

    @property
    def image_url(self) -> str:
        return self._image_url

    def __repr__(self) -> str:
        return f"Name: {self.name}, Biography: {self.bio}"
