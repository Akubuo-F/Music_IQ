import requests
from spotipy import Spotify, SpotifyClientCredentials, SpotifyException

from builders.artist_builder import ArtistBuilder
from builders.song_builder import SongBuilder
from utils.storage import Storage
from models.artist import Artist
from models.model import Model
from models.song import Song
from utils.helper import Helper
from utils.local_storage import LocalStorage


class SpotifyAPIClient:

    def __init__(self):
        self._spotify: Spotify = Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=Helper.load_env_variable("SPOTIFY_CLIENT_ID"),
                client_secret=Helper.load_env_variable("SPOTIFY_CLIENT_SECRET")
            )
        )

    def get_songs(self, query: str, limit: int = 5) -> list[Song]:
        local_data: list[str] = LocalStorage.search(query=query, storage=Storage.SONG)
        if local_data:
            return SongBuilder.build_from_local(local_data)
        else:
            api_data: list[dict] = self._search(query, Model.SONG, limit=limit)
            return SongBuilder.build_from_api(api_data)

    def get_artists(self, song: Song) -> list[Artist]:
        local_data: list[str] = LocalStorage.search(query=song.title, storage=Storage.ARTIST)
        if local_data:
            artists: list[Artist] = ArtistBuilder.build_from_local(local_data)
        else:
            api_data: list[dict] = []
            for name in song.artists:
                api_data += self._search(name, Model.ARTIST, limit=1)
            artists: list[Artist] = ArtistBuilder.build_from_api(api_data)
        return artists

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
    def test_get_songs():
        LocalStorage.clear_storage(Storage.SONG)
        spotify = SpotifyAPIClient()
        songs = spotify.get_songs("Mamushi")
        for song in songs:
            print(song, song.image_url)
            LocalStorage.save(song, "Mamushi", Storage.SONG)

    def test_get_artists():
        LocalStorage.clear_storage(Storage.ARTIST)
        fake_song = Song("Mamushi (feat. Yuki Chiba), Artists: Megan Thee Stallion",
                         ["Megan The Stallion", "千葉雄喜"],
                         "",
                         "")
        spotify = SpotifyAPIClient()
        artists = spotify.get_artists(fake_song)
        for artist in artists:
            print(artist, artist.image_url)
            LocalStorage.save(artist, fake_song.title, Storage.ARTIST)

    def main():
        test_get_songs()
        print("Next")
        test_get_artists()
        LocalStorage.clear_storage(Storage.ARTIST)
        LocalStorage.clear_storage(Storage.SONG)

    main()
