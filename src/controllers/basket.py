import tkinter as tk
from tkinter import ttk

class BasketController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.calculate_button.config(command=self.calculate)
        self.view.add_button.config(command=self.add_to_basket)
        self.view.clear_button.config(command=self.clear_selection)

    def calculate(self):
        item_type = self.view.type_var.get()
        quantity = self.view.quantity_entry.get()
        total, vat = self.model.calculate_total(item_type, quantity)
        if total is not None:
            self.view.vat_label.config(text=f"VAT Rate: {vat * 100}%")
            self.view.total_label.config(text=f"Total Cost: €{total:.2f}")
        else:
            self.view.total_label.config(text="Please select item and enter valid quantity.")

    def add_to_basket(self):
        item_type = self.view.type_var.get()
        quantity = self.view.quantity_entry.get()
        total, _ = self.model.calculate_total(item_type, quantity)
        self.model.add_to_basket(item_type, quantity, total)
        self.update_basket_display()

    def update_basket_display(self):
        self.view.basket_display.delete(1.0, tk.END)
        basket_total = self.model.get_basket_total()
        for item in self.model.get_basket_contents():
            self.view.basket_display.insert(tk.END, f"{item[0]} x {item[1]}: €{item[2]:.2f}\n")
        self.view.basket_display.insert(tk.END, f"\nTotal Cost: €{basket_total:.2f}")

    def clear_selection(self):
        self.view.type_var.set('')
        self.view.quantity_entry
