import tkinter as tk
from tkinter import messagebox, ttk
from database import connect_to_db
import hashlib
import config


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def add_medicine(entry_name, entry_description, entry_quantity, entry_unit_price, entry_expiry_date,
                 entry_minimum_stock):
    name = entry_name.get()
    description = entry_description.get()
    quantity = int(entry_quantity.get())
    unit_price = float(entry_unit_price.get())
    expiry_date = entry_expiry_date.get()
    minimum_stock = int(entry_minimum_stock.get())

    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO medicines (name, description, quantity, unit_price, expiry_date, minimum_stock) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (name, description, quantity, unit_price, expiry_date, minimum_stock))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Medicine added successfully!")


def update_stock(entry_medicine_id, entry_stock_quantity, combo_transaction_type):
    medicine_id = int(entry_medicine_id.get())
    transaction_type = combo_transaction_type.get()
    quantity = int(entry_stock_quantity.get())

    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        if transaction_type == 'incoming':
            query = "UPDATE medicines SET quantity = quantity + %s WHERE id = %s"
        elif transaction_type == 'outgoing':
            query = "UPDATE medicines SET quantity = quantity - %s WHERE id = %s"
        cursor.execute(query, (quantity, medicine_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", f"Stock updated ({transaction_type}) successfully!")


def check_low_stock(low_stock_display):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        query = "SELECT id, name, quantity, minimum_stock FROM medicines"
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()

        low_stock = [row for row in results if row[2] < row[3]]
        low_stock_display.delete(*low_stock_display.get_children())  # Clear the display

        for row in low_stock:
            low_stock_display.insert("", "end", values=row)


def generate_report(report_display):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        query = "SELECT name, quantity, unit_price, expiry_date FROM medicines"
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()

        report_display.delete(*report_display.get_children())  # Clear the display
        for row in results:
            report_display.insert("", "end", values=row)


import tkinter as tk
from tkinter import messagebox

def add_user(entry_Emp_name, entry_Emp_Fname, entry_cell, entry_username, entry_password, combo_role, cursor, conn):
    try:
        # Get the values from the fields and combobox
        role_value = combo_role.get()
        emp_name = entry_Emp_name.get()
        emp_f_name = entry_Emp_Fname.get()
        cell_value = entry_cell.get()
        username = entry_username.get()
        password = entry_password.get()

        # Check if any of the fields are empty
        if not (username and password and role_value and emp_name and emp_f_name and cell_value):
            # Show error message if any field is empty
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        # Example code for adding a user to the database
        query = "INSERT INTO users (username, password, role, EmpName, EmpFname, cell) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (
            username,
            password,
            role_value,
            emp_name,
            emp_f_name,
            cell_value
        )
        cursor.execute(query, values)
        conn.commit()
        print("User added successfully!")

        # Clear all the fields after adding the user
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)
        combo_role.set('')  # Clear the combobox selection
        entry_Emp_name.delete(0, tk.END)
        entry_Emp_Fname.delete(0, tk.END)
        entry_cell.delete(0, tk.END)

    except Exception as e:
        print(f"Error adding user: {e}")



