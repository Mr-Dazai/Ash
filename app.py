#.\venv\Scripts\activate   
import os
from openai import OpenAI
import tkinter as tk
# from tkinter import ttk
from dotenv import load_dotenv

from Chat import ChatApp


def main():
    load_dotenv()
    openai = OpenAI()
    API_KEY = os.getenv("OPENAI_API_KEY")
    openai.api_key = API_KEY
    root = tk.Tk()
    app = ChatApp(root,openai)
    root.mainloop()

if __name__ == '__main__':
    main()
