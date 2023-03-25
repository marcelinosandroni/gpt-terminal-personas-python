from speech import Speech


class OpenaiWhisperSpeech(Speech):
    def __init__(self, API_KEY: str):
        self._API_KEY = API_KEY
    
    def say(self, text):
        print(text)
