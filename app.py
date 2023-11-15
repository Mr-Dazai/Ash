import os
from openai import OpenAI

from dotenv import load_dotenv

def main():
    load_dotenv()
    openai=OpenAI()
    API_KEY = os.getenv("OPENAI_API_KEY")
    openai.api_key=API_KEY
    chat_log=[]
    while True:
        user_message=input()
        if user_message.lower()=='quit':
            break
        else:
            chat_log.append({"role":"user","content":user_message})
            responce= openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=chat_log
            )
            message_content = responce.choices[0].message.content
            print(message_content)
            chat_log.append({"role":"system","content":message_content})

    # responce= openai.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role":"user","content":"What is Python?"}
    #     ]
    # )
    # message_content = responce.choices[0].message.content
    # print(message_content)


if __name__=='__main__':
    main()