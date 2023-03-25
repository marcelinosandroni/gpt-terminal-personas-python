from speech import Speech
import requests


class ElevenLabsSpeech(Speech):
    _URL = 'https://api.11labs.com/v1/speech'

    def __init__(self, api_key):
        self.api_key = api_key

    def say(self, text):
        response = requests.post(self._URL, headers={
            'Authorization': self.api_key}, data={'text': text})
        print(response)

        try:
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as error:
            print(error)
            return
