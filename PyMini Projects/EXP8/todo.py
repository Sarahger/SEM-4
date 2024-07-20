import tkinter as tk

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append((task, False))
        update_task_frame()
        task_entry.delete(0, tk.END)

def delete_task():
    updated_tasks = [(task, checked) for task, checked in tasks if not checked]
    tasks.clear()
    tasks.extend(updated_tasks)
    update_task_frame()

def update_task_frame():
    for widget in task_frame.winfo_children():
        widget.destroy()
    
    for i, (task, checked) in enumerate(tasks):
        check_button = tk.Checkbutton(task_frame, text=task, variable=tk.BooleanVar(value=checked))
        check_button.grid(row=i, column=0, sticky="w")

root = tk.Tk()
root.title("To-do List")

# Entry for adding new tasks
task_entry = tk.Entry(root, width=30, justify="center")
task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2 )

# Button to add tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=1, column=0, padx=10, pady=10)

# Frame to contain tasks
task_frame = tk.Frame(root)
task_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Button to delete tasks
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
