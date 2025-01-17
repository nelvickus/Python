import requests
import tkinter as tk
from tkinter import messagebox
import json

def get_repo_data(repo_name):
    url = f'https://api.github.com/repos/{repo_name}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        repo_info = {
            'company': None,
            'created_at': data.get('created_at'),
            'email': None,
            'id': data.get('id'),
            'name': data.get('name'),
            'url': data.get('url')
        }
        return repo_info
    else:
        messagebox.showerror("Error", "Repository not found!")

def on_button_click():
    repo_name = entry.get()
    repo_data = get_repo_data(repo_name)
    
    if repo_data:
        with open(f"{repo_name.replace('/', '_')}_info.json", 'w') as json_file:
            json.dump(repo_data, json_file, indent=4)
        messagebox.showinfo("Success", "Data saved successfully!")


root = tk.Tk()
root.title("GitHub Repo Info")

label = tk.Label(root, text="Enter Repository Name (owner/repo):")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Get Repo Data", command=on_button_click)
button.pack()

root.mainloop()
