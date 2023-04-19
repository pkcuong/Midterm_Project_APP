from modules.videocard1 import VideoCard
from modules.VCmanager1 import VideoCardManager
from modules.login import Login
import tkinter as tk

def main():
    # Create login window
    login_window = tk.Tk()
    login = Login(login_window)

    # Run login window main loop
    login_window.mainloop()

    # Check if login was successful
    if login.login_successful:
        # Create video card manager window
        root = tk.Tk()
        manager = VideoCardManager(root)

        # Run video card manager window main loop
        root.mainloop()
    else:
        print("Login failed")

if __name__ == "__main__":
    main()
