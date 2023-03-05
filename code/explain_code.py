import os
import sys
import time
import openai
from termcolor import colored

os.system('clear')

from dotenv import load_dotenv
load_dotenv()

def typingOutput(text):

    for characters in text:

        sys.stdout.write(characters)
        sys.stdout.flush()

        time.sleep(0.03)

    print("\n")

openai.api_key = os.getenv("OPENAI_API_KEY")

codex = "code-davinci-002"
davinci = "text-davinci-003"
curie = "text-curie-001"

file_path = sys.argv[1]

with open(str(file_path), "r") as file:

    code = file.read()

prompt = f"\"\"\"\n{code}\n\"\"\"\n\nExplain the code in step by step format"

response = openai.Completion.create(
  model=davinci,
  prompt=prompt,
  temperature=0.7,
  max_tokens=2000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

explanation = response["choices"][0]["text"].strip()
formatted_response = colored(f"{explanation}", "green", attrs=["bold"])

print("\n")
typingOutput(formatted_response)