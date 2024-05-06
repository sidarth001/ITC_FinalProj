import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import database

def login():
    username = username_entry.get()
    password = password_entry.get()
    conn = sqlite3.connect('userdata_3.db.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = cursor.fetchone()
    conn.close()

    if user and user[2] == password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}! You have successfully logged in.")
        database.log_activity(username, "Login")
        create_lunch_booking_page()  # Move to lunch booking page
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def create_lunch_booking_page():
    root.withdraw()  # Hide the login window
    lunch_root = tk.Tk()
    lunch_root.title("Lunch Booking")
    lunch_root.attributes('-fullscreen', True)  # Maximize the window

    # Use ttk style to customize the appearance of widgets
    style = ttk.Style()
    style.configure('TButton', font=('Helvetica', 14), background='black', foreground='white', padding=10)

    current_time = datetime.now().time()
    time_label = ttk.Label(lunch_root, text=f"Current Time: {current_time.strftime('%H:%M:%S')}", font=('Helvetica', 16))
    time_label.pack(pady=20)

    if datetime.now().time() >= datetime.strptime('09:00:00', '%H:%M:%S').time() and datetime.now().time() <= datetime.strptime('11:30:00', '%H:%M:%S').time():
        book_lunch_button = ttk.Button(lunch_root, text="Book Lunch", command=book_lunch)
        book_lunch_button.pack(pady=10)

        # To-Do List Frame
        todo_frame = ttk.Frame(lunch_root)
        todo_frame.pack(pady=20)

        todo_label = ttk.Label(todo_frame, text="To-Do List:", font=("Helvetica", 16))
        todo_label.pack()

        # Add a listbox to display the to-do items
        todo_listbox = tk.Listbox(todo_frame, height=5, width=50, font=("Helvetica", 12))
        todo_listbox.pack(pady=10)

        # Add items to the to-do listbox
        todo_listbox.insert(tk.END, "Task 1")
        todo_listbox.insert(tk.END, "Task 2")
        todo_listbox.insert(tk.END, "Task 3")

    else:
        message_label = ttk.Label(lunch_root, text="Lunch booking is only available between 9:00 AM and 11:30 AM.")
        message_label.pack(pady=10)

    lunch_root.mainloop()

def book_lunch():
    messagebox.showinfo("Lunch Booked", "Your lunch has been booked successfully!")
    database.log_activity(username_entry.get(), "Lunch Booking")

root = tk.Tk()
root.title("Basic Webpage - Login")
root.attributes('-fullscreen', True)  # Maximize the window

# Use ttk style to customize the appearance of widgets
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 14), background='black', foreground='white', padding=10)

title_label = ttk.Label(root, text="Welcome to My Basic Webpage", font=("Helvetica", 24))
title_label.pack(pady=20)

username_label = ttk.Label(root, text="Username:", font=("Helvetica", 16))
username_label.pack()
username_entry = ttk.Entry(root, font=("Helvetica", 14))
username_entry.pack()

password_label = ttk.Label(root, text="Password:", font=("Helvetica", 16))
password_label.pack()
password_entry = ttk.Entry(root, show="*", font=("Helvetica", 14))
password_entry.pack()

login_button = ttk.Button(root, text="Login", command=login)
login_button.pack(pady=10)

root.mainloop()
