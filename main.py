import tkinter as tk

root = tk.Tk()

v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python

types = ["Shaped", "Shapeless"]

tk.Label(root,
         text="""Choose the type of recipe:""",
         justify=tk.LEFT,
         padx=20).pack()

for val, language in enumerate(types):
    tk.Radiobutton(root,
                   text=language,
                   padx=20,
                   variable=v,
                   value=val).pack(anchor=tk.W)

print(v.get())


master = tk.Tk()
tk.Label(master, text="Output").grid(row=0)

e1 = tk.Entry(master)

e1.grid(row=0, column=1)
print(e1.get())
root.mainloop()
