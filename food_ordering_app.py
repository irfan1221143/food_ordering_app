import tkinter as tk
from tkinter import messagebox

# -------------------------
# MENU DATA (Dictionary)
# -------------------------
# Keys  → item names shown to user
# Values → price of each item
menu = {
    "Burger(Price = 5.99)": 5.99,
    "Pizza(Price = 8.99)": 8.99,
    "Salad(Price = 4.49)": 4.49,
    "Fries(Price = 2.99)": 2.99,
    "Soda(Price = 1.99)": 1.99
}

# Dictionary to store selected items and their quantity
cart = {}

# -------------------------
# FUNCTION: Add selected item to cart
# -------------------------
def add_to_cart():
    # Get the currently selected item from menu listbox
    selected = menu_listbox.get(tk.ACTIVE)
    
    if selected:
        # If item already added earlier, increase quantity
        if selected in cart:
            cart[selected] += 1
        else:
            # Add item to cart with quantity 1
            cart[selected] = 1
        
        # Update cart display text
        update_cart_display()
        
        # Popup message
        messagebox.showinfo("Added", f"Added {selected} to cart.")

# -------------------------
# FUNCTION: Update cart display and show total bill
# -------------------------
def update_cart_display():
    cart_text.delete(1.0, tk.END)  # Clear previous text
    total = 0  # Stores final calculated bill
    
    # Loop through all items added in cart
    for item, qty in cart.items():
        price = menu[item] * qty
        cart_text.insert(tk.END, f"{item} x{qty} - ${price:.2f}\n")
        total += price
    
    # Display total bill at the bottom
    cart_text.insert(tk.END, f"\nTotal: ${total:.2f}")

# -------------------------
# FUNCTION: Place the order
# -------------------------
def place_order():
    if not cart:
        # If no items in cart
        messagebox.showwarning("Empty Cart", "Your cart is empty!")
        return
    
    # Ask user confirmation before placing order
    confirm = messagebox.askyesno("Confirm Order", "Place the order?")
    if confirm:
        messagebox.showinfo("Order Placed", "Thank you! Your order has been placed.")
        cart.clear()           # Remove all items after placing order
        update_cart_display()  # Refresh cart display

# -------------------------
# MAIN WINDOW SETTINGS
# -------------------------
root = tk.Tk()
root.title("Food Ordering App")
root.geometry("400x400")

# -------------------------
# MENU DISPLAY SECTION
# -------------------------
tk.Label(root, text="Menu", font=("Arial", 12, "bold")).pack()

# Listbox to show all available foods
menu_listbox = tk.Listbox(root, height=5)
for item in menu:
    menu_listbox.insert(tk.END, item)
menu_listbox.pack()

# Button to add item to cart
tk.Button(root, text="Add to Cart", command=add_to_cart).pack()

# -------------------------
# CART DISPLAY SECTION
# -------------------------
tk.Label(root, text="Your Cart", font=("Arial", 12, "bold")).pack()

# Text widget to show cart items and total bill
cart_text = tk.Text(root, height=10, width=40)
cart_text.pack()

# Button to place final order
tk.Button(root, text="Place Order", command=place_order).pack()

# -------------------------
# START THE APPLICATION
# -------------------------
root.mainloop()
