import tkinter as tk

TYPES = {1: "Shaped",
         2: "Shapeless",
         3: "Smelting"}


class TypeSelector:

    def __init__(self, master):
        self._master = master
        master.title("Minecraft Recipe Generator")
        master.geometry("300x100")

        # Widgets
        # labels
        self._type_label = tk.Label(master, text="Type")

        # radio buttons
        self._radio_input = tk.IntVar()
        self._radio_one = tk.Radiobutton(master, text="Shaped", variable=self._radio_input, value=1)
        self._radio_two = tk.Radiobutton(master, text="Shapeless", variable=self._radio_input, value=2)

        # button
        self._next_button = tk.Button(master, text="Next", command=self.next_step)

        # Layout
        self._type_label.grid(row=0, column=0, sticky=tk.W)
        self._radio_one.grid(row=1, column=0, sticky=tk.W)
        self._radio_two.grid(row=2, column=0, sticky=tk.W)
        self._next_button.grid(row=0, column=1, sticky=tk.E)

    def next_step(self):
        selected_item = self._radio_input.get()
        print(selected_item)

        if selected_item != 0:
            self._master.destroy()
            new_root = tk.Tk()
            new_gui = MainPage(new_root, TYPES[self._radio_input.get()])
        else:
            tk.Label(self._master, text="Please select a type.").grid(row=4)


class MainPage:

    def __init__(self, master, recipe_type):
        self._master = master
        master.title("Minecraft Recipe Generator")
        master.geometry("400x270")

        self._type = recipe_type

        # labels
        self._output_label = tk.Label(master, text="Output:")
        self._output_count_label = tk.Label(master, text="Count:")
        self._item_input_label = tk.Label(master, text="Item Input:")
        self._block_input_label = tk.Label(master, text="Block Input:")

        # conditional labels and entries
        if self._type == "Shaped":
            self._pattern_label = tk.Label(master, text="Pattern:")
            self._pattern_one_entry = tk.Entry(master)
            self._pattern_two_entry = tk.Entry(master)
            self._pattern_three_entry = tk.Entry(master)

        # entries
        self._output_entry = tk.Entry(master)
        self._output_count_entry = tk.Entry(master)
        self._item_key_entries = [tk.Entry(master, width=3) for _ in range(9)]
        self._block_key_entries = [tk.Entry(master, width=3) for _ in range(9)]
        self._item_input_entries = [tk.Entry(master, width=15) for _ in range(9)]
        self._block_input_entries = [tk.Entry(master, width=15) for _ in range(9)]

        # buttons
        self._preview_button = tk.Button(master, text="Preview", command=self.preview)
        self._create_button = tk.Button(master, text="Create", command=self.preview)

        # layout
        master.grid_columnconfigure(2, minsize=10)
        master.grid_columnconfigure(5, minsize=5)
        master.grid_rowconfigure(3, minsize=8)
        self._item_input_label.grid(row=4, sticky=tk.W)
        self._block_input_label.grid(row=4, column=3, sticky=tk.W)

        if self._type == "Shaped":
            self.shaped_layout()
        else:
            self.shapeless_layout()

        for index in range(9):
            self._item_key_entries[index].grid(row=4 + index, column=1, sticky=tk.W)
            self._item_input_entries[index].grid(row=4 + index, column=1, sticky=tk.E)
            self._block_key_entries[index].grid(row=4 + index, column=4, sticky=tk.W)
            self._block_input_entries[index].grid(row=4 + index, column=4, sticky=tk.E)

        self._preview_button.grid()

    def shaped_layout(self):
        self._output_label.grid(row=0, column=3, sticky=tk.W)
        self._output_count_label.grid(row=1, column=3, sticky=tk.W)

        self._output_entry.grid(row=0, column=4, sticky=tk.W)
        self._output_count_entry.grid(row=1, column=4, sticky=tk.W)

        self._pattern_label.grid(row=0, column=0, sticky=tk.W)
        self._pattern_one_entry.grid(row=0, column=1)
        self._pattern_two_entry.grid(row=1, column=1)
        self._pattern_three_entry.grid(row=2, column=1)

    def shapeless_layout(self):
        self._master.grid_columnconfigure(4, pad=30)

        self._output_label.grid(row=0, column=0, sticky=tk.W)
        self._output_count_label.grid(row=1, column=0, sticky=tk.W)

        self._output_entry.grid(row=0, column=1)
        self._output_count_entry.grid(row=1, column=1)

    def preview(self):
        pass

    def create(self):
        pass


class Preview:

    def __init__(self, master):
        self._master = master
        master.title("Preview")


if __name__ == "__main__":
    root = tk.Tk()
    gui = TypeSelector(root)
    root.mainloop()
