"""
Python module containing all class for Tkinter GUI

Created on May 24, 2018
@author: Larry Shi
"""

# general imports
import tkinter as tk
from tkinter import filedialog, messagebox

from recipe_generator.json_generator import Json
from recipe_generator.recipe import ShapedRecipe, ShapelessRecipe

# constants
LABEL_FONT = ("Courier", 14)
DEF_FONT = ("Courier", 12)
TYPES = {1: "Shaped",
         2: "Shapeless",
         3: "Smelting"}


class TypeSelector:

    def __init__(self, master):
        self._master = master
        self._dir_path = ''

        master.title("Minecraft Recipe Generator")
        master.geometry("300x140")

        # WIDGETS
        # labels
        self._type_label = tk.Label(master, text="Type", font=LABEL_FONT)

        # radio buttons
        self._choice = tk.IntVar()
        self._radio_one = tk.Radiobutton(master, text="Shaped", variable=self._choice, value=1, font=DEF_FONT)
        self._radio_two = tk.Radiobutton(master, text="Shapeless", variable=self._choice, value=2, font=DEF_FONT)

        # entries
        self._file_path_entry = tk.Entry(master)

        # buttons
        self._next_button = tk.Button(master, text="Next", command=self.next_step, font=DEF_FONT)
        self._browse_button = tk.Button(master, text="Browse", command=self.browse_csv, font=DEF_FONT)

        # LAYOUT
        master.grid_columnconfigure(0, minsize=10)
        master.grid_columnconfigure(2, minsize=20)
        master.grid_rowconfigure(4, minsize=10)

        self._type_label.grid(row=0, column=1, sticky=tk.W)
        self._radio_one.grid(row=1, column=1, sticky=tk.W)
        self._radio_two.grid(row=2, column=1, sticky=tk.W)
        self._next_button.grid(row=3, column=1, sticky=tk.W)
        self._browse_button.grid(row=1, column=3)
        self._file_path_entry.grid(row=0, column=3)

    def next_step(self):
        selected_item = self._choice.get()

        if selected_item == 0:
            self._master.geometry("340x180")
            tk.Label(self._master, text="Please select a type.", font=DEF_FONT).grid(row=5, column=1, columnspan=3,
                                                                                     sticky=tk.W)
        elif self._dir_path == '':
            self._master.geometry("340x180")
            tk.Label(self._master, text="Please choose a file directory", font=DEF_FONT).grid(row=5, column=1,
                                                                                              columnspan=4, sticky=tk.W)
        else:
            self._master.destroy()
            new_root = tk.Tk()
            MainPage(new_root, TYPES[self._choice.get()], self._dir_path)

    def browse_csv(self):
        self._dir_path = tk.filedialog.askdirectory()
        self._file_path_entry.insert(0, self._dir_path)


class MainPage:

    def __init__(self, master, recipe_type, dir_path):
        # VARIABLES
        # gui related
        self._master = master
        self._type = recipe_type

        master.title("Minecraft Recipe Generator")
        master.geometry("580x340")

        # directory path
        self._dir_path = dir_path

        # user entry
        self._output = ''
        self._output_count = 1
        self._item_input = {}
        self._block_input = {}
        self._pattern = []

        # WIDGETS
        # labels
        self._output_label = tk.Label(master, text="Output:", font=LABEL_FONT)
        self._output_count_label = tk.Label(master, text="Count:", font=LABEL_FONT)
        self._item_input_label = tk.Label(master, text="Item Input:", font=LABEL_FONT)
        self._block_input_label = tk.Label(master, text="Block Input:", font=LABEL_FONT)

        # entries
        self._output_entry = tk.Entry(master)
        self._output_count_entry = tk.Entry(master)
        self._output_count_entry.insert(0, '1')
        self._item_input_entries = [tk.Entry(master) for _ in range(9)]
        self._block_input_entries = [tk.Entry(master) for _ in range(9)]

        # shaped labels and entries
        if self._type == "Shaped":
            self._pattern_label = tk.Label(master, text="Pattern:", font=LABEL_FONT)
            self._pattern_entries = [tk.Entry(master) for _ in range(3)]

            self._item_key_entries = [tk.Entry(master, width=3) for _ in range(9)]
            self._block_key_entries = [tk.Entry(master, width=3) for _ in range(9)]

            for index in range(9):
                self._item_input_entries[index].configure(width=15)
                self._block_input_entries[index].configure(width=15)

        # buttons
        self._preview_button = tk.Button(master, text="Preview", command=self.preview, font=DEF_FONT)
        self._create_button = tk.Button(master, text="Create", command=self.create, font=DEF_FONT)

        # LAYOUT
        # rows and columns config
        master.grid_columnconfigure(2, minsize=15)
        master.grid_columnconfigure(5, minsize=5)
        master.grid_rowconfigure(3, minsize=8)
        master.grid_rowconfigure(13, minsize=8)

        # labels grid
        self._item_input_label.grid(row=4, sticky=tk.W)
        self._block_input_label.grid(row=4, column=3, sticky=tk.W)

        # item inputs and block inputs entries grid
        for index in range(9):
            self._item_input_entries[index].grid(row=4 + index, column=1, sticky=tk.W)
            self._block_input_entries[index].grid(row=4 + index, column=4, sticky=tk.W)

        # conditional item grid
        if self._type == "Shaped":
            self.shaped_layout()
        else:
            self.shapeless_layout()

        # buttons grid
        self._preview_button.grid(row=14, column=0)
        self._create_button.grid(row=14, column=1, sticky=tk.W)

    def shaped_layout(self):
        # labels grid
        self._output_label.grid(row=0, column=3, sticky=tk.W)
        self._output_count_label.grid(row=1, column=3, sticky=tk.W)
        self._pattern_label.grid(row=0, column=0, sticky=tk.W)

        # entries grid
        self._output_entry.grid(row=0, column=4, sticky=tk.W)
        self._output_count_entry.grid(row=1, column=4, sticky=tk.W)

        # pattern entries grid
        row = 0
        for entry in self._pattern_entries:
            entry.grid(row=row, column=1)
            row += 1

        # item input and block input grid and config
        for index in range(9):
            self._item_input_entries[index].grid(sticky=tk.E)
            self._block_input_entries[index].grid(sticky=tk.E)
            self._item_key_entries[index].grid(row=4 + index, column=1, sticky=tk.W)
            self._block_key_entries[index].grid(row=4 + index, column=4, sticky=tk.W)

    def shapeless_layout(self):
        # row and column config
        self._master.grid_columnconfigure(4, pad=30)

        # labels grid
        self._output_label.grid(row=0, column=0, sticky=tk.W)
        self._output_count_label.grid(row=1, column=0, sticky=tk.W)

        # entries grid
        self._output_entry.grid(row=0, column=1)
        self._output_count_entry.grid(row=1, column=1)

    def preview(self):
        pass

    def create(self):
        recipe_json = self.create_json()
        complete = recipe_json.generator(self._dir_path)

        if complete:
            tk.messagebox.showinfo("Success!", "The recipe file has been created.")
        else:
            tk.messagebox.showerror("Error!", "The creation of the file has failed. Check for any unfilled blanks.")

    def create_json(self):
        # retrieve data from entries
        self._output = self._output_entry.get()
        self._output_count = self._output_count_entry.get()
        name = self._output.split(':')[1] if self._output != '' else ''

        for index in range(9):
            # check if the item input entries are filled or not
            item_key = self._item_key_entries[index].get()
            item = self._item_input_entries[index].get()
            if item_key != '' and item != '':
                self._item_input[item_key] = item

            # check if the block input entries are filled or not
            block_key = self._block_key_entries[index].get()
            block = self._block_input_entries[index].get()
            if block_key != '' and block != '':
                self._block_input[block_key] = block

        # create json objects based on its recipe type
        if self._type == "Shaped":
            pattern = [entry.get() for entry in self._pattern_entries]
            recipe_object = ShapedRecipe(name, self._output, self._item_input, self._block_input, self._pattern,
                                         self._output_count)
            json_object = Json(recipe_object)
        elif self._type == "Shapeless":
            recipe_object = ShapelessRecipe(name, self._output, self._item_input, self._block_input, self._output_count)
            json_object = Json(recipe_object)
        else:
            json_object = None

        # return json object for other uses
        return json_object


class Preview:

    def __init__(self, master):
        self._master = master
        master.title("Preview")


if __name__ == "__main__":
    root = tk.Tk()
    gui = TypeSelector(root)
    root.mainloop()
