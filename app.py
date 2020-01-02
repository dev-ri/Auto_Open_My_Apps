import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []
if os.path.isfile('save.text'):
    with open('save.text', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def add_app():
    for widget in frame.winfo_children():
        widget.destroy ()

    filename = filedialog.askopenfilename(initialdir="C:/", title="Select File", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, width= 50, pady = 5, padx = 10, text = app, bg = "#f67280", fg="white")
        label.pack()

def run_apps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=700, width=500)
canvas.pack()

frame = tk.Frame(root, bg="#1b262c")
frame.place(relwidth=1, relheight =1)

open_file = tk.Button(root, text="Open File", width=20, pady= 10, fg="#1b262c", bg="#fff", command=add_app)
open_file.pack()

run_apps = tk.Button(root, text="Run Apps", width = 20, pady= 10, fg="#1b262c", bg="#fff", command=run_apps)
run_apps.pack()

for app in apps:
    label = tk.Label(frame, width= 50, pady = 5, padx = 10, text = app, bg = "#f67280", fg="white")
    label.pack()
root.mainloop()

with open('save.text', 'w') as f:
    for app in apps:
        f.write(app+',')