import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ..models.new_page import NewPage

class InventoryView(NewPage):
    def __init__(self, *args, **kwargs):
        NewPage.__init__(self, *args, **kwargs)

        # Item name entry
        ttk.Label(self, text="Enter item name:").pack(side=tk.TOP, fill=tk.X, padx=(10, 10), pady=(10, 5))
        self.name_entry = ttk.Entry(self)
        self.name_entry.pack(side=tk.TOP, fill=tk.X, padx=(10, 10))

        # Item type combobox
        ttk.Label(self, text="Enter item type:").pack(side=tk.TOP, fill=tk.X, padx=(10, 10), pady=(5, 5))
        self.type_var = ttk.StringVar()
        self.type_dropdown = ttk.Combobox(self, textvariable=self.type_var, values=["luxury", "essential", "gift"])
        self.type_dropdown.pack(side=tk.TOP, fill=tk.X, padx=(10, 10))

        # Expiration date entry
        ttk.Label(self, text="Enter expiration date (YYYY-MM-DD):").pack(side=tk.TOP, fill=tk.X, padx=(10, 10), pady=(5, 5))
        self.date_entry = ttk.Entry(self)
        self.date_entry.pack(side=tk.TOP, fill=tk.X, padx=(10, 10))

        # Item Length Entry
        ttk.Label(self, text="Enter item length (cm):").pack(side=tk.TOP, fill=tk.X, padx=(10, 10), pady=(5, 5))
        self.length_entry = ttk.Entry(self)
        self.length_entry.pack(side=tk.TOP, fill=tk.X, padx=(10, 10))

        # Item Width Entry
        ttk.Label(self, text="Enter item width (cm):").pack(side=tk.TOP, fill=tk.X, padx=(10, 10), pady=(5, 5))
        self.width_entry = ttk.Entry(self)
        self.width_entry.pack(side=tk.TOP, fill=tk.X, padx=(10, 10))

        # Item Height Entry
        ttk.Label(self, text="Enter item height (cm):").pack(side=tk.TOP, fill=tk.X, padx=(10, 10), pady=(5, 5))
        self.height_entry = ttk.Entry(self)
        self.height_entry.pack(side=tk.TOP, fill=tk.X, padx=(10, 10))

        # Item Weight Entry
        ttk.Label(self, text="Enter item weight (kg):").pack(side=tk.TOP, fill=tk.X, padx=(10, 10), pady=(5, 5))
        self.weight_entry = ttk.Entry(self)
        self.weight_entry.pack(side=tk.TOP, fill=tk.X, padx=(10, 10))

        # Add item button
        ttk.Button(self, text="Add Item", command=self.on_add_click, bootstyle=PRIMARY).pack(side=tk.TOP, pady=(10, 0))

        # Result label
        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(side=tk.TOP, pady=(5, 0), padx=(10, 10))

        # View Items Frame
        self.view_frame = ttk.Frame(self)
        self.view_frame.pack(padx=10, pady=10)

        # Listbox for items
        self.listbox = tk.Listbox(self.view_frame)
        self.listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Refresh and delete buttons
        ttk.Button(self.view_frame, text="Refresh List", command=self.on_view_click, bootstyle=INFO).pack(side=tk.LEFT, padx=(0, 5), pady=5)
        ttk.Button(self.view_frame, text="Delete Selected Item", command=self.on_delete_click, bootstyle=DANGER).pack(side=tk.RIGHT, padx=(5, 0), pady=5)


    def set_on_add(self, on_add):
        self.on_add = on_add
    
    def set_on_view(self, on_view):
        self.on_view = on_view
    
    def set_on_delete(self, on_delete):
        self.on_delete = on_delete

    def on_add_click(self):
        self.on_add(self.name_entry.get(), self.type_var.get(), self.date_entry.get(), self.length_entry.get(), self.width_entry.get(), self.height_entry.get(), self.weight_entry.get())

    def on_view_click(self):
        self.on_view()

    def on_delete_click(self):
        selected = self.listbox.get(tk.ANCHOR)
        if selected:
            print(selected)
            item_id = selected.split(' ')[1]
            self.on_delete(item_id)

    def show_items(self, items):
        self.listbox.delete(0, tk.END)
        for item in items:
            self.listbox.insert(tk.END, f"{item.__str__()}")

    def show_result(self, text):
        self.result_label.config(text=text)
