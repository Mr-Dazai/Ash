import os
from openai import OpenAI

from dotenv import load_dotenv

def main():
    load_dotenv()
    openai=OpenAI()
    API_KEY = os.getenv("OPENAI_API_KEY")
    openai.api_key=API_KEY
    responce= openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"user","content":"What is Python?"}
        ]
    )
    message_content = responce.choices[0].message.content
    print(message_content)


if __name__=='__main__':
    main()