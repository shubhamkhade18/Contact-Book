import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")

        self.contacts = []
        self.name_entry = tk.Entry(master, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        self.phone_entry = tk.Entry(master, width=30)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(master, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
        tk.Label(master, text="Phone:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)

        add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.contact_listbox = tk.Listbox(master, selectmode=tk.SINGLE, width=30)
        self.contact_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        remove_button = tk.Button(master, text="Remove Contact", command=self.remove_contact)
        remove_button.grid(row=4, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()

        if name and phone:
            contact = f"{name} - {phone}"
            self.contacts.append(contact)
            self.contact_listbox.insert(tk.END, contact)
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter both name and phone.")

    def remove_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            contact = self.contacts.pop(selected_index[0])
            self.contact_listbox.delete(selected_index)
            messagebox.showinfo("Contact Removed", f"Contact '{contact}' removed.")
        else:
            messagebox.showwarning("Warning", "Please select a contact to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
