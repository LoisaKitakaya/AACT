import os
import openai

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nAI:"
restart_sequence = "\nMe: "

davinci = "text-davinci-003"
curie = "text-curie-001"

print("To exit the program, type 'exit' when you are prompted.\n\n")

intro = openai.Completion.create(
    model=davinci,
    prompt="AACT is an AI assistant.\nAACT stands for (AI Application CLI Toolkit).\nAACT is helpful, creative, clever, witty, very sarcastic, and ends every response with an emoji that matches the sentiment of its response.\nThe following is a conversation with AACT AI assistant.\n\nMe: Hello, who are you?",
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Me:", " AI:"]
)

print(intro['choices'][0]['text'].strip())

ai_personalization = "AACT is an AI assistant. AACT stands for (AI Application CLI Toolkit). AACT is helpful, creative, clever, witty, very sarcastic, and ends every response with an emoji that matches the sentiment of its response. The following is a conversation with AACT AI assistant."

user_input = input("\nMe: ")

prompt_sequence = f"\nMe: {user_input}"
prompt = f"{ai_personalization}\n{prompt_sequence}"

while True:

    response = openai.Completion.create(
        model=davinci,
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Me:", " AI:"]
    )

    ai_answer = response['choices'][0]['text'].strip()

    print(f"\n{ai_answer}")

    prompt += f"\n\n{ai_answer}"

    user_input = input("\nMe: ")

    if user_input == "exit":

        prompt_sequence = f"Me: Goodbye. Thanks for your time. Catch your later."

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

print(f"\n{outro['choices'][0]['text'].strip()}\n")