import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

# Define the CSV file name
CONTACTS_FILE = 'contacts.csv'
# Define the headers for the CSV file
HEADERS = ["First Name", "Last Name", "Email", "Phone Number", "Address"]

# --- Functions for File Operations ---

def ensure_csv_file_exists():
    """Checks if the contacts.csv file exists, creates it with headers if not."""
    if not os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)

def save_contact_to_csv(contact_data):
    """Appends a new contact to the CSV file."""
    ensure_csv_file_exists() # Ensure file exists before writing
    with open(CONTACTS_FILE, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(contact_data)

def get_all_contacts():
    """Reads all contacts from the CSV file."""
    ensure_csv_file_exists() # Ensure file exists before reading
    contacts = []
    with open(CONTACTS_FILE, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader) # Skip the header row
        for row in reader:
            contacts.append(row)
    return contacts

# --- GUI Functions ---

def add_contact():
    """Adds a new contact based on user input."""
    first_name = first_name_var.get().strip()
    last_name = last_name_var.get().strip()
    email = email_var.get().strip()
    phone = phone_var.get().strip()
    address = address_text.get("1.0", tk.END).strip() # Get text from Text widget

    if not all([first_name, last_name, email, phone, address]):
        messagebox.showwarning("Warning", "Please fill in all contact fields.")
        return

    contact_data = [first_name, last_name, email, phone, address]
    save_contact_to_csv(contact_data)
    messagebox.showinfo("Success", "Contact added successfully!")
    clear_entries() # Clear input fields after adding

def search_contact():
    """Searches for a contact by first and last name."""
    search_first = search_first_name_var.get().strip().lower()
    search_last = search_last_name_var.get().strip().lower()

    if not search_first and not search_last:
        messagebox.showwarning("Warning", "Please enter a first name or last name to search.")
        return

    found_contacts = []
    contacts = get_all_contacts()
    for contact in contacts:
        contact_first = contact[0].lower() # First Name
        contact_last = contact[1].lower()  # Last Name

        if (search_first and search_first in contact_first) or \
           (search_last and search_last in contact_last):
            found_contacts.append(contact)

    clear_details() # Clear previous search results

    if found_contacts:
        details_text.insert(tk.END, "--- Found Contacts ---\n\n")
        for contact in found_contacts:
            details_text.insert(tk.END, f"First Name: {contact[0]}\n")
            details_text.insert(tk.END, f"Last Name: {contact[1]}\n")
            details_text.insert(tk.END, f"Email: {contact[2]}\n")
            details_text.insert(tk.END, f"Phone: {contact[3]}\n")
            details_text.insert(tk.END, f"Address: {contact[4]}\n")
            details_text.insert(tk.END, "----------------------\n\n")
    else:
        details_text.insert(tk.END, "No matching contacts found.\n")

def clear_entries():
    """Clears all input fields for adding a new contact."""
    first_name_var.set("")
    last_name_var.set("")
    email_var.set("")
    phone_var.set("")
    address_text.delete("1.0", tk.END)
    search_first_name_var.set("") # Also clear search fields
    search_last_name_var.set("")

def clear_details():
    """Clears the contact details display area."""
    details_text.delete("1.0", tk.END)

# --- Set up the main application window ---
root = tk.Tk()
root.title("Simple Contact Book")
root.geometry("600x650") # Adjust size as needed
root.resizable(False, False) # Prevent resizing for simpler layout
root.config(bg="#f0f0f0") # Light grey background

# --- Variables to store input and output ---
first_name_var = tk.StringVar()
last_name_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()
search_first_name_var = tk.StringVar()
search_last_name_var = tk.StringVar()

# --- Contact Input Frame ---
input_frame = ttk.LabelFrame(root, text="Add New Contact", padding="15")
input_frame.pack(pady=10, padx=15, fill="x")

# Grid layout for input fields
ttk.Label(input_frame, text="First Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
ttk.Entry(input_frame, textvariable=first_name_var, width=30).grid(row=0, column=1, padx=5, pady=5, sticky="ew")

ttk.Label(input_frame, text="Last Name:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
ttk.Entry(input_frame, textvariable=last_name_var, width=30).grid(row=1, column=1, padx=5, pady=5, sticky="ew")

ttk.Label(input_frame, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
ttk.Entry(input_frame, textvariable=email_var, width=30).grid(row=2, column=1, padx=5, pady=5, sticky="ew")

ttk.Label(input_frame, text="Phone Number:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
ttk.Entry(input_frame, textvariable=phone_var, width=30).grid(row=3, column=1, padx=5, pady=5, sticky="ew")

ttk.Label(input_frame, text="Address:").grid(row=4, column=0, padx=5, pady=5, sticky="nw")
address_text = tk.Text(input_frame, height=4, width=30)
address_text.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

# Buttons for adding/cancelling
button_frame = ttk.Frame(input_frame)
button_frame.grid(row=5, column=0, columnspan=2, pady=10)
ttk.Button(button_frame, text="Add Contact", command=add_contact).pack(side=tk.LEFT, padx=5)
ttk.Button(button_frame, text="Clear Fields", command=clear_entries).pack(side=tk.LEFT, padx=5)

# --- Search Frame ---
search_frame = ttk.LabelFrame(root, text="Search Contact", padding="15")
search_frame.pack(pady=10, padx=15, fill="x")

ttk.Label(search_frame, text="First Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
ttk.Entry(search_frame, textvariable=search_first_name_var, width=20).grid(row=0, column=1, padx=5, pady=5, sticky="ew")

ttk.Label(search_frame, text="Last Name:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
ttk.Entry(search_frame, textvariable=search_last_name_var, width=20).grid(row=1, column=1, padx=5, pady=5, sticky="ew")

search_button_frame = ttk.Frame(search_frame)
search_button_frame.grid(row=2, column=0, columnspan=2, pady=10)
ttk.Button(search_button_frame, text="Search", command=search_contact).pack(side=tk.LEFT, padx=5)
ttk.Button(search_button_frame, text="Clear Search Results", command=clear_details).pack(side=tk.LEFT, padx=5)


# --- Contact Details Display Area ---
details_frame = ttk.LabelFrame(root, text="Contact Details", padding="15")
details_frame.pack(pady=10, padx=15, fill="both", expand=True)

details_text = tk.Text(details_frame, height=10, width=50, wrap="word", state="normal") # 'normal' to allow insertion
details_text.pack(fill="both", expand=True)
# Add a scrollbar to the text widget
text_scrollbar = ttk.Scrollbar(details_text, command=details_text.yview)
details_text.config(yscrollcommand=text_scrollbar.set)
text_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


# --- Run the application ---
if __name__ == "__main__":
    ensure_csv_file_exists() # Make sure the CSV file is ready on startup
    root.mainloop()