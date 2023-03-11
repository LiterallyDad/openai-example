import os

from dotenv import load_dotenv
import openai

load_dotenv()  # take environment variables from .env.

# Set the API key
api_key = os.getenv("OPENAI_API_KEY")
print(api_key)
openai.api_key = api_key
# Use the ChatGPT model to generate text
model_engine = "text-davinci-002"
prompt = "Hello, how are you today?"
completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.7)
message = completion.choices[0].text
print(message)