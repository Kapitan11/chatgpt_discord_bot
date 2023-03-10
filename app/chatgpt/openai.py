# The load_dotenv function reads the key-value pairs from a .env file and sets them as environment variables.
from dotenv import load_dotenv
# The os module provides a way of using operating system dependent functionality.
import os
# The openai module provides a Python interface to the OpenAI API.
import openai

# Load environment variables from .env file.
load_dotenv()

# Set OpenAI API key from environment variables.
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define a function that sends a prompt to the GPT model and returns its response.
def chatgpt_response(prompt):
    # Call the OpenAI API to generate a completion based on the prompt.
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=100
    )
    # Extract the text response from the API response dictionary.
    response_dict = response.get("choices")
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0].get("text")
    return prompt_response
