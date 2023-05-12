import openai


class OpenAiConnector:
    def __init__(self, api_key: str, openai: openai):
        self._api_key = api_key
        openai.api_key = self._api_key
