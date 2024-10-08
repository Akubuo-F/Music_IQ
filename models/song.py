from utils.savable import Savable


class Song(Savable):

    def __init__(self, title: str, artists: list[str], image_url: str, preview_url: str) -> None:
        self._title: str = title
        self._artists: list[str] = artists
        self._image_url: str = image_url
        self._preview_url: str = preview_url

    @classmethod
    def from_dict(cls, data: dict) -> "Song":
        return cls(
            title=data.get("name", ""),
            artists=[artist.get("name", "") for artist in data.get("artists", [])],
            image_url=data.get("album", {}).get("images", [{}])[0].get("url", ""),
            preview_url=data.get("preview_url", "")
        )

    @property
    def to_dict(self) -> dict:
        return {
            "name": self.title,
            "artists": [{"name": name} for name in self.artists],
            "album": {"images": [{"url": self.image_url}]},
            "preview_url": self.preview_url
        }

    @property
    def title(self) -> str:
        return self._title

    @property
    def artists(self) -> list[str]:
        return self._artists

    @property
    def image_url(self) -> str:
        return self._image_url

    @property
    def preview_url(self) -> str:
        return self._preview_url

    def __repr__(self) -> str:
        return f"Title: {self.title}, Artists: {', '.join(self.artists)}"
