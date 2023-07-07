
import tkinter as tk


root = tk.Tk()
root.title(" Grocery List")
root.geometry("800x800")

def retrievedata():
    ''' get data stored '''
    global list_data
    list_data = []
    try:
      with open("save.txt", "r", encoding="utf-8") as file:
       for f in file:
        listbox.insert(tk.END, f.strip())
        list_data.append(f.strip())
        print(list_data)
    except:
        pass

def reload_data():
    listbox.delete(0, tk.END)
    for d in list_data:
        listbox.insert(0, d)


def add_item(event=1):
    global list_data
    if content.get() != "":
        listbox.insert(tk.END, content.get())
        list_data.append(content.get())
        content.set("")


def delete():
    global list_data
    listbox.delete(0, tk.END)
    list_data = []


def delete_selected():

    try:
        selected = listbox.get(listbox.curselection())
        listbox.delete(listbox.curselection())
        list_data.pop(list_data.index(selected))
        # reload_data()
        # # listbox.selection_clear(0, END)
        listbox.selection_set(0)
        listbox.activate(0)
        listbox.event_generate("<<ListboxSelect>>")
        print(listbox.curselection())
    except:
        pass



def quit():
 global root
 with open("save.txt", "w", encoding="utf-8") as file:
  for d in list_data:
   file.write(d + "\n")
 root.destroy()

# LISTBOX

content = tk.StringVar()
entry = tk.Entry(root, textvariable=content)
entry.pack()

button = tk.Button(root, text="Add Item", command=add_item)
button.pack()

button_delete = tk.Button(text="Delete", command=delete)
button_delete.pack()

button_delete_selected = tk.Button(text="Delete Selected", command=delete_selected)
button_delete_selected.pack()

listbox = tk.Listbox(root)
listbox.pack()
entry.bind("<Return>", add_item)

bquit = tk.Button(root, text="Quit and save", command=quit)
bquit.pack()

retrievedata()
root.mainloop()