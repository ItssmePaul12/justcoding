from tkinter import ttk
import tkinter as tk
root = tk.Tk()
root.geometry('500x300')
root.title('Server Window')
root.wm_resizable(width=False, height=False)

# Create display area for selected items

display = tk.Text(root, height=10, width=30, bg='Orange', bd=4)
display.grid(row=1, column=3)

price_display = tk.Text(root, height=3, width=15, bg='Orange', bd=4)
price_display.grid(row=3, column=3)
#====================== Functions =================================
def fireFood():
    # Every time a new item is selected i want a new total to be calculated and displayed
    global menu
    global price_display
    global display
    global select_option
    total = 0
    prices = []
    # this inserts food item onto display
    display.insert(tk.END,options.get())
    prices.append([options.get(), menu[options.get()]])

    for x in prices:
        total = total + float(x[1])

    # this shows price on lower display
        price_display.insert(tk.END, total)

    total += float(menu[options.get()])

def addList(arr):
    cost = 0
    arr.remove('\n')
    total = [sum(float(x) for x in arr)]
    for x in total:
        cost += x
    return cost
#======================================================================

# Create a Dictionary of items to be displayed in Combobox
menu = {'fries ':5, 'Burger ':10, 'Pizza ':15, 'Chicken ':8, 'Fish ':7.50}
menu_list = [x for x in menu.keys()]
menu_prices = [y for y in menu.values()]
options = ttk.Combobox(values=menu_list)

# Set default value for the combobox to 'Menu' to function as a pseudo label
options.set('Menu')
options.grid(row=0, column=0)

# Create a button that when pressed will get the value of combobox
select_option = ttk.Button(root, text='Select', command=fireFood)
select_option.grid(row=0, column=1)

root.mainloop()