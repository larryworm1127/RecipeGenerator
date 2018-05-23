from tkinter import *

root = Tk()

root.grid_columnconfigure(2, minsize=8)

Label(root, text="Output").grid(row=1, sticky="W", columnspan=2)
Label(root, text="Output Count").grid(row=1, column=3, sticky="W")
Label(root, text="Pattern").grid(row=3, sticky="W")
Label(root, text="Item Input").grid(row=6, sticky="W")

output = Entry(root).grid(row=1, column=1)
output_count = Entry(root).grid(row=1, column=4)
pattern_row_one = Entry(root).grid(row=3, column=1)
pattern_row_two = Entry(root).grid(row=4, column=1)
pattern_row_three = Entry(root).grid(row=5, column=1)


item_input_count = 1
block_input_count = 1

item_input = []
block_input = []
for column in range(item_input_count):
    item_input.append(Entry(root).grid(row=6, column=column + 1))

root.mainloop()
