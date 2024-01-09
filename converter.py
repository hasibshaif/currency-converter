import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates

class CurrencyConverter:
    def __init__(self, root):
        # Initialize the CurrencyConverter class with the Tkinter root window
        self.root = root
        self.root.title("Currency Converter")  # Set the title of the window

        # Set a background color for the window
        self.root.configure(bg="#1d3954")

        # Initialize variables for amount, source currency, target currency, and converted amount
        self.amount_var = tk.DoubleVar()
        self.from_currency_var = tk.StringVar(value='USD')
        self.to_currency_var = tk.StringVar(value='USD')
        self.converted_amount_var = tk.StringVar()

        # Labels for the GUI
        self.title_label = tk.Label(root, text="Currency Converter", font=("Helvetica", 18, "bold"), bg="#1d3954", fg="#ECF0F1")
        self.from_label = tk.Label(root, text="From:", font=("Helvetica", 14, "italic"), bg="#1d3954", fg="#ECF0F1")
        self.to_label = tk.Label(root, text="To:", font=("Helvetica", 14, "italic"), bg="#1d3954", fg="#ECF0F1")

        # Left side (From) widgets
        self.amount_label_from = tk.Label(root, text="Amount:", font=("Helvetica", 12), bg="#1d3954", fg="#ECF0F1")
        self.amount_entry_from = tk.Entry(root, textvariable=self.amount_var, font=("Helvetica", 12), width=15, bd=5, relief="flat")
        self.currency_label_from = tk.Label(root, text="Currency:", font=("Helvetica", 12), bg="#1d3954", fg="#ECF0F1")
        self.currency_dropdown_from = ttk.Combobox(root, textvariable=self.from_currency_var, values=self.get_currency_list(), font=("Helvetica", 12), state="readonly", justify="center", width=13, background="#34495E", foreground="#ECF0F1")

        # Right side (To) widgets
        self.amount_label_to = tk.Label(root, text="Converted Amount:", font=("Helvetica", 12), bg="#1d3954", fg="#ECF0F1")
        self.amount_entry_to = tk.Entry(root, state="readonly", textvariable=self.converted_amount_var, font=("Helvetica", 12), width=15, bd=5, relief="flat")
        self.currency_label_to = tk.Label(root, text="Currency:", font=("Helvetica", 12), bg="#1d3954", fg="#ECF0F1")
        self.currency_dropdown_to = ttk.Combobox(root, textvariable=self.to_currency_var, values=self.get_currency_list(), font=("Helvetica", 12), state="readonly", justify="center", width=13, background="#34495E", foreground="#ECF0F1")

        # Convert button
        self.convert_button = tk.Button(root, text="Convert", command=self.convert_currency, font=("Helvetica", 14), bg="#118996", fg="white", bd=5, relief="flat", activebackground="#2980B9", cursor="hand2")

        # Place widgets on the grid
        self.title_label.grid(row=0, column=0, columnspan=4, pady=10)
        self.from_label.grid(row=1, column=0, pady=5)
        self.to_label.grid(row=1, column=2, pady=5)

        self.amount_label_from.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.amount_entry_from.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        self.currency_label_from.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.currency_dropdown_from.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.amount_label_to.grid(row=2, column=2, padx=10, pady=10, sticky="w")
        self.amount_entry_to.grid(row=2, column=3, padx=10, pady=10, sticky="w")
        self.currency_label_to.grid(row=3, column=2, padx=10, pady=10, sticky="w")
        self.currency_dropdown_to.grid(row=3, column=3, padx=10, pady=10, sticky="w")

        self.convert_button.grid(row=4, column=0, columnspan=4, pady=20)

    def get_currency_list(self):
        # Get the list of currency codes using the forex-python library
        c = CurrencyRates()
        currencies = c.get_rates('USD')
        currency_list = ['USD'] + list(currencies.keys())
        return currency_list

    def convert_currency(self):
        try:
            # Get user input and perform currency conversion
            amount = float(self.amount_var.get())
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()

            # Use the forex-python library to get the exchange rate
            c = CurrencyRates()
            rate = c.get_rate(from_currency, to_currency)

            # Calculate the converted amount and display it
            converted_amount = round(amount * rate, 2)
            self.converted_amount_var.set(converted_amount)
        except ValueError:
            # Handle invalid input (non-numeric input)
            self.converted_amount_var.set("Invalid Input")

if __name__ == "__main__":
    # Create an instance of the Tkinter root window and the CurrencyConverter class
    root = tk.Tk()
    converter = CurrencyConverter(root)
    # Start the Tkinter event loop
    root.mainloop()
