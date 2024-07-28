import tkinter as tk
from tkinter import ttk, messagebox

# Apply a style
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TButton', font=('Helvetica', 12))

# Create and place the widgets with padding
mainframe = ttk.Frame( padding="20 20 20 20")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

amount_label = ttk.Label(mainframe, text="Amount in USD:")
amount_label.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
amount_entry = ttk.Entry(mainframe, width=20)
amount_entry.grid(column=2, row=1, padx=5, pady=5)

currency_label = ttk.Label(mainframe, text="Target Currency (e.g., EUR, GBP, JPY, CAD):")
currency_label.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
target_currency_entry = ttk.Entry(mainframe, width=20)
target_currency_entry.grid(column=2, row=2, padx=5, pady=5)

convert_button = ttk.Button(mainframe, text="Convert", command=)
convert_button.grid(column=2, row=3, padx=5, pady=10)

result_label = ttk.Label(mainframe, text="")
result_label.grid(column=1, row=4, columnspan=2, padx=5, pady=5)

# Set the focus to the amount entry field
amount_entry.focus()

