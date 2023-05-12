from speech import Speech
# import aws sdk

class AwsSpeech(Speech):
    def __init__(self, api_key: str):
        self._api_key = api_key

    def say(self, text):
        # call aws sdk
        print(text)