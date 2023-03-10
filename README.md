# Discord Chatbot powered by OpenAI API

Quick implementation of a Discord chatbot powered by OpenAI API.


## Installation

You can create a virtual environment with the [Anaconda Python distribution](https://www.anaconda.com/products/distribution) and activate it.

```sh
conda create -n chatbot 
conda activate chatbot
```

Next, you need to clone the repository and install  all necessary Python packages for your own Discord chatbot.

```sh
git clone https://github.com/Kapitan11/chatgpt_discord_bot.git
cd chatgpt_discord_bot
pip install -r requirements.txt
```

Finally, you need to create a `.env` file to store the required API keys with the following content inside:

```sh
DISCORD_TOKEN = < your Discord API token >
OPENAI_API_KEY = < your OpenAI API key >
```
If you're not sure where or how to get the Discord Bot token I advice you read this great tutorial [tutorial by WRITEBOTS](https://www.writebots.com/discord-bot-token/). 
The same goes for OpenAI API key, here's the [tutorial by Richard Devine](https://www.windowscentral.com/software-apps/how-to-get-an-openai-api-key).

## Usage

Now activate your bot on the Discord server.

```sh
python run.py
```
And voile! Your own chatbot is up and running. To interact with it, go to your server where you enabled your bot and use commands `/ai`, `/chatbot` or `/chatgpt` and write your prompt like this:

![MIGHTY PROMPT](assets/images/prompt_example.png?raw=true)


## Credits

The code was written following the following [tutorial](https://www.youtube.com/watch?v=wdgVv4UP08c). 