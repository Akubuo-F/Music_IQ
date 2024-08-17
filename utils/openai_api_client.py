from utils.ai_api_client import AIAPIClient


class OpenaiAPIClient(AIAPIClient):

    # Override
    def get_response(self, prompt: str) -> dict[str, str]:
        pass
