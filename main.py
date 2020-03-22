import requests
import os
import openai
import argparse

class OpenAiConnector:
    def __init__ (self, api_key, openai):
        self._api_key = api_key
        openai.api_key = self._api_key

class OpenAiModel:
    _API_KEY_LENGTH = 51
    _OPENAI_CONNECTOR = None

    def __init__(self, openai_connector):
        self._OPENAI_CONNECTOR = openai_connector
        self._api_key = os.getenv("OPENAI_API_KEY")

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def set_api_key(self, value):
        if not isinstance(value, str):
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
        return self._OPENAI_CONNECTOR.Models.list()


class GPT3(OpenAiModel):
    _MODEL_NAME = 'gpt-3.5-turbo'
    _INSTRUCTIONS: str = None

    def __init__(self, openai_connector):
        super().__init__(openai_connector)

    @property
    def name(self):
        return self._MODEL_NAME
    
    def instructions(self, instructions):
        self._INSTRUCTIONS = instructions
    
    def prompt(self, message, role='user'):
        response = self._OPENAI_CONNECTOR.ChatCompletion.create(
            model=self._MODEL_NAME, messages=[{'role': role, 'content': message}])
        return response['choices'][0]['message']['content']


def main():
    parser = argparse.ArgumentParser()
    parser.set_defaults(func=main, help=help, )
    parser.add_argument('-m', '--model', help='Specify the GPT-3 model to use')
    parser.add_argument(
        '-k', '--key', help='Specify the OpenAI API key to use')
    parser.add_argument('-v', '--version',
                        help='Show the version of GPT-3 CLI')
    parser.add_argument('-l', '--list-models',
                        help='List all available models')
    parser.add_argument('-i', '--instructions',
                        help='Set GPT-3 system instructions')
    parser.add_argument('message', nargs='?', help='Message to send to GPT-3')

    try:
        args = parser.parse_args()
        gpt3 = GPT3(openai)
        match args.key:
            case args.model: gpt3.models()
        
        if args.model:
            gpt3.models()
        elif args.key:
            gpt3.api_key = args.key
        elif args.version:
            print('GPT-3 CLI version 0.1.0')
        elif args.list_models:
            gpt3.models()
        elif args.instructions:
            gpt3.instructions(args.instructions)
        elif args.message:
            gpt3.prompt(args.message)
        else:
            print(f'The arg {args.key} is not supported yet')
    except Exception as e:
        print('Error: ', e)

    print("Welcome to the GPT-3 chatbot!")
    print("Type 'exit' to quit.\n")
    message = ''
    while message != 'exit':
        message = input("You: ")
        response = gpt3.prompt(message)
        print(f'GPT-3: {response}\n\n')


def help():
    print('GPT-3 CLI help')
    print('Usage: gpt3 [options] [message]')
    print('Options:')
    print('  -h, --help\t\tShow this help message and exit')
    print('  -m, --model\t\tSpecify the GPT-3 model to use')
    print('  -k, --key\t\tSpecify the OpenAI API key to use')
    print('  -v, --version\t\tShow the version of GPT-3 CLI')
    print('  -l, --list-models\tList all available GPT-3 models')
    print('  -i, --instructions \t\tSet GPT-3 system instructions')


def set_model(model_name):


if __name__ == '__main__':
    main()
