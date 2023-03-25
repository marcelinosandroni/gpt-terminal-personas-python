from speech import Speech
import pyttsx3

class PyttsxSpeech(Speech):
    engine: pyttsx3.Engine

    def __init__(self)
        self.engine = pyttsx3.init()

    def say(self, text: str):
        if not text:
            raise ValueError('text is required')
        self.engine.say(text)
        self.engine.runAndWait()

    def save_to_file(self, text: str, filename: str):
        if not text or not filename:
            raise ValueError('text and filename are required')
        self.engine.save_to_file(text, 'response.mp3')
        self.engine.runAndWait()
