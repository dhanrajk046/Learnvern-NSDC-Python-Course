import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to validate login
def login():
    user = username_entry.get()
    pwd = password_entry.get()

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="zhfs4866@#DK",
            database="user_db"
        )
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        cursor.execute(query, (user, pwd))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Login Success", f"Welcome {user}!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# GUI setup
root = tk.Tk()
root.title("MySQL Login")
root.geometry("300x200")

tk.Label(root, text="Username").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Password").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Login", command=login).pack(pady=20)

root.mainloop()