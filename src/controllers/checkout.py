import tkinter as tk
from tkinter import ttk 

class ChangeCalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def calculate_change(self):
        try:
            total_cost = float(self.view.total_cost_entry.get())
            amount_paid = float(self.view.amount_paid_entry.get())
            change_distribution, message = self.model.calculate_change(total_cost, amount_paid)

            if change_distribution is None:
                self.view.result_label.config(text=message)
            else:
                result_text = "Change breakdown:\n" + "\n".join(f"{key}€: {value}" for key, value in change_distribution.items())
                self.view.result_label.config(text=result_text)
        except ValueError:
            self.view.result_label.config(text="Invalid input. Please enter numeric values.")

    def clear_fields(self):
        self.view.total_cost_entry.delete(0, tk.END)
        self.view.amount_paid_entry.delete(0, tk.END)
        self.view.result_label.config(text="")
