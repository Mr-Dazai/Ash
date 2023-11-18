import tkinter as tk
from tkinter import ttk


class ChatApp:
    def __init__(self,root,openai): 
        self.root=root
        self.openai = openai
        self.create_GUI()
        self.chat_log = []
    
    def create_GUI(self):
        self.root.title("Chat GPT")

        search_var = tk.StringVar()
        search_box = ttk.Entry(self.root, textvariable=search_var)
        search_box.pack(padx=10, pady=10, fill='x')

        # search button
        search_button = ttk.Button(self.root, text="Send", command=lambda:self.search(search_var))
        search_button.pack(padx=10, pady=10)

        self.results = ttk.Treeview(self.root, columns=('Chat'))
        self.results.heading('Chat', text='Chat')
        self.results['show'] = 'headings'
        self.results.pack(padx=10, pady=10, fill='both', expand=True)
    
    def search(self,search_var):
        query = search_var.get()
        text=("User: "+query)
        print(text)
        self.results.insert("", tk.END, values=(text,))
        if query:
            self.chat_log.append({"role": "user", "content": query})
            response =self.openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=self.chat_log
            )
            message_content = ("OpenAI: "+response.choices[0].message.content)
            print(message_content)
            self.results.insert("", tk.END, values=(message_content,))
            self.chat_log.append({"role":"system","content":message_content})
