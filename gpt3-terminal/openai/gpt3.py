from openai_connector import OpenAiConnector
from openai_model import OpenAiModel


class GPT3(OpenAiModel):
    _MODEL_NAME = 'gpt-3.5-turbo'
    _instructions: str = None

    def __init__(self, openai_connector: OpenAiConnector):
        super().__init__(openai_connector)

    @property
    def name(self):
        return self._MODEL_NAME

    def instructions(self, instructions: str):
        self._instructions = instructions

    def prompt(self, message: str):
        system_message = {
            'role': 'system', 'content': self._instructions if self._instructions else ''}
        user_message = {'role': 'user', 'content': message if message else ''}
        response = self._OPENAI_CONNECTOR.ChatCompletion.create(
            model=self._MODEL_NAME, messages=[system_message, user_message])
        return response['choices'][0]['message']['content']
