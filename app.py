#.\venv\Scripts\activate   
import os
from openai import OpenAI
import tkinter as tk
from tkinter import ttk
from dotenv import load_dotenv

def main():
    load_dotenv()
    openai = OpenAI()
    API_KEY = os.getenv("OPENAI_API_KEY")
    openai.api_key = API_KEY
    chat_log = []

    def search():
        query = search_var.get()
        text=("User: "+query)
        print(text)
        results.insert("", tk.END, values=(text,))
        if query:
            chat_log.append({"role": "user", "content": query})
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=chat_log
            )
            message_content = ("OpenAI: "+response.choices[0].message.content)
            print(message_content)
            results.insert("", tk.END, values=(message_content,))
            chat_log.append({"role":"system","content":message_content})

    root = tk.Tk()
    root.title("Chat GPT")

    search_var = tk.StringVar()
    search_box = ttk.Entry(root, textvariable=search_var)
    search_box.pack(padx=10, pady=10, fill='x')

    # search button
    search_button = ttk.Button(root, text="Send", command=search)
    search_button.pack(padx=10, pady=10)

    results = ttk.Treeview(root, columns=('Chat'))
    results.heading('Chat', text='Chat')
    results['show'] = 'headings'
    results.pack(padx=10, pady=10, fill='both', expand=True)

    root.mainloop()

if __name__ == '__main__':
    main()
