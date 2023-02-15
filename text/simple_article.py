import os
import sys
import openai

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

davinci = "text-davinci-003"
curie = "text-curie-001"

title = sys.argv[1]
my_doc = f"{title} \n\n"

prompt = f"In numbered point form generate key points to be addressed in an article with the title '{title}'."

key_points = openai.Completion.create(
  model=davinci,
  prompt=prompt,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
key_points_response = key_points['choices'][0]['text'].strip()
key_points_list = key_points_response.split('\n')

my_doc = my_doc + f"Key points highlighted in this article \n\n{key_points_response} \n\n"

for point in key_points_list:
    
    section_prompt = f"In several paragraphs, discuss the following topic '{point}'"

    section_paragraph = openai.Completion.create(
        model=davinci,
        prompt=section_prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    section_paragraph_response = section_paragraph['choices'][0]['text'].strip()
    paragraph = f"{point} \n\n{section_paragraph_response} \n"
    print(paragraph)

    my_doc = my_doc + paragraph + "\n"

with open(f"{title}.txt", "w") as file:

    file.write(my_doc)