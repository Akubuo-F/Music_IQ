class Song:

    def __init__(self, title: str, artists: list[str]):
        self._title: str = title
        self._artists: list[str] = artists

    @property
    def title(self) -> str:
        return self._title

    @property
    def artists(self) -> list[str]:
        return self._artists
