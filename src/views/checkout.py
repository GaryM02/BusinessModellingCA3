from ..models.new_page import NewPage
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class ChangeCalculatorView(NewPage):
    def __init__(self, *args, **kwargs):
        NewPage.__init__(self, *args, **kwargs)

        # Total Cost Entry
        ttk.Label(self, text="Total Cost (€):").pack(side=tk.TOP, fill=tk.X, pady=(0, 5))
        self.total_cost_entry = ttk.Entry(self)
        self.total_cost_entry.pack(side=tk.TOP, fill=tk.X)

        # Amount Paid Entry
        ttk.Label(self, text="Amount Paid (€):").pack(side=tk.TOP, fill=tk.X, pady=(5, 5))
        self.amount_paid_entry = ttk.Entry(self)
        self.amount_paid_entry.pack(side=tk.TOP, fill=tk.X)

        # Buttons Frame
        button_frame = ttk.Frame(self)
        button_frame.pack(padx=10, pady=10, fill=tk.X)

        # Calculate Change Button
        ttk.Button(button_frame, text="Calculate Change", command=self.calculate_change, bootstyle=PRIMARY).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

        # Clear Button
        ttk.Button(button_frame, text="Clear", command=self.clear_fields, bootstyle=DANGER).pack(side=tk.LEFT, expand=True, fill=tk.X)

        # Result Label
        self.result_label = ttk.Label(self, text="", bootstyle=SECONDARY)
        self.result_label.pack(padx=10, pady=10, fill=tk.X)


    def set_calculate_change(self, calculate_change):
        self.calculate_change = calculate_change
    
    def set_clear_fields(self, clear_fields):
        self.clear_fields = clear_fields

    def calculate_change(self):
        self.calculate_change()

    def clear_fields(self):
        self.clear_fields()
