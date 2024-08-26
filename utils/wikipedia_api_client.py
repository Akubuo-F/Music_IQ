import requests
from wikipediaapi import Wikipedia, WikipediaPage


class WikipediaAPIClient:

    def __init__(self):
        self._wikipedia: Wikipedia = Wikipedia(
            user_agent="MusicIQ (akubuof.work@gmail.com)",
            language="en"
        )

    def get_artist_info(self, artist_name: str) -> dict[str, str]:
        page_details: dict[str, str] = WikipediaAPIClient._get_page_details(f"{artist_name} musician")
        page_title: str = page_details.get("title", "")
        page: WikipediaPage = self._wikipedia.page(title=page_title)
        if page.exists():
            return {
                "name": page_title,
                "bio": page.summary
            }
        else:
            raise ValueError("Wiki page does not exist.")

    @staticmethod
    def _get_page_details(query: str) -> dict[str, str]:
        url = f"https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json"
        }
        response: requests.Response = requests.get(url, params=params)
        data: dict = response.json()
        if data['query']['search']:
            page_title: str = data['query']['search'][0]['title']
            page_url: str = f"https://en.wikipedia.org/wiki/{page_title.replace(' ', '_')}"
            return {"title": page_title, "url": page_url}
        else:
            ValueError("Wiki page does not exist.")


if __name__ == '__main__':
    wikipedia = WikipediaAPIClient()
    artist1 = "Megan Thee Stallion"
    artist2 = "千葉雄喜"
    artist3 = "Drake"
    artists = (
        artist1,
        artist2,
        artist3,
    )
    for artist in artists:
        artist_info = wikipedia.get_artist_info(artist)
        print(f"Name: {artist_info['name']}, Bio: {artist_info['bio']}")
        print(len(artist_info["bio"]))
