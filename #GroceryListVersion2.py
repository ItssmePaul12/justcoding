#GroceryListVersion2.py
#Make sure to download item_cost.txt file from BookStack
#Copy and Paste this into the file name box: C:\Users\SERN_INTERN\Downloads\item_cost.txt
import tkinter as tk

grocery_items = []

def load_list():
    filename = entry_filename.get()
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                item = line.strip()
                grocery_items.append({"name": item, "quantity": 0, "price": 0.0})
            update_listbox()
    except FileNotFoundError:
        pass

def update_item():
    selected_index = listbox.curselection()
    if selected_index:
        quantity = int(entry_quantity.get())
        price = float(entry_price.get())
        
        item = grocery_items[selected_index[0]]
        item["quantity"] = quantity
        item["price"] = price
        
        update_listbox()

def remove_item():
    selected_indices = listbox.curselection()
    if selected_indices:
        for index in reversed(selected_indices):
            grocery_items.pop(index)
        update_listbox()
        
def update_listbox():
    listbox.delete(0, tk.END)
    for item in grocery_items:
        name = item["name"]
        quantity = item["quantity"]
        price = item["price"]
        item_text = f"{name} - {quantity} x ${price:.2f}"
        listbox.insert(tk.END, item_text)
    calculate_cost()
    
def calculate_cost():
    total_cost = 0.0
    for item in grocery_items:
        quantity = item["quantity"]
        price = item["price"]
        total_cost += quantity * price
    cost_label.config(text=f"Total Cost: ${total_cost:.2f}")
    
window = tk.Tk()
window.title("Grocery List")

frame_entry = tk.Frame(window)
frame_entry.pack(pady=10)

label_filename = tk.Label(frame_entry, text="File Name:")
label_filename.pack(side=tk.LEFT)
entry_filename = tk.Entry(frame_entry, width=30)
entry_filename.pack(side=tk.LEFT)

load_button = tk.Button(window, text="Load List", command=load_list)
load_button.pack(pady=10)

scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(window)
listbox.pack(pady=10)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

frame_entry = tk.Frame(window)
frame_entry.pack(pady=10)

label_quantity = tk.Label(frame_entry, text="Quantity:")
label_quantity.pack(side=tk.LEFT)
entry_quantity = tk.Entry(frame_entry, width=10)
entry_quantity.pack(side=tk.LEFT)

label_price = tk.Label(frame_entry, text="Price ($):")
label_price.pack(side=tk.LEFT)
entry_price = tk.Entry(frame_entry, width=10)
entry_price.pack(side=tk.LEFT)

frame_buttons = tk.Frame(window)
frame_buttons.pack()

update_button = tk.Button(frame_buttons, text="Update Item", command=update_item)
update_button.pack(side=tk.LEFT, padx=5)
remove_button = tk.Button(frame_buttons, text="Remove Item", command=remove_item)
remove_button.pack(side=tk.LEFT)

cost_label = tk.Label(window, text="Total Cost: $0.00")
cost_label.pack()

calculate_button = tk.Button(window, text="Calculate Cost", command=calculate_cost)
calculate_button.pack(pady=10)

window.mainloop()
    
    