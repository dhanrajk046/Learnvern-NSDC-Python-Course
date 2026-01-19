from tkinter import *
import sqlite3

# --- Database Setup ---
def connect_db():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS student (
            roll INTEGER PRIMARY KEY,
            firstname TEXT,
            lastname TEXT,
            email TEXT
        )
    """)
    conn.commit()
    conn.close()

connect_db()

# --- CRUD Operations ---
def insert_data():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO student VALUES (?, ?, ?, ?)", (
        roll_entry.get(),
        fname_entry.get(),
        lname_entry.get(),
        email_entry.get()
    ))
    conn.commit()
    conn.close()
    status_label.config(text="Inserted successfully")

def search_data():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student WHERE roll=?", (roll_entry.get(),))
    row = cur.fetchone()
    conn.close()
    if row:
        fname_entry.delete(0, END)
        lname_entry.delete(0, END)
        email_entry.delete(0, END)
        fname_entry.insert(0, row[1])
        lname_entry.insert(0, row[2])
        email_entry.insert(0, row[3])
        status_label.config(text="Record found")
    else:
        status_label.config(text="No record found")

def update_data():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("""
        UPDATE student SET firstname=?, lastname=?, email=? WHERE roll=?
    """, (
        fname_entry.get(),
        lname_entry.get(),
        email_entry.get(),
        roll_entry.get()
    ))
    conn.commit()
    conn.close()
    status_label.config(text="Updated successfully")

def delete_data():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM student WHERE roll=?", (roll_entry.get(),))
    conn.commit()
    conn.close()
    fname_entry.delete(0, END)
    lname_entry.delete(0, END)
    email_entry.delete(0, END)
    status_label.config(text="Deleted successfully")

# --- GUI Setup ---
r = Tk()
r.geometry("500x400")
r.title("Student Database")
r.configure(bg="yellow")

Label(r, text="Roll No.", bg="yellow").place(x=20, y=20)
roll_entry = Entry(r)
roll_entry.place(x=150, y=20)

Label(r, text="First Name", bg="yellow").place(x=20, y=60)
fname_entry = Entry(r)
fname_entry.place(x=150, y=60)

Label(r, text="Last Name", bg="yellow").place(x=20, y=100)
lname_entry = Entry(r)
lname_entry.place(x=150, y=100)

Label(r, text="Email", bg="yellow").place(x=20, y=140)
email_entry = Entry(r)
email_entry.place(x=150, y=140)

Button(r, text="Insert", command=insert_data).place(x=50, y=200)
Button(r, text="Search", command=search_data).place(x=120, y=200)
Button(r, text="Update", command=update_data).place(x=200, y=200)
Button(r, text="Delete", command=delete_data).place(x=280, y=200)

status_label = Label(r, text="", bg="yellow", fg="blue")
status_label.place(x=20, y=250)

r.mainloop()