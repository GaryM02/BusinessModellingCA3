import tkinter as tk
from src.views.main_view import MainView
import ttkbootstrap as ttk



if __name__ == "__main__":
    root = ttk.Window(themename="darkly")
    main = MainView(root)
    root.title("Tkinter Navbar")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    print(screen_width, screen_height)
    root.geometry(f"{screen_width//2}x{screen_height}+850+50")
    root.mainloop()


