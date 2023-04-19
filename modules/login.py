import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from .VCmanager1 import VideoCardManager
class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("800x400")
        self.login_successful = False
        
        # Create username and password labels and entries
        self.username_label = ttk.Label(self.master, text="Username:")
        self.username_entry = ttk.Entry(self.master)
        self.password_label = ttk.Label(self.master, text="Password:")
        self.password_entry = ttk.Entry(self.master, show="*")
        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        
        # Create login button
        self.login_button = ttk.Button(self.master, text="Login", command=self.login)
        self.login_button.pack()
        
    def login(self):
        # Get username and password from entries
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if username and password are valid
        with open('admin.txt') as f:
            for line in f:
                if line.startswith(f'Username: {username};'):
                    if f'Password: {password}' in line:
                        self.login_successful = True
                        self.master.destroy()
                        return
                    else:
                        messagebox.showerror("Invalid password", "The password you entered is invalid")
                        return

            messagebox.showerror("Invalid username", "The username you entered is invalid")



