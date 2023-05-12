# GPT Terminal Personas

GPT Terminal Personas is an amazing application that brings AI-powered chatbot conversations to life! Interact with various personas and engage in dynamic and entertaining conversations. To get started, make sure to configure the application by following the instructions below:

## Configuration

Before running the GPT Terminal Personas application, you need to set up the necessary API keys and environment variables. Create a file named `.env` in the project directory and copy the example file `env.example` provided with the following configuration:

```plaintext
# APPLICATION CONFIGURATION
# Set the API keys for the services below
# Copy this file to .env to run

# OpenAI API key to access GPT-3, Whisper, and DALL-E
OPENAI_API_KEY=your_openai_api_key_here

# Eleven Labs AI Natural Voice
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here

# COQUIAI Open Source API KEY
COQUIAI_API_KEY=your_coquiai_api_key_here

# AWS API key to access Polly
AWS_ACCESS_KEY_ID=your_aws_access_key_id_here

# Google Speech to Text
GOOGLE_API_KEY=your_google_api_key_here

# Default timeout on connections
TIMEOUT=30
```

Replace the placeholder values (`your_api_key_here`) with your actual API keys or credentials for each service. The configuration options are described below:

- `OPENAI_API_KEY`: Your API key for OpenAI services, including GPT-3, Whisper, and DALL-E.
- `ELEVENLABS_API_KEY`: Your API key for Eleven Labs AI Natural Voice service.
- `COQUIAI_API_KEY`: Your API key for COQUIAI Open Source service.
- `AWS_ACCESS_KEY_ID`: Your AWS API key ID for accessing AWS Polly service.
- `GOOGLE_API_KEY`: Your API key for Google Speech to Text service.
- `TIMEOUT`: The default timeout duration for connections in seconds.

Make sure to save the `.env` file with the updated configuration before running the application.

## Running the Application

To start the GPT Terminal Personas application, navigate to the project directory and execute the following command:

```shell
python main.py [options] [message]
```

### Options

- `-h`, `--help`: Show the help message and exit.
- `-m`, `--model`: Specify the GPT-3 model to use.
- `-k`, `--key`: Specify the OpenAI API key to use.
- `-v`, `--version`: Show the version of GPT-3 CLI.
- `-l`, `--list-models`: List all available GPT-3 models.
- `-i`, `--instructions`: Set GPT-3 system instructions.

### Examples

- Running the application with a specific model: `python main.py -m model_name`
- Setting the OpenAI API key: `python main.py -k your_api_key`
- Displaying the version: `python main.py -v`
- Listing available GPT-3 models: `python main.py -l`
- Setting GPT-3 system instructions: `python main.py -i`
- Sending a message to GPT-3: `python main.py Hello`

Please note that you can pass a message as an argument to have a conversation with GPT-3 right from the command line.

## Example Environment Configuration

Here's a brief explanation of each configuration option in the `.env` file:

- `OPENAI_API_KEY`: The API key for OpenAI services, allowing access to GPT-3, Whisper, and DALL-E. Make sure to obtain an API key from OpenAI and replace the placeholder value.
- `ELEVENLABS_API_KEY`: The API key for Eleven Labs AI Natural Voice service, which provides natural-sounding AI voices. Obtain an API key from Eleven Labs and replace the placeholder value.

- `COQUIAI_API_KEY`: The API key for COQUIAI Open Source service, an open-source AI platform. Get an API key from COQUIAI and replace the placeholder value.

- `AWS_ACCESS_KEY_ID`: The AWS API key ID for accessing AWS Polly service, which offers text-to-speech capabilities. Replace the placeholder value with your AWS API key ID.

- `GOOGLE_API_KEY`: The API key for Google Speech to Text service, allowing speech recognition capabilities. Obtain an API key from Google and replace the placeholder value.

- `TIMEOUT`: The default timeout duration for connections in seconds. You can adjust this value as per your requirements.

## Contributing

If you have any creative ideas or suggestions to enhance the application, feel free to contribute! We welcome contributions in the form of issues and pull requests on the project's GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE). Enjoy your journey through the world of GPT Terminal Personas, where AI meets creativity!

## Disclaimer

Please note that this application is for demonstration purposes only and does not provide actual access to the mentioned services. Replace the placeholder API keys with your valid API keys to use the application with real services.

Feel free to explore and have fun with GPT Terminal Personas!