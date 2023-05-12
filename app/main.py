import os
import argparse
import openai
import sys
from dotenv import load_dotenv
from app.character import *
from app.ai import *
# from app.presentation import app
from app.speech.coquiai_speech import CoquiaiSpeech
from app.speech.sound import Sound


def main():
    coaquiai = CoquiaiSpeech()
    sound = Sound()
    # coaquiai.list_speakers()
    # audio_url = coaquiai.say('Something new here for me' * 10)
    # coaquiai.download_file_from_url(audio_url)
    # sound.play_file('sample.wav')
    # sys.exit(0)
    print('getenv ' + os.getenv('ELEVENLABS_API_KEY') or 'not found')
    character = Character()
    character.select(personas)

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
        gpt3 = GPT3()
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
            gpt3.instructions(character.get_description())
        elif args.message:
            gpt3.prompt(args.message)
        else:
            print(f'The arg {args.key} is not supported yet')
    except Exception as e:
        print('Error: ', e)

    print("Welcome to the GPT-3 chatbot!")
    print("Type 'exit' to quit.\n")
    print('Setting instructions')
    instruction = "Act as a character to the user, been very real and related to the persona attributes, here is your character: " + \
        character.get_description()
    gpt3.instructions(instruction)

    message = ''
    while message != 'exit':
        message = input("You: ")
        response = gpt3.prompt(message)
        print(f'\n{response}\n\n')
        audio_url = coaquiai.say(response)
        coaquiai.download_file_from_url(audio_url)
        sound.play_file('sample.wav')


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


if __name__ == '__main__':
    load_dotenv()
    main()
