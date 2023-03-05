import os
import openai

os.system('clear')

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

codex = "code-davinci-002"
davinci = "text-davinci-003"
curie = "text-curie-001"

user_input = input("Describe functionality.\n=> ")
language = input("\nPython or JavaScript code? [py|js].\n=> ")
file_name = input("\nName of the file.\n=> ")

if language == "py":

    file_extension = "py"
    code_style = "python"

elif language == "js":

    file_extension = "js"
    code_style = "javascript"

prompt = f"\"\"\"\n{code_style} code to {user_input}\n\"\"\""

response = openai.Completion.create(
  model=davinci,
  prompt=prompt,
  temperature=0,
  max_tokens=2000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

code = response["choices"][0]["text"].strip()

with open(f"{file_name}.{file_extension}", "w") as file:

    file.write(code)

print("\nCode generation complete")