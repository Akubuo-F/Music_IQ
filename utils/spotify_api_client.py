import requests
from spotipy import Spotify, SpotifyClientCredentials, SpotifyException

from models.song import Song
from utils.helper import Helper
from utils.storage_handler import StorageHandler


class SpotifyAPIClient:
    """
    A client for interacting with the Spotify API to retrieve metadata
    of songs based on a search query. The client first attempts to retrieve
    songs from local storage before querying the Spotify API to avoid
    hitting the API rate limit.

    Attributes:
        _spotify (Spotify): An instance of the Spotify API client.
    """

    def __init__(self):
        self._spotify: Spotify = Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=Helper.load_env_variable("SPOTIFY_CLIENT_ID"),
                client_secret=Helper.load_env_variable("SPOTIFY_CLIENT_SECRET")  # corrected spelling
            )
        )

    def get_songs(self, query: str, limit: int = 5) -> list[Song]:
        """
        Retrieves a list of songs based on a search query.

        This method first checks local storage for existing song data. If
        no songs are found, it queries the Spotify API to get the song
        data.

        Args:
            query (str): The search query for retrieving songs.
            limit (int): The maximum number of songs to fetch from the
                         API if they are not found in local storage.

        Returns:
            list[Song]: A list of Song objects retrieved either from
                         stored data or the Spotify API.

        Raises:
            ValueError: If there are issues accessing or retrieving
                        song data from local storage or the Spotify API.
        """
        search_results: list[Song] = StorageHandler.search_song(query=query)

        if not search_results:
            search_results = self._search_song(query, limit=limit)

        return search_results

    def _search_song(self, query: str, limit: int) -> list[Song]:
        """
        Searches for songs using the Spotify API based on a query.

        This method fetches songs from the Spotify API, saves them to
        local storage, and returns a list of Song objects.

        Args:
            query (str): The search query for retrieving songs from
                         the Spotify API.
            limit (int): The maximum number of songs to fetch from the
                         API.

        Returns:
            list[Song]: A list of Song objects retrieved from the
                         Spotify API.

        Raises:
            Exception: If there are issues accessing the Spotify API or
                        saving songs to storage.
        """
        songs: list[Song] = []
        try:
            search_results: list[dict] = self._spotify.search(q=query, limit=limit)["tracks"]["items"]
            for song_data in search_results:
                song: Song = Song.load_from_dict(song_data)
                StorageHandler.save_song(song, query)
                songs.append(song)
        except KeyError as e:
            raise Exception("Invalid response structure from Spotify API; expected 'tracks' or 'items' key.") from e
        except requests.exceptions.RequestException as e:
            raise Exception("Failed to connect to Spotify API; check your network connection.") from e
        except ValueError as e:
            raise Exception("Failed to load song data from the response.") from e
        except TypeError as e:
            raise Exception("Data type mismatch when loading song data.") from e
        except SpotifyException as e:
            raise Exception(f"Spotify API returned an error: {e}") from e

        return songs


if __name__ == '__main__':
    spotify = SpotifyAPIClient()
    songs_ = spotify.get_songs("Mamushi")
    for song_ in songs_:
        print(song_)
