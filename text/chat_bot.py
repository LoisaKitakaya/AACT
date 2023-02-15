import os
import sys
import time
import openai
from termcolor import colored

from dotenv import load_dotenv
load_dotenv()

def typingOutput(text):

    for characters in text:

        sys.stdout.write(characters)
        sys.stdout.flush()

        time.sleep(0.03)

    print("\n")

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nAI:"
restart_sequence = "\nMe: "

davinci = "text-davinci-003"
curie = "text-curie-001"

pre_exit_text = colored("To exit the program, type", "yellow", attrs=["bold"])
exit_text = colored("'exit'", "red", attrs=["bold"])
post_exit_text = colored("when you are prompted.", "yellow", attrs=["bold"])


print(f"{pre_exit_text} {exit_text} {post_exit_text}\n")

intro = openai.Completion.create(
    model=davinci,
    prompt="Cassiopeia is an AI assistant.\nCassiopeia is part of AACT (a set of programming tools powered by artificial intelligence). AACT stands for AI Application CLI Toolkit. As part of AACT Cassiopeia assists software engineers in their work.\nCassiopeia is helpful, creative, clever, witty, very sarcastic, occasionally cracks programming jokes, and ends every response with an emoji that matches the sentiment of its response.\nThe following is a conversation with Cassiopeia AI assistant.\n\nMe: Hello, who are you?",
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Me:", " AI:"]
)

intro_response = intro['choices'][0]['text'].strip()
formatted_intro = colored(f"{intro_response}", "green", attrs=["bold"])

typingOutput(formatted_intro)

ai_personalization = "Cassiopeia is an AI assistant.\nCassiopeia is part of AACT (a set of programming tools powered by artificial intelligence). AACT stands for AI Application CLI Toolkit. As part of AACT Cassiopeia assists software engineers in their work.\nCassiopeia is helpful, creative, clever, witty, very sarcastic, occasionally cracks programming jokes, and ends every response with an emoji that matches the sentiment of its response.\nThe following is a conversation with Cassiopeia AI assistant."

user_input = input("\nMe: ")

prompt_sequence = f"\nMe: {user_input}"
prompt = f"{ai_personalization}\n{prompt_sequence}"

while True:

    response = openai.Completion.create(
        model=davinci,
        prompt=prompt,
        temperature=0.9,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Me:", " AI:"]
    )

    ai_answer = response['choices'][0]['text'].strip()
    formatted_answer = colored(f"{ai_answer}", "green", attrs=["bold"])

    print("\n")
    typingOutput(formatted_answer)

    prompt += f"\n\n{ai_answer}"

    user_input = input("\nMe: ")

    if user_input == "exit":

        prompt_sequence = f"Me: Alright Cassiopeia, catch your later."

        prompt += f"\n\n{prompt_sequence}"

        break

    prompt_sequence = f"Me: {user_input}"

    prompt += f"\n\n{prompt_sequence}"

outro = openai.Completion.create(
    model=davinci,
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Me:", " AI:"]
)

outro_response = outro['choices'][0]['text'].strip()
formatted_outro = colored(f"{outro_response}", "green", attrs=["bold"])

print("\n")
typingOutput(formatted_outro)