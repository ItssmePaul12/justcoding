import tkinter as tk

items = {
    "Yogurt $1.49": 1.49,
    "Chicken $5.99": 5.99,
    "Beef $8.99": 8.99,
    "Pork $6.99": 6.99,
    "Fish $9.99": 9.99,
    "Shrimp $12.99": 12.99,
    "Lobster $24.99": 24.99,
    "Crab $14.99": 14.99,
    "Salmon $11.99": 11.99,
    "Tuna $8.99": 8.99,
    "Sardines $3.99": 3.99,
    "Peanut butter $3.99": 3.99,
    "Jelly $2.99": 2.99,
    "Honey $4.99": 4.99,
    "Cereal $4.49": 4.49,
    "Oatmeal $3.99": 3.99,
    "Granola $5.99": 5.99,
    "Pancake mix $2.99": 2.99,
    "Syrup $3.99": 3.99,
    "Flour $2.99": 2.99,
    "Sugar $1.99": 1.99,
    "Salt $0.99": 0.99,
    "Pepper $1.49": 1.49,
    "Garlic $1.99": 1.99,
    "Onion $0.99": 0.99,
    "Potato $2.99": 2.99,
    "Tomato $1.99": 1.99,
    "Lettuce $1.49": 1.49,
    "Spinach $2.49": 2.49,
    "Kale $2.99": 2.99,
    "Carrots $1.99": 1.99,
    "Broccoli $2.99": 2.99,
    "Cauliflower $3.49": 3.49,
    "Cucumber $0.99": 0.99,
    "Bell pepper $1.99": 1.99,
    "Mushrooms $2.99": 2.99,
    "Zucchini $1.99": 1.99,
    "Squash $2.49": 2.49,
    "Avocado $1.99": 1.99,
    "Bananas $0.69": 0.69,
    "Apples $1.49": 1.49,
    "Oranges $1.99": 1.99,
    "Lemons $0.99": 0.99,
    "Limes $0.49": 0.49,
    "Grapes $2.99": 2.99,
    "Strawberries $3.99": 3.99,
    "Blueberries $4.99": 4.99,
    "Raspberries $5.99": 5.99,
    "Blackberries $4.99": 4.99,
    "Pineapple $2.99": 2.99,
    "Watermelon $4.99": 4.99,
    "Cantaloupe $2.99": 2.99,
    "Honeydew $3.99": 3.99,
    "Grapefruit $1.49": 1.49,
    "Peaches $2.99": 2.99,
    "Plums $2.49": 2.49,
    "Nectarines $2.99": 2.99,
    "Apricots $3.99": 3.99,
    "Cherries $4.99": 4.99,
    "Pears $2.99": 2.99,
    "Grape juice $3.99": 3.99,
    "Orange juice $2.99": 2.99,
    "Apple juice $2.99": 2.99,
    "Cranberry juice $3.49": 3.49,
    "Grapefruit juice $2.99": 2.99,
    "Lemonade $2.49": 2.49,
    "Iced tea $1.99": 1.99,
    "Soda $1.49": 1.49,
    "Beer $8.99": 8.99,
    "Wine $12.99": 12.99,
    "Whiskey $24.99": 24.99,
    "Vodka $19.99": 19.99,
    "Rum $16.99": 16.99,
    "Tequila $29.99": 29.99,
    "Coffee $6.99": 6.99,
    "Tea $3.99": 3.99,
    "Hot chocolate $2.99": 2.99,
    "Ice cream $4.99": 4.99,
    "Frozen vegetables $2.99": 2.99,
    "Frozen fruits $3.99": 3.99,
    "Frozen pizza $5.99": 5.99,
    "Frozen dinners $3.99": 3.99,
    "Snacks $1.99": 1.99,
    "Candy $0.99": 0.99,
    "Nuts $4.99": 4.99,
    "Dried fruit $3.99": 3.99,
    "Crackers $2.99": 2.99,
    "Chips $2.49": 2.49,
    "Popcorn $1.99": 1.99,
    "Cookies $3.49": 3.49,
    "Cake mix $2.99": 2.99,
    "Frosting $2.49": 2.49,
    "Brownie mix $2.99": 2.99,
    "Pudding mix $1.99": 1.99,
    "Jello $1.49": 1.49
}

def add_item():
    item = item_var.get()
    quantity = int(quantity_var.get())
    
    if item in items:
        cost = items[item] * quantity
        item_list.append((item, quantity, cost))
        total_cost.set(sum([item[2] for item in item_list]))

def remove_item():
    selected_item = item_listbox.get(tk.ACTIVE)
    for item in item_list:
        if item[0] == selected_item:
         item_list.remove(item)
         break
    total_cost.set(sum([item[2] for item in item_list]))

window = tk.Tk()
window.title("Grocery List")

item_list = []

item_var = tk.StringVar(window)
item_var.set("Yogurt $1.49")
item_label = tk.Label(window, text="Item:")
item_optionmenu = tk.OptionMenu(window, item_var, *items.keys())
item_label.pack()
item_optionmenu.pack()

quantity_var = tk.StringVar(window)
quantity_var.set("1")
quantity_label = tk.Label(window, text="Quantity:")
quantity_entry = tk.Entry(window, textvariable=quantity_var)
quantity_label.pack()
quantity_entry.pack()

add_button = tk.Button(window, text="Add Item", command=add_item)
add_button.pack()
remove_button = tk.Button(window, text="Remove Item", command=remove_item)
remove_button.pack()

item_listbox = tk.Listbox(window)
item_listbox.pack()

total_cost = tk.DoubleVar(window)
total_cost_label = tk.Label(window, text="Total Cost: $")
total_cost_value = tk.Label(window, textvariable=total_cost)
total_cost_label.pack()
total_cost_value.pack()

window.mainloop()
