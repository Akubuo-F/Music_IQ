class Artist:

    def __init__(self, name: str, bio: str):
        self._name: str = name
        self._bio: str = bio

    @property
    def name(self) -> str:
        return self._name

    @property
    def bio(self) -> str:
        return self._bio
