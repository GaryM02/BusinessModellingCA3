
import tkinter as tk
from ..models.new_page import NewPage
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class PackingView(NewPage):
    def __init__(self, *args, **kwargs):
        NewPage.__init__(self, *args, **kwargs)

        # Box Weight
        ttk.Label(self, text="Box Weight (kg):").pack(padx=10, pady=(10, 5))
        self.box_weight_entry = ttk.Entry(self)
        self.box_weight_entry.pack(padx=10, fill='x')

        # Box Width
        ttk.Label(self, text="Box Width (cm):").pack(padx=10, pady=(10, 5))
        self.box_width_entry = ttk.Entry(self)
        self.box_width_entry.pack(padx=10, fill='x')

        # Box Height
        ttk.Label(self, text="Box Height (cm):").pack(padx=10, pady=(10, 5))
        self.box_height_entry = ttk.Entry(self)
        self.box_height_entry.pack(padx=10, fill='x')

        # Box Depth
        ttk.Label(self, text="Box Depth (cm):").pack(padx=10, pady=(10, 5))
        self.box_length_entry = ttk.Entry(self)
        self.box_length_entry.pack(padx=10, fill='x')

       
        self.submit_button = ttk.Button(self, text="Add Box", command=self.on_click_add, bootstyle=PRIMARY)
        self.submit_button.pack(pady=10)
        # Result label
        self.box_label = ttk.Label(self, text="")
        self.box_label.pack(side=tk.TOP, pady=(5, 0), padx=(10, 10))


        # View Items Frame
        self.view_frame = ttk.Frame(self)
        self.view_frame.pack(padx=10, pady=10)
        # Result label
        self.result_label = ttk.Label(self.view_frame, text="")
        self.result_label.pack(pady=(5, 0), padx=(10, 10))
       
        self.show_button = ttk.Button(self.view_frame, text="Show Items In Iventory", command=self.on_click_show, bootstyle=PRIMARY)
        self.show_button.pack(pady=10)
        # Listbox for items
        self.listbox = tk.Listbox(self.view_frame)
        self.listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.calculate_button = ttk.Button(self.view_frame, text="Calculate Boxes Needed", command=self.on_click_calculate, bootstyle=PRIMARY)
        self.calculate_button.pack(pady=10)

        # Result label
        self.calc_result_label = ttk.Label(self.view_frame, text="")
        self.calc_result_label.pack(pady=(5, 0), padx=(10, 10))

# calculate volume of the box and using this calculation we can get the volume of all the items and calculate how many boxes are needed to pack the items
# we will also take weight into consideration and make sure that the box is not over the weight limit
    
    def show_result(self, text):
        self.result_label.config(text=text)
    
    def show_calculated_result(self, text):
        self.calc_result_label.config(text=text)

    def show_box(self, text):
        self.box_label.config(text=text)

    def envoke_retrieval(self, func):
        self.retrival_function = func

    def show_items(self, items):
        self.listbox.delete(0, tk.END)
        for item in items:
            self.listbox.insert(tk.END, f"{item.__str__()}")

    def set_on_view(self, on_view):
        self.on_view = on_view

    def set_on_add(self, on_add):
        self.on_add = on_add

    def set_calculate_boxes_needed(self, calculate_boxes_needed):
        self.calculate_boxes_needed = calculate_boxes_needed

    def on_click_show(self):
        self.on_view()

    def on_click_add(self):
        self.on_add()

    def on_click_calculate(self):
        self.calculate_boxes_needed()