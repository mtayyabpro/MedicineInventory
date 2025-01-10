import tkinter as tk
from tkinter import ttk
from ui import add_medicine, update_stock, check_low_stock, generate_report, add_user
import database

# Initialize the main window
root = tk.Tk()
root.title("Advanced Inventory Management System")

# Create Sidebar
sidebar = tk.Frame(root, width=200, bg="#2f4f4f", height=600, relief="sunken", borderwidth=2)
sidebar.grid(row=0, column=0, sticky="nsew")

# Sidebar Buttons
button_add_medicine = tk.Button(sidebar, text="Add Medicine", command=lambda: show_frame("add_medicine"), width=20, bg="#4CAF50", fg="white")
button_add_medicine.grid(row=0, column=0, padx=10, pady=10)

button_update_stock = tk.Button(sidebar, text="Update Stock", command=lambda: show_frame("update_stock"), width=20, bg="#4CAF50", fg="white")
button_update_stock.grid(row=1, column=0, padx=10, pady=10)

button_check_low_stock = tk.Button(sidebar, text="Low Stock", command=lambda: show_frame("low_stock"), width=20, bg="#4CAF50", fg="white")
button_check_low_stock.grid(row=2, column=0, padx=10, pady=10)

button_generate_report = tk.Button(sidebar, text="Generate Report", command=lambda: show_frame("stock_report"), width=20, bg="#4CAF50", fg="white")
button_generate_report.grid(row=3, column=0, padx=10, pady=10)

button_user_management = tk.Button(sidebar, text="User Management", command=lambda: show_frame("user_management"), width=20, bg="#4CAF50", fg="white")
button_user_management.grid(row=4, column=0, padx=10, pady=10)

# Create main content area
main_content = tk.Frame(root, width=800, height=600)
main_content.grid(row=0, column=1, padx=10, pady=10)

# Add Medicine Form
frame_add_medicine = tk.LabelFrame(main_content, text="Add Medicine", padx=10, pady=10)
label_name = tk.Label(frame_add_medicine, text="Medicine Name:")
label_name.grid(row=0, column=0)
entry_name = tk.Entry(frame_add_medicine)
entry_name.grid(row=0, column=1)

label_type=tk.Label(frame_add_medicine, text='type')
label_type.grid(row=1, column=0)
label_type = tk.Entry(frame_add_medicine)
label_type.grid(row=1, column=1)

label_description = tk.Label(frame_add_medicine, text="Description:")
label_description.grid(row=2, column=0)
entry_description = tk.Entry(frame_add_medicine)
entry_description.grid(row=2, column=1)

label_strength = tk.Label(frame_add_medicine, text='strength')
label_strength.grid(row=3,column=0)
label_strength = tk.Entry(frame_add_medicine)
label_strength.grid(row=3,column=1)

label_quantity = tk.Label(frame_add_medicine, text="Quantity:")
label_quantity.grid(row=4, column=0)
entry_quantity = tk.Entry(frame_add_medicine)
entry_quantity.grid(row=4, column=1)

label_unit_price = tk.Label(frame_add_medicine, text="Unit Price:")
label_unit_price.grid(row=5, column=0)
entry_unit_price = tk.Entry(frame_add_medicine)
entry_unit_price.grid(row=5, column=1)

label_expiry_date = tk.Label(frame_add_medicine, text="Expiry Date (YYYY-MM-DD):")
label_expiry_date.grid(row=6, column=0)
entry_expiry_date = tk.Entry(frame_add_medicine)
entry_expiry_date.grid(row=6, column=1)

label_minimum_stock = tk.Label(frame_add_medicine, text="Minimum Stock:")
label_minimum_stock.grid(row=7, column=0)
entry_minimum_stock = tk.Entry(frame_add_medicine)
entry_minimum_stock.grid(row=7, column=1)

button_add_medicine = tk.Button(frame_add_medicine, text="Add Medicine", command=lambda: add_medicine(entry_name, entry_description, entry_quantity, entry_unit_price, entry_expiry_date, entry_minimum_stock))
button_add_medicine.grid(row=8, column=0, columnspan=2)

# Update Stock Form
frame_update_stock = tk.LabelFrame(main_content, text="Update Stock", padx=10, pady=10)
label_medicine_id = tk.Label(frame_update_stock, text="Medicine ID:")
label_medicine_id.grid(row=0, column=0)
entry_medicine_id = tk.Entry(frame_update_stock)
entry_medicine_id.grid(row=0, column=1)

label_stock_quantity = tk.Label(frame_update_stock, text="Quantity:")
label_stock_quantity.grid(row=1, column=0)
entry_stock_quantity = tk.Entry(frame_update_stock)
entry_stock_quantity.grid(row=1, column=1)

label_transaction_type = tk.Label(frame_update_stock, text="Transaction Type:")
label_transaction_type.grid(row=2, column=0)
combo_transaction_type = ttk.Combobox(frame_update_stock, values=['incoming', 'outgoing'])
combo_transaction_type.grid(row=2, column=1)

button_update_stock = tk.Button(frame_update_stock, text="Update Stock", command=lambda: update_stock(entry_medicine_id, entry_stock_quantity, combo_transaction_type))
button_update_stock.grid(row=3, column=0, columnspan=2)

# Low Stock Display
frame_low_stock = tk.LabelFrame(main_content, text="Low Stock Medicines", padx=10, pady=10)
low_stock_display = ttk.Treeview(frame_low_stock, columns=("ID", "Name", "Quantity", "Minimum Stock"), show="headings")
low_stock_display.grid(row=0, column=0)
low_stock_display.heading("ID", text="ID")
low_stock_display.heading("Name", text="Name")
low_stock_display.heading("Quantity", text="Quantity")
low_stock_display.heading("Minimum Stock", text="Minimum Stock")

button_check_low_stock = tk.Button(frame_low_stock, text="Check Low Stock", command=lambda: check_low_stock(low_stock_display))
button_check_low_stock.grid(row=1, column=0)

# Report Display
frame_report = tk.LabelFrame(main_content, text="Stock Report", padx=10, pady=10)
report_display = ttk.Treeview(frame_report, columns=("Name", "Quantity", "Unit Price", "Expiry Date"), show="headings")
report_display.grid(row=0, column=0)
report_display.heading("Name", text="Name")
report_display.heading("Quantity", text="Quantity")
report_display.heading("Unit Price", text="Unit Price")
report_display.heading("Expiry Date", text="Expiry Date")

button_generate_report = tk.Button(frame_report, text="Generate Report", command=lambda: generate_report(report_display))
button_generate_report.grid(row=1, column=0)

# User Management Form
frame_user_management = tk.LabelFrame(main_content, text="User Management", padx=10, pady=10)
label_username = tk.Label(frame_user_management, text="Username:")
label_username.grid(row=0, column=0)
entry_username = tk.Entry(frame_user_management)
entry_username.grid(row=0, column=1)

label_password = tk.Label(frame_user_management, text="Password:")
label_password.grid(row=1, column=0)
entry_password = tk.Entry(frame_user_management, show="*")
entry_password.grid(row=1, column=1)

label_role = tk.Label(frame_user_management, text="Role:")
label_role.grid(row=2, column=0)
combo_role = ttk.Combobox(frame_user_management, values=["admin", "staff"])
combo_role.grid(row=2, column=1)

button_add_user = tk.Button(frame_user_management, text="Add User", command=lambda: add_user(entry_username, entry_password, combo_role))
button_add_user.grid(row=3, column=0, columnspan=2)

# Function to switch between frames
def show_frame(frame_name):
    for widget in main_content.winfo_children():
        widget.grid_forget()

    if frame_name == "add_medicine":
        frame_add_medicine.grid(row=0, column=0, padx=10, pady=10)
    elif frame_name == "update_stock":
        frame_update_stock.grid(row=0, column=0, padx=10, pady=10)
    elif frame_name == "low_stock":
        frame_low_stock.grid(row=0, column=0, padx=10, pady=10)
    elif frame_name == "stock_report":
        frame_report.grid(row=0, column=0, padx=10, pady=10)
    elif frame_name == "user_management":
        frame_user_management.grid(row=0, column=0, padx=10, pady=10)

# Show initial frame
show_frame("add_medicine")

# Start the main loop
root.mainloop()
