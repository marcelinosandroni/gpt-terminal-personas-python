import requests
from app.speech.speech import Speech
import os
import json
import concurrent.futures


class CoquiaiSpeech(Speech):
    _list_speakers_url = 'https://app.coqui.ai/api/v2/speakers'
    _create_sample_url = 'https://app.coqui.ai/api/v2/samples'
    _API_KEY: str
    _default_speaker_id = 'cb4f835e-7f61-4b8c-a0f6-f059bbf6f583'

    def __init__(self):
        self._API_KEY = os.getenv('COQUIAI_API_KEY')

    def list_speakers(self):
        response = requests.get(self._list_speakers_url, headers={
                                'Authorization': 'Bearer ' + self._API_KEY,
                                'Content-Type': 'application/json'})
        print(type(response.json()))
        print(response.json())
        print(json.dumps(response.json(), indent=4, sort_keys=True))
        print(type(json.dumps(response.json(), indent=4, sort_keys=True)))

    def split_text(self, text):
        if len(text) > 250:
            print(
                f'WARNING: text is too long, truncating to 250 characters. (was {len(text)} characters)')
            texts = []
            index = 0
            splited = text.split(',')
            print(splited)
            for sentence in text.split(','):
                print(texts)
                if not len(texts) or len(texts[index]) + len(sentence) < 250:
                    texts[index] += sentence
                else:
                    index += 1
                    texts.append(sentence)
                    print(len(texts))

            return texts
        else:
            return [text]

    def say(self, text):
        if len(text) > 250:
            texts = self.split_text(text)

            with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
                future_tasks = {executor.submit(
                    self.say, text): text for text in texts}
                results = []

                for future in concurrent.futures.as_completed(future_tasks):
                    results.append(future.result())

                return results
        data = {
            'speaker_id': self._default_speaker_id,
            'emotion': 'Neutral',
            'name': 'anything',
            'text': text,
            'speed': 1
        }
        response = requests.post(self._create_sample_url, headers={
            'Authorization': 'Bearer ' + self._API_KEY}, data=data)

        # verify errors
        try:
            response.raise_for_status()
            # print(response.json())
            return response.json().get('audio_url')
        except requests.exceptions.HTTPError as error:
            print(error)
            return

    def download_file_from_url(self, url):
        response = requests.get(url)
        try:
            response.raise_for_status()
            with open('sample.wav', 'wb') as file:
                file.write(response.content)
            return response
        except requests.exceptions.HTTPError as error:
            print(error)
            return
