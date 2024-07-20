import tkinter as tk
from tkinter import filedialog

def new_file():
    text.delete("1.0", tk.END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text.delete("1.0", tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get("1.0", tk.END))

def copy_text():
    text.clipboard_clear()
    text.clipboard_append(text.selection_get())

def cut_text():
    copy_text()
    text.delete("sel.first", "sel.last")

def paste_text():
    text.insert(tk.INSERT, text.clipboard_get())

root = tk.Tk()
root.title("Text Editor")

text = tk.Text(root, wrap="word", undo=True)
text.grid(row=0, column=0, sticky="nsew")

# Create a toolbar for actions
toolbar = tk.Frame(root, border=2)
toolbar.grid(row=1, column=0, sticky="ew")

new_button = tk.Button(toolbar, text="New", command=new_file)
new_button.pack(side=tk.LEFT, padx=25, pady=15)

open_button = tk.Button(toolbar, text="Open", command=open_file)
open_button.pack(side=tk.LEFT, padx=25, pady=15)

save_button = tk.Button(toolbar, text="Save", command=save_file)
save_button.pack(side=tk.LEFT, padx=25, pady=15)

copy_button = tk.Button(toolbar, text="Copy", command=copy_text)
copy_button.pack(side=tk.LEFT, padx=25, pady=15)

cut_button = tk.Button(toolbar, text="Cut", command=cut_text)
cut_button.pack(side=tk.LEFT, padx=25, pady=15)

paste_button = tk.Button(toolbar, text="Paste", command=paste_text)
paste_button.pack(side=tk.LEFT, padx=25, pady=15)

root.mainloop()
