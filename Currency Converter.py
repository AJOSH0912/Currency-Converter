import tkinter as tk
from tkinter import ttk, messagebox


def get_exchange_rate(target_currency):
    """Return the exchange rate for the target currency."""
    exchange_rates = {
        'USD': 1.0,    # Base currency
        'EUR': 0.85,   # Example rates
        'GBP': 0.75,
        'JPY': 110.0,
        'CAD': 1.25
    }
    return exchange_rates.get(target_currency.upper(), None)

def convert_currency(amount, target_currency):
    """Convert the amount to the target currency using the exchange rate."""
    rate = get_exchange_rate(target_currency)
    if rate is None:
        return None
    return amount * rate

def on_convert():
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number for the amount.")
        return

    target_currency = target_currency_entry.get().upper()
    converted_amount = convert_currency(amount, target_currency)
    
    if converted_amount is not None:
        result_label.config(text=f"{amount:.2f} USD is equivalent to {converted_amount:.2f} {target_currency}.")
    else:
        messagebox.showerror("Invalid currency", "Please enter a valid target currency.")

# Create the main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x200")
root.resizable(False, False)

# Apply a style
style = ttk.Style(root)
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TButton', font=('Helvetica', 12))

# Create and place the widgets with padding
mainframe = ttk.Frame(root, padding="20 20 20 20")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

amount_label = ttk.Label(mainframe, text="Amount in USD:")
amount_label.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
amount_entry = ttk.Entry(mainframe, width=20)
amount_entry.grid(column=2, row=1, padx=5, pady=5)

currency_label = ttk.Label(mainframe, text="Target Currency (e.g., EUR, GBP, JPY, CAD):")
currency_label.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
target_currency_entry = ttk.Entry(mainframe, width=20)
target_currency_entry.grid(column=2, row=2, padx=5, pady=5)

convert_button = ttk.Button(mainframe, text="Convert", command=on_convert)
convert_button.grid(column=2, row=3, padx=5, pady=10)

result_label = ttk.Label(mainframe, text="")
result_label.grid(column=1, row=4, columnspan=2, padx=5, pady=5)

# Set the focus to the amount entry field
amount_entry.focus()

# Start the main loop
root.mainloop()
