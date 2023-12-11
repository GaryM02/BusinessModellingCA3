import tkinter as tk
import ttkbootstrap as ttk

class NewPage(ttk.Frame):
    def __init__(self, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()