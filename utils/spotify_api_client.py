import requests
from spotipy import Spotify, SpotifyClientCredentials, SpotifyException

from builders.song_builder import SongBuilder
from data.storage import Storage
from models.model import Model
from models.song import Song
from utils.helper import Helper
from utils.LocalStorage import LocalStorage


class SpotifyAPIClient:

    def __init__(self):
        self._spotify: Spotify = Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=Helper.load_env_variable("SPOTIFY_CLIENT_ID"),
                client_secret=Helper.load_env_variable("SPOTIFY_CLIENT_SECRET")
            )
        )

    def get_songs(self, query: str, limit: int = 5) -> list[Song]:
        results_from_local: list[str] = LocalStorage.search(query=query, storage=Storage.SONG)
        if results_from_local:
            return SongBuilder.build_from_local(results_from_local)
        else:
            results_from_api: list[dict] = self._search(query, Model.SONG, limit=limit)
            return SongBuilder.build_from_api(results_from_api)

    def _search(self, query: str, model: Model,  limit: int) -> list[dict]:
        try:
            search_results: list[dict] = self._spotify.search(
                q=query,
                type="track,artist",
                limit=limit
            )[model.value[1]]["items"]
        except requests.exceptions.RequestException as e:
            raise Exception("Failed to connect to Spotify API; check your network connection.") from e
        except SpotifyException as e:
            raise Exception(f"Spotify API returned an error: {e}") from e

        return search_results


if __name__ == '__main__':
    spotify = SpotifyAPIClient()
    songs_ = spotify.get_songs("Mamushi")
    for song_ in songs_:
        print(song_)
        LocalStorage.save(song_, "Mamushi", Storage.SONG)
