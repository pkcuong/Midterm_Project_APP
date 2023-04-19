
from .videocard1 import VideoCard
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def read_videocards_from_file(filename):
    videocards = []
    with open(filename, 'r') as f:
        for line in f:
            fields = line.strip().split(', ')
            name = fields[0][6:]  # Remove 'Name: ' prefix
            brand = fields[1][7:]  # Remove 'Brand: ' prefix
            memory = int(fields[2][8:])  # Remove 'Memory: ' prefix and convert to int
            price = float(fields[3][7:])  # Remove 'Price: ' prefix and convert to float
            videocard = VideoCard(name, brand, memory, price)
            videocards.append(videocard)
    return videocards

class VideoCardManager:
    def __init__(self,master):
        self.master = master
        self.master.title("Videocard Manager")
        self.master.geometry("900x540")
        
        self.videocards = []
        # create GUI elements
        self.name_label = ttk.Label(master, text="Name:")
        self.name_entry = ttk.Entry(master)
        self.brand_label = ttk.Label(master, text="Brand:")
        self.brand_entry = ttk.Entry(master)
        self.memory_label = ttk.Label(master, text="Memory (GB):")
        self.memory_entry = ttk.Entry(master)
        self.price_label = ttk.Label(master, text="Price ($):")
        self.price_entry = ttk.Entry(master)
        self.add_button = ttk.Button(master, text="Add", command=self.add_videocard)
        self.list_button = ttk.Button(master, text="List", command=self.list_videocards)
        self.sort_button = ttk.Button(master, text="Sort (ascending order) ", command=self.sort_videocards)
        self.search_button = ttk.Button(master, text="Search", command=self.search_videocards)
        self.clear_button = ttk.Button(master, text="Clear", command=self.clear_entries)
        self.quit_button = ttk.Button(master, text="Quit", command=master.quit)
        
        # layout GUI elements
        self.name_label.grid(row=0, column=0, padx=60, pady=20)
        self.name_entry.grid(row=0, column=1, padx=60, pady=20)
        self.brand_label.grid(row=1, column=0, padx=60, pady=20)
        self.brand_entry.grid(row=1, column=1, padx=60, pady=20)
        self.memory_label.grid(row=2, column=0, padx=60, pady=20)
        self.memory_entry.grid(row=2, column=1, padx=60, pady=20)
        self.price_label.grid(row=3, column=0, padx=60, pady=20)
        self.price_entry.grid(row=3, column=1, padx=60, pady=20)
        self.add_button.grid(row=0, column=2, padx=60, pady=20)
        self.list_button.grid(row=0, column=3, padx=60, pady=20)
        self.sort_button.grid(row=1, column=2, padx=60, pady=20)
        self.search_button.grid(row=1, column=3, padx=60, pady=20)
        self.clear_button.grid(row=2, column=2, padx=60, pady=20)
        self.quit_button.grid(row=2, column=3, padx=60, pady=20)
        
        # set focus to name entry
        self.name_entry.focus()
        self.videocards = read_videocards_from_file('videocards1.txt')
    
    def add_videocard(self):

        name = self.name_entry.get().strip()
        brand = self.brand_entry.get().strip()
        memory = int(self.memory_entry.get().strip())
        price = float(self.price_entry.get().strip())
        videocard = VideoCard(name, brand, memory, price)
        self.videocards.append(videocard)
        with open('videocards1.txt', 'a') as f:
            f.write(f'Name: {name}, Brand: {brand}, Memory: {memory}, Price: {price}\n')
        messagebox.showinfo("Success", "Video card added successfully.")
  
    def list_videocards(self,*videocards):
        if self.videocards:
            message = "\n".join(str(videocard) for videocard in self.videocards)
        else:
            message = "No videocards found."
        self.display_message(message)

    def sort_videocards(self):
            self.videocards.sort(key=lambda videocard: videocard.price)
            self.list_videocards()

    def search_videocards(self):
        name = self.name_entry.get().strip()
        brand = self.brand_entry.get().strip()
        try:
            memory = int(self.memory_entry.get().strip())
        except ValueError:
            memory = None
        try:
            price = float(self.price_entry.get().strip())
        except ValueError:
            price = None
        matches = []
        for videocard in self.videocards:
            if name and name.lower() not in videocard.name.lower():
                continue
            if brand and brand.lower() not in videocard.brand.lower():
                continue
            if memory is not None and videocard.memory <= memory:
                continue
            if price is not None and videocard.price > price:
                continue
            matches.append(videocard)
        if matches:
            message = "\n".join(str(videocard) for videocard in matches)
        else:
            message = "No videocards found."
        self.display_message(message)
   
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.brand_entry.delete(0, tk.END)
        self.memory_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.name_entry.focus()
    
    def display_message(self, message):
        messagebox.showinfo("Videocard Manager", message)   
    

