import os
from openai_connector import OpenAiConnector


class OpenAiModel:
    _API_KEY_LENGTH = 51
    _OPENAI_CONNECTOR = None

    def __init__(self, openai_connector: OpenAiConnector):
        self._OPENAI_CONNECTOR = openai_connector
        self._api_key = os.getenv("OPENAI_API_KEY")

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def set_api_key(self, value: str):
        if type(value) != str:
            raise TypeError(
                f"Invalid API key type, need str, got {type(value)}")
        if not value.startswith('sk-'):
            raise ValueError(
                f"Invalid API key, need to start with 'sk-', got {value}")
        if len(value) != self._API_KEY_LENGTH:
            raise ValueError(
                f"Invalid API key length, need {self._API_KEY_LENGTH} characters, got {len(value)}")
        self._api_key = value

        return self

    def models(self):
        return dir(self._OPENAI_CONNECTOR)
        return self._OPENAI_CONNECTOR.Models.list()