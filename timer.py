import tkinter as tk
from tkinter import messagebox

# Function to start the countdown
def start_timer():
    try:
        minutes = int(entry_minutes.get())
        seconds = int(entry_seconds.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for minutes and seconds.")
        return

    total_seconds = minutes * 60 + seconds
    countdown(total_seconds)

# Function to handle the countdown
def countdown(seconds_left):
    if seconds_left >= 0:
        minutes = seconds_left // 60
        seconds = seconds_left % 60
        time_string = f"{minutes:02}:{seconds:02}"
        label_time.config(text=time_string)
        root.after(1000, countdown, seconds_left - 1)  # Call countdown again after 1 second
    else:
        messagebox.showinfo("Time's up!", "The countdown has finished!")

# Set up the main window
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("400x300")
root.configure(bg="#2E3B4E")  # Set the background color

# Set up the layout with padding
frame = tk.Frame(root, bg="#2E3B4E")
frame.pack(pady=30)

# Title label
title_label = tk.Label(frame, text="Countdown Timer", font=("Helvetica", 20, "bold"), fg="white", bg="#2E3B4E")
title_label.grid(row=0, columnspan=4, pady=10)

# Labels and Entry fields for minutes and seconds
label_minutes = tk.Label(frame, text="Minutes:", font=("Helvetica", 12), fg="white", bg="#2E3B4E")
label_minutes.grid(row=1, column=0, padx=10, pady=5)

entry_minutes = tk.Entry(frame, width=5, font=("Helvetica", 12), bd=2, relief="solid")
entry_minutes.grid(row=1, column=1, pady=5)

label_seconds = tk.Label(frame, text="Seconds:", font=("Helvetica", 12), fg="white", bg="#2E3B4E")
label_seconds.grid(row=1, column=2, padx=10, pady=5)

entry_seconds = tk.Entry(frame, width=5, font=("Helvetica", 12), bd=2, relief="solid")
entry_seconds.grid(row=1, column=3, pady=5)

# Start button with a stylish background
button_start = tk.Button(root, text="Start Timer", font=("Helvetica", 14), bg="#4CAF50", fg="Maroon", command=start_timer, relief="raised")
button_start.pack(pady=20)

# Timer label to display remaining time
label_time = tk.Label(root, text="00:00", font=("Helvetica", 30, "bold"), fg="White", bg="#2E3B4E")
label_time.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
