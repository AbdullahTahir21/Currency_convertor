#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
import requests
import json

class CurrencyConverter:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data["rates"]

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != "USD":
            amount = amount / self.currencies[from_currency]
        amount = round(amount * self.currencies[to_currency], 4)
        return amount

class App:
    def __init__(self, master):
        self.converter = CurrencyConverter("https://openexchangerates.org/api/latest.json?app_id=f9464a6643304da5a353323ab5b0ee08")

        # Create the dropdown menu for selecting the currencies
        self.currencies = sorted(list(self.converter.currencies.keys()))
        self.from_currency_var = tk.StringVar()
        self.from_currency_var.set(self.currencies[0])
        self.from_currency_label = tk.Label(master, text="From Currency")
        self.from_currency_menu = tk.OptionMenu(master, self.from_currency_var, *self.currencies)
        self.to_currency_var = tk.StringVar()
        self.to_currency_var.set(self.currencies[0])
        self.to_currency_label = tk.Label(master, text="To Currency")
        self.to_currency_menu = tk.OptionMenu(master, self.to_currency_var, *self.currencies)
        self.from_currency_label.grid(row=0, column=0, padx=10, pady=10)
        self.from_currency_menu.grid(row=0, column=1, padx=10, pady=10)
        self.to_currency_label.grid(row=1, column=0, padx=10, pady=10)
        self.to_currency_menu.grid(row=1, column=1, padx=10, pady=10)

        # Create the input field for the amount to convert
        self.amount_label = tk.Label(master, text="Amount")
        self.amount_entry = tk.Entry(master)
        self.amount_label.grid(row=2, column=0, padx=10, pady=10)
        self.amount_entry.grid(row=2, column=1, padx=10, pady=10)

        # Create the submit button and the label for displaying the converted amount
        self.submit_button = tk.Button(master, text="Convert", command=self.convert_currency)
        self.converted_amount_label = tk.Label(master, text="")
        self.submit_button.grid(row=3, column=0, padx=10, pady=10)
        self.converted_amount_label.grid(row=3, column=1, padx=10, pady=10)

        # Create the reset button
        self.reset_button = tk.Button(master, text="Reset", command=self.reset_fields)
        self.reset_button.grid(row=4, column=0, padx=10, pady=10)

    def convert_currency(self):
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()
        amount = float(self.amount_entry.get())
        converted_amount = self.converter.convert(from_currency, to_currency, amount)
        self.converted_amount_label.configure(text=str(converted_amount))

    def reset_fields(self):
        self.from_currency_var.set(self.currencies[0])
        self.to_currency_var.set(self.currencies[0])
        self.amount_entry.delete(0, tk.END)
        self.converted_amount_label.configure(text="")

root = tk.Tk()
app = App(root)
root.mainloop()


# In[ ]:




