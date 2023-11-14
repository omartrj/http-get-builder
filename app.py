import tkinter as tk
from tkinter import ttk
import requests
from styles import FRAME_BACKGROUND, APP_BACKGROUND

class HttpRequestBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("HTTP Request Builder")
        self.root.configure(bg=APP_BACKGROUND)

        self.style = ttk.Style()
        self.style.configure('Dark.TFrame', background=FRAME_BACKGROUND)

        self.create_widgets()

    def send_request(self):
        base_url = self.entry_base_url.get()
        if not base_url:
            self.show_error("Please enter a Base URL.")
            return

        params = {}
        for param_entry in self.param_entries:
            param_name = param_entry[1].get().strip()
            param_value = param_entry[2].get().strip() 
            if param_name and param_value:
                params[param_name] = param_value

        try:
            response = requests.get(base_url, params=params)

            # Clear the response text box
            self.response_text.delete(1.0, tk.END)  

            # Highlight HTTP status code
            status_code_text = f"Status Code: {response.status_code}\n\n"
            self.response_text.insert(tk.END, status_code_text)
            self.response_text.tag_add("status_code", "1.0", "1.13")
            self.response_text.tag_config("status_code", foreground="green")

            # Insert the response content
            self.response_text.insert(tk.END, response.text)
        except requests.RequestException as e:
            self.response_text.delete(1.0, tk.END)
            self.response_text.insert(tk.END, f"Request Error: {e}")

    def add_param_entry(self):
        param_frame = ttk.Frame(self.param_container, style='Dark.TFrame')
        param_frame.grid(column=0, columnspan=3, pady=2)

        param_name_entry = ttk.Entry(param_frame)
        param_name_entry.grid(row=0, column=0, padx=5)
        param_value_entry = ttk.Entry(param_frame)
        param_value_entry.grid(row=0, column=1, padx=5)
        delete_button = ttk.Button(param_frame, text='x', command=lambda frame=param_frame: self.delete_param(frame))
        delete_button.grid(row=0, column=2, padx=5)

        self.param_entries.append((param_frame, param_name_entry, param_value_entry))

    def delete_param(self, param_frame):
        for entry in self.param_entries:
            if entry[0] == param_frame:
                entry[0].destroy()
                self.param_entries.remove(entry)
                break

    def show_error(self, message):
        self.error_label.config(text=message)

    def create_widgets(self):
        ttk.Label(self.root, text="Enter Base URL:", foreground='white', background='#333333').pack()
        self.entry_base_url = ttk.Entry(self.root, width=50)
        self.entry_base_url.pack()

        self.error_label = ttk.Label(self.root, text="", foreground="red", background='#333333')
        self.error_label.pack()

        self.param_container = ttk.Frame(self.root, style='Dark.TFrame')
        self.param_container.pack()

        name_label = ttk.Label(self.param_container, text="Name", foreground='white', background='#444444')
        name_label.grid(row=0, column=0, padx=5)
        value_label = ttk.Label(self.param_container, text="Value", foreground='white', background='#444444')
        value_label.grid(row=0, column=1, padx=5)

        self.param_entries = []
        self.add_param_entry()

        ttk.Button(self.root, text="Add Parameter", command=self.add_param_entry).pack()
        ttk.Button(self.root, text="Send Request", command=self.send_request).pack()

        ttk.Label(self.root, text="Response:", foreground='white', background='#333333').pack()
        self.response_text = tk.Text(self.root, height=20, width=80)
        self.response_text.pack()
