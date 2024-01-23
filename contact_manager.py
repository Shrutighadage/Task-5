import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManagerApp:
    def __init__(self):
        self.contacts = []
        
        self.root = tk.Tk()
        self.root.title("Contact Manager")

        # Labels and Entry widgets for contact details
        tk.Label(self.root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Email:").grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Address:").grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons for actions
        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="View Contacts", command=self.view_contacts).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Search Contact", command=self.search_contact).grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Update Contact", command=self.update_contact).grid(row=7, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=8, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            new_contact = Contact(name, phone, email, address)
            self.contacts.append(new_contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and phone are required fields.")

    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join([f"{contact.name}: {contact.phone}" for contact in self.contacts])
            messagebox.showinfo("Contacts", contact_list)
        else:
            messagebox.showinfo("Contacts", "No contacts available.")

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_term:
            search_result = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
            if search_result:
                contact_list = "\n".join([f"{contact.name}: {contact.phone}" for contact in search_result])
                messagebox.showinfo("Search Result", contact_list)
            else:
                messagebox.showinfo("Search Result", "No matching contacts found.")
        else:
            messagebox.showerror("Error", "Please enter a search term.")

    def update_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_term:
            search_result = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
            if search_result:
                contact = search_result[0]
                new_phone = tk.simpledialog.askstring("Update Contact", f"Update phone for {contact.name}:")
                if new_phone:
                    contact.phone = new_phone
                    messagebox.showinfo("Success", "Contact updated successfully!")
                else:
                    messagebox.showerror("Error", "Invalid phone number.")
            else:
                messagebox.showinfo("Search Result", "No matching contacts found.")
        else:
            messagebox.showerror("Error", "Please enter a search term.")

    def delete_contact(self):
        search_term = tk.simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_term:
            search_result = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
            if search_result:
                contact = search_result[0]
                confirmation = messagebox.askyesno("Delete Contact", f"Are you sure you want to delete {contact.name}'s contact?")
                if confirmation:
                    self.contacts.remove(contact)
                    messagebox.showinfo("Success", "Contact deleted successfully!")
                else:
                    messagebox.showinfo("Info", "Contact not deleted.")
            else:
                messagebox.showinfo("Search Result", "No matching contacts found.")
        else:
            messagebox.showerror("Error", "Please enter a search term.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ContactManagerApp()
    app.run()
