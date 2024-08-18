from spotipy import Spotify, SpotifyClientCredentials

from models.song import Song
from utils.helper import Helper
from utils.storage_handler import StorageHandler


class SpotifyAPIClient:

    def __init__(self):
        self._spotify: Spotify = Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=Helper.load_env_variable("SPOTIFY_CLIENT_ID"),
                client_secret=Helper.load_env_variable("SPOTIFY_CLIENT_SECRETE")
            )
        )

    def get_songs(self, query: str, limit=5) -> list[Song]:

        """
            Retrieves a list of songs based on a search query.

            Args:
                query (str): The search query for retrieving songs.
                limit (int): The maximum number of songs to fetch from the API if not in stored data.

            Returns:
                list[Song]: A list of Song objects retrieved either from stored data or the Spotify API.
            """
        try:
            search_results: list[Song] = StorageHandler.search_song(query=query)
        except ValueError as e:
            raise e
        if not search_results:
            try:
                search_results: list[Song] = self._search_song(query, limit=limit)
            except ValueError as e:
                raise e

        return search_results

    def _search_song(self, query: str, limit) -> list[Song]:
        songs: list[Song] = []
        search_results: list[dict] = self._spotify.search(q=query, limit=limit)["tracks"]["items"]
        for song_data in search_results:
            try:
                song: Song = Song.from_dict(song_data)
                StorageHandler.save_song(song, query)
                songs.append(song)
            except Exception as e:
                raise e
        return songs


if __name__ == '__main__':
    spotify = SpotifyAPIClient()
    songs_ = spotify.get_songs("Mamushi")
    for song_ in songs_:
        print(song_)
