from .openai_model import OpenAiModel


class GPT3(OpenAiModel):
    _MODEL_NAME = 'gpt-3.5-turbo'
    _instructions: str = ''
    _messages = []
    _instructions_registered = False

    def __init__(self):
        super().__init__()

    @property
    def name(self):
        return self._MODEL_NAME

    def instructions(self, instructions: str):
        self._instructions = instructions

    def prompt(self, message: str):
        if not self._instructions_registered:
            self._messages.append(
                {'role': 'system', 'content': self._instructions})
            self._instructions_registered = True
        user_message = {'role': 'user', 'content': message if message else ''}
        self._messages.append(user_message)
        response = self._OPENAI_CHAT.create(
            model=self._MODEL_NAME, messages=self._messages)
        assistant_response = response['choices'][0]['message']
        self._messages.append(assistant_response)
        return assistant_response['content']
