import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []
        
        self.entry = tk.Entry(self.root, font=("Helvetica", 16))
        self.entry.pack(pady=10)
        
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task, bg="green", fg="white")
        self.add_button.pack(pady=5)
        
        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task, bg="blue", fg="white")
        self.update_button.pack(pady=5)
        
        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task, bg="red", fg="white")
        self.delete_button.pack(pady=5)
        
        self.clear_button = tk.Button(self.root, text="Clear Screen", command=self.clear_screen, bg="purple", fg="white")
        self.clear_button.pack(pady=5)
        
        self.track_button = tk.Button(self.root, text="Track Tasks", command=self.track_tasks, bg="orange", fg="white")
        self.track_button.pack(pady=5)
        
        self.listbox = tk.Listbox(self.root, height=15, width=50, font=("Helvetica", 12))
        self.listbox.pack(pady=15)
    
    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.entry.delete(0, tk.END)
    
    def update_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            new_task = self.entry.get()
            if new_task:
                index = selected_index[0]
                self.tasks[index] = new_task
                self.update_listbox()
                self.entry.delete(0, tk.END)
    
    def delete_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_listbox()
    
    def clear_screen(self):
        self.listbox.delete(0, tk.END)
    
    def track_tasks(self):
        tasks_text = "\n".join(self.tasks)
        messagebox.showinfo("Tasks", tasks_text)
    
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
