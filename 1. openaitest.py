from openai import OpenAI
from colorama import init
from colorama import Fore, Back, Style
import time


init()

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="123",
)

time.sleep(5)

prompts = [
    "what is ROI in the context of finance, provide a worked example?",
    "define the efficient frontier in the context of finance",
    "what is glass stegal?",
    "how does derivative pricing work?",
]


for prompt in prompts:
    print(Fore.LIGHTMAGENTA_EX + prompt, end="\n")
    response = client.chat.completions.create(
        model="llama.cpp/models/mixtral-8x7b-instruct-v0.1.Q2_K.gguf",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        stream=True,
        max_tokens=20,
    )
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            print(
                Fore.LIGHTBLUE_EX + chunk.choices[0].delta.content,
                end="",
                flush=True,
            )
    print("\n")
