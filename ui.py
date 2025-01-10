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


def add_user(entry_username, entry_password, combo_role):
    username = entry_username.get()
    password = entry_password.get()
    role = combo_role.get()

    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        hashed_password = hash_password(password)
        query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, hashed_password, role))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "User added successfully!")
