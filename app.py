# app.py
import tkinter as tk
from tkinter import ttk, messagebox
import json
import re
import urllib.request  # part of stdlib; no external libs needed

API_URL = "http://localhost:5000/submit"

root = tk.Tk()
root.title("Purchase Form")

# ---------- FORM VARIABLES ----------
name_var = tk.StringVar()
email_var = tk.StringVar()
prodid_var = tk.StringVar()
descrip_var = tk.StringVar()
price_var = tk.StringVar()
online_var = tk.BooleanVar()

# ---------- LAYOUT ----------
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

# Name
ttk.Label(frame, text="Name:").grid(column=0, row=0, sticky=tk.W)
name_entry = ttk.Entry(frame, width=30, textvariable=name_var)
name_entry.grid(column=1, row=0)

# Email
ttk.Label(frame, text="Email:").grid(column=0, row=1, sticky=tk.W)
email_entry = ttk.Entry(frame, width=30, textvariable=email_var)
email_entry.grid(column=1, row=1)

# Product ID
ttk.Label(frame, text="Product ID:").grid(column=0, row=2, sticky=tk.W)
prodid_entry = ttk.Entry(frame, width=30, textvariable=prodid_var)
prodid_entry.grid(column=1, row=2)

# Description
ttk.Label(frame, text="Description:").grid(column=0, row=3, sticky=tk.W)
descrip_entry = ttk.Entry(frame, width=30, textvariable=descrip_var)
descrip_entry.grid(column=1, row=3)

# Price
ttk.Label(frame, text="Price:").grid(column=0, row=4, sticky=tk.W)
price_entry = ttk.Entry(frame, width=30, textvariable=price_var)
price_entry.grid(column=1, row=4)

# Online checkbox
online_cb = ttk.Checkbutton(frame, text="Online", variable=online_var)
online_cb.grid(columnspan=2, row=5, sticky=tk.W)

# Submit button
submit_btn = ttk.Button(frame, text="Submit", command=lambda: submit_form())
submit_btn.grid(row=6, columnspan=2, pady=(10, 0))


def validate() -> bool:
    """Return True if all fields are valid; otherwise show an error."""
    # Simple non-empty checks
    if not name_var.get().strip():
        messagebox.showerror("Validation Error", "Name cannot be empty.")
        return False

    email = email_var.get().strip()
    if not email or not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        messagebox.showerror("Validation Error", "Enter a valid email address.")
        return False

    product = prodid_var.get().strip()
    if not product:
        messagebox.showerror("Validation Error", "Product ID cannot be empty.")
        return False

    description = descrip_var.get().strip()
    if not description:
        messagebox.showerror("Validation Error", "Description cannot be empty.")
        return False

    price = price_var.get().strip()
    if not price:
        messagebox.showerror("Validation Error", "Price cannot be empty.")
        return False
    try:
        price = float(price_var.get())
        if price < 0 or price > 1000:
            messagebox.showerror(
                "Validation Error", "Price must be a number between 0 and 1000."
            )
            return False
    except ValueError:
        messagebox.showerror("Validation Error", "Enter a valid price.")
        return False

    return True


def collect_data() -> dict:
    """Return a dictionary that represents the form."""
    return {
        "name": name_var.get().strip(),
        "email": email_var.get().strip(),
        "product_id": prodid_var.get().strip(),
        "description": descrip_var.get().strip(),
        "price": float(price_var.get()),
        "online": online_var.get(),
    }


def submit_form() -> None:
    if not validate():
        return  # abort if validation failed

    payload = collect_data()
    json_payload = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        API_URL,
        data=json_payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read().decode())
            messagebox.showinfo("Success", f"Server replied: {result}")
    except urllib.error.HTTPError as e:
        error_msg = e.read().decode()
        messagebox.showerror("API Error", f"{e.code} - {error_msg}")
    except Exception as exc:
        messagebox.showerror("Connection Error", str(exc))


if __name__ == "__main__":
    root.mainloop()
