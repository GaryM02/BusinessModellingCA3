import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

from ..models.new_page import NewPage

class ShoppingBasketView(NewPage):
    def __init__(self, *args, **kwargs):
        NewPage.__init__(self, *args, **kwargs)

        # Item Selection
        self.type_var = tb.StringVar()
        self.type_dropdown = tb.Combobox(self, textvariable=self.type_var, values=["Luxury", "Essential", "Gift"])
        self.type_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

        tb.Label(self, text="Select Item Type:").grid(row=0, column=0, padx=10, pady=10, sticky='ew')
        self.quantity_entry = tb.Entry(self)
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

        tb.Label(self, text="Enter Quantity:").grid(row=1, column=0, padx=10, pady=10, sticky='ew')

        # VAT and Total Cost
        self.vat_label = tb.Label(self, text="")
        self.vat_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky='ew')
        self.total_label = tb.Label(self, text="")
        self.total_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky='ew')

        # Buttons
        self.calculate_button = tb.Button(self, text="Calculate", bootstyle=PRIMARY)
        self.calculate_button.grid(row=4, column=0, padx=10, pady=10, sticky='ew')

        self.add_button = tb.Button(self, text="Add to Basket", bootstyle=SUCCESS)
        self.add_button.grid(row=4, column=1, padx=10, pady=10, sticky='ew')

        self.clear_button = tb.Button(self, text="Clear", bootstyle=DANGER)
        self.clear_button.grid(row=4, column=2, padx=10, pady=10, sticky='ew')

        # Basket Display
        self.basket_display = tb.Text(self, height=10, width=50)
        self.basket_display.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky='ew')

        # Configure the grid to adjust the layout dynamically
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

  
