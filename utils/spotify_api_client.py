from spotipy import Spotify, SpotifyClientCredentials

from models.song import Song
from utils.helper import Helper


class SpotifyAPIClient:

    def __init__(self, datapath: str):
        self._datapath: str = datapath
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
        search_results: list[Song] = []
        try:
            search_results = self._search_song_from_stored_data(query)
        except ValueError as e:
            print(e)
        if not search_results:
            try:
                search_results = self._search_song_from_spotify(query, limit=limit)
            except ValueError as e:
                print(e)

        return search_results

    def _search_song_from_stored_data(self, query: str) -> list[Song]:
        songs: list[Song] = []
        stored_data: dict[str, list[str]] = Helper.get_json_data(self._datapath)
        if query in stored_data:
            for song_data in stored_data[query]:
                song: Song = Song.from_object_str(song_data)
                if song:
                    Helper.save_object(song, query, Helper.get_filepath(self._datapath))
                    songs.append(song)
                else:
                    raise ValueError("Song object is None after attempting to build from object string.")
        return songs

    def _search_song_from_spotify(self, query: str, limit) -> list[Song]:
        songs: list[Song] = []
        search_results: list[dict] = self._spotify.search(q=query, limit=limit)["tracks"]["items"]
        for song_data in search_results:
            try:
                song: Song = Song.from_dict(song_data)
                Helper.save_object(song, query, Helper.get_filepath(self._datapath))
                songs.append(song)
            except Exception as e:
                raise ValueError(f"Failed to build song from Spotify API: {e}")
        return songs
