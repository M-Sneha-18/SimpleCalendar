import tkinter as tk
from tkinter import messagebox
import calendar

# Month colors mapping
month_colors = {
    1: "blue",
    2: "red",
    3: "green",
    4: "black",
    5: "pink",
    6: "orange",
    7: "skyblue",
    8: "maroon",
    9: "magenta",
    10: "silver",
    11: "gold",
    12: "yellow",
}

def show_calendar():
    year = year_entry.get()
    month = month_entry.get()

    if not (year.isdigit() and month.isdigit()):
        messagebox.showerror("Invalid input", "Year and month must be numbers.")
        return

    year = int(year)
    month = int(month)

    if month < 1 or month > 12:
        messagebox.showerror("Invalid input", "Month must be between 1 and 12.")
        return

    calendar_text.config(state=tk.NORMAL)
    calendar_text.delete("1.0", tk.END)

    month_color = month_colors.get(month, "black")
    calendar_text.tag_configure("monthcolor", foreground=month_color)

    month_name = calendar.month_name[month]
    header = f"{month_name} {year}\n"
    calendar_text.insert(tk.END, header, ("header", "monthcolor"))

    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    start_index = calendar_text.index(tk.END)
    # Insert weekday names with fixed spacing
    for day in weekdays:
        calendar_text.insert(tk.END, f"{day:^6}")  # 6 spaces, centered
    calendar_text.insert(tk.END, "\n")
    calendar_text.tag_add("weekday", start_index, calendar_text.index(tk.END))
    calendar_text.tag_add("monthcolor", start_index, calendar_text.index(tk.END))

    month_cal = calendar.monthcalendar(year, month)

    for week in month_cal:
        for i, day in enumerate(week):
            if day == 0:
                calendar_text.insert(tk.END, "      ")  # 6 spaces empty day
            else:
                day_str = f"{day:^6}"  # center day in 6 spaces
                pos_start = calendar_text.index(tk.END)
                calendar_text.insert(tk.END, day_str)
                pos_end = calendar_text.index(tk.END)

                calendar_text.tag_add("monthcolor", pos_start, pos_end)

                if i == 5:  # Saturday
                    calendar_text.tag_add("saturday", pos_start, pos_end)
                elif i == 6:  # Sunday
                    calendar_text.tag_add("sunday", pos_start, pos_end)
        calendar_text.insert(tk.END, "\n")

    calendar_text.config(state=tk.DISABLED)

# Setup window
root = tk.Tk()
root.title("Large Colorful Calendar by Month")
root.geometry("500x400")
root.configure(bg="#f0f8ff")

title_label = tk.Label(root, text="Simple Calendar", font=("Times New Roman", 28, "bold"), bg="#f0f8ff", fg="#333366")
title_label.grid(row=0, column=0, columnspan=2, pady=15)

tk.Label(root, text="Year:", font=("Times New Roman", 16), bg="#f0f8ff", fg="#333366").grid(row=1, column=0, sticky="e", padx=10)
year_entry = tk.Entry(root, width=12, bd=3, relief="groove", font=("Times New Roman", 16))
year_entry.grid(row=1, column=1, sticky="w", padx=10)

tk.Label(root, text="Month (1-12):", font=("Times New Roman", 16), bg="#f0f8ff", fg="#333366").grid(row=2, column=0, sticky="e", padx=10)
month_entry = tk.Entry(root, width=12, bd=3, relief="groove", font=("Times New Roman", 16))
month_entry.grid(row=2, column=1, sticky="w", padx=10)

show_button = tk.Button(root, text="Show Calendar", bg="#336699", fg="white", activebackground="#28527a", font=("Times New Roman", 16), command=show_calendar)
show_button.grid(row=3, column=0, columnspan=2, pady=20)

# Use monospace font for text widget for perfect alignment
calendar_text = tk.Text(root, width=45, height=12, font=("Consolas", 20), bd=3, relief="sunken", bg="#ffffff")
calendar_text.grid(row=4, column=0, columnspan=2, padx=20, pady=20)
calendar_text.config(state=tk.DISABLED)

calendar_text.tag_configure("header", font=("Consolas", 24, "bold"))
calendar_text.tag_configure("weekday", font=("Consolas", 18, "bold"))
calendar_text.tag_configure("saturday", foreground="#ff4500", font=("Consolas", 20, "bold"))
calendar_text.tag_configure("sunday", foreground="#ff0000", font=("Consolas", 20, "bold"))

root.mainloop()
