"""
Python module containing all class for Tkinter GUI

@date: 5/25/2018
@author: Larry Shi
"""

# general imports
from __future__ import absolute_import

import tkinter as tk

from os.path import expanduser
from tkinter import filedialog, messagebox

from .util import create_shaped_json, create_shapeless_json, verify_data, STATE
from . import get_logger

# constants
LABEL_FONT = ("Courier", 14)
DEF_FONT = ("Courier", 12)
TYPES = {1: "Shaped", 2: "Shapeless", 3: "Smelting"}

# global variables
preview_open = False


# classes
class IntroPage:
    """Class for Type Selecting Page"""

    def __init__(self, master, directory):
        # VARIABLES
        self._master = master
        self._dir_path = directory
        self._logger = get_logger('root.IntroPage')

        master.title("Minecraft Recipe Generator")
        master.geometry("300x140")

        # WIDGETS
        self._logger.info("Initialize Widgets")

        # labels
        self._type_label = tk.Label(master, text="Type", font=LABEL_FONT)

        # radio buttons
        self._choice = tk.IntVar()
        self._radio_one = tk.Radiobutton(master, text="Shaped",
                                         variable=self._choice, value=1,
                                         font=DEF_FONT)
        self._radio_two = tk.Radiobutton(master, text="Shapeless",
                                         variable=self._choice, value=2,
                                         font=DEF_FONT)

        # entries
        self._file_path_entry = tk.Entry(master)
        self._file_path_entry.insert(0, self._dir_path)

        # buttons
        self._next_button = tk.Button(master, text="Next",
                                      command=self.next_step, font=DEF_FONT)
        self._browse_button = tk.Button(master, text="Browse",
                                        command=self.browse_csv, font=DEF_FONT)

        # LAYOUT
        self._logger.info("Initialize GUI layout")

        # row and column config
        master.grid_columnconfigure(0, minsize=10)
        master.grid_columnconfigure(2, minsize=20)
        master.grid_rowconfigure(4, minsize=10)

        # widget grid
        self._type_label.grid(row=0, column=1, sticky=tk.W)
        self._radio_one.grid(row=1, column=1, sticky=tk.W)
        self._radio_two.grid(row=2, column=1, sticky=tk.W)
        self._next_button.grid(row=3, column=1, sticky=tk.W)
        self._browse_button.grid(row=1, column=3)
        self._file_path_entry.grid(row=0, column=3)

    def next_step(self):
        """Event handler for Next button"""

        self._logger.info("Next button pressed")
        selected_item = self._choice.get()

        # user didn't select recipe type
        if selected_item == 0:
            self._logger.error("Recipe type not selected")
            tk.messagebox.showerror("Error!", "Please select a recipe type.")

        # user didn't select a file path
        elif self._dir_path == '':
            self._logger.error("No directory path selected")
            tk.messagebox.showerror("Error!", "Please choose a file directory.")

        # user is directed to main page
        else:
            self._logger.info("Start main page, destroy type select page")
            self._master.destroy()
            new_root = tk.Tk()
            MainPage(new_root, TYPES[self._choice.get()], self._dir_path)

    def browse_csv(self):
        """ Event handler for Browse button"""

        self._logger.info("Browse files")

        # create file dialog and update file path entry text
        self._dir_path = tk.filedialog.askdirectory()
        self._file_path_entry.delete(0, 'end')
        self._file_path_entry.insert(0, self._dir_path)


class MainPage:
    """Class for Main Page"""

    def __init__(self, master, recipe_type, dir_path):
        # VARIABLES
        # gui related
        self._master = master
        self._type = recipe_type

        master.title("Minecraft Recipe Generator")
        master.geometry("580x340")
        master.protocol("WM_DELETE_WINDOW", self.confirm_close)

        # other variables
        self._dir_path = dir_path
        self._preview_class = None
        self._logger = get_logger('root.MainPage')

        # WIDGETS
        self._logger.info("Initialize widgets")

        # labels
        self._output_label = tk.Label(master, text="Output:", font=LABEL_FONT)
        self._output_count_label = tk.Label(master, text="Count:",
                                            font=LABEL_FONT)
        self._item_input_label = tk.Label(master, text="Item Input:",
                                          font=LABEL_FONT)
        self._block_input_label = tk.Label(master, text="Block Input:",
                                           font=LABEL_FONT)

        # entries
        self._output_entry = tk.Entry(master)
        self._output_count_entry = tk.Entry(master)
        self._output_count_entry.insert(0, '1')
        self._item_input_entries = [tk.Entry(master) for _ in range(9)]
        self._block_input_entries = [tk.Entry(master) for _ in range(9)]

        # shaped labels and entries
        self._pattern_label = tk.Label(master, text="Pattern:", font=LABEL_FONT)
        self._pattern_entries = [[tk.Entry(master, width=5) for _ in range(3)]
                                 for _ in range(3)]

        self._item_key_entries = [tk.Entry(master, width=3) for _ in range(9)]
        self._block_key_entries = [tk.Entry(master, width=3) for _ in range(9)]

        # buttons
        self._preview_button = tk.Button(master, text="Preview",
                                         command=self.preview, font=DEF_FONT)
        self._create_button = tk.Button(master, text="Create",
                                        command=self.create, font=DEF_FONT)
        self._back_button = tk.Button(master, text="Back", command=self.back,
                                      font=DEF_FONT)
        self._reset_button = tk.Button(master, text="Reset", command=self.reset,
                                       font=DEF_FONT)

        # LAYOUT
        self._logger.info("Initialize GUI layout")

        # rows and columns config
        master.grid_columnconfigure(2, minsize=15)
        master.grid_columnconfigure(5, minsize=5)
        master.grid_rowconfigure(3, minsize=8)
        master.grid_rowconfigure(13, minsize=15)

        # labels grid
        self._item_input_label.grid(row=4, sticky=tk.W)
        self._block_input_label.grid(row=4, column=3, sticky=tk.W)

        # item inputs and block inputs entries grid
        for index in range(9):
            self._item_input_entries[index].grid(row=4 + index, column=1,
                                                 sticky=tk.W)
            self._block_input_entries[index].grid(row=4 + index, column=4,
                                                  sticky=tk.W)

        # conditional item grid
        if self._type == "Shaped":
            self.shaped_layout()
        else:
            self.shapeless_layout()

        # buttons grid
        self._preview_button.grid(row=14, column=1, sticky=tk.W)
        self._create_button.grid(row=14, column=3, sticky=tk.W)
        self._back_button.grid(row=14, column=0)
        self._reset_button.grid(row=14, column=4, sticky=tk.W)

    def shaped_layout(self):
        """Helper function for setting up GUI for shaped recipe"""

        self._logger.info("Initialize shaped recipe GUI layout")

        # row and column config
        self._master.grid_columnconfigure(1, pad=30)

        # labels grid
        self._output_label.grid(row=0, column=3, sticky=tk.W)
        self._output_count_label.grid(row=1, column=3, sticky=tk.W)
        self._pattern_label.grid(row=0, column=0, sticky=tk.W)

        # entries grid
        self._output_entry.grid(row=0, column=4, sticky=tk.W)
        self._output_count_entry.grid(row=1, column=4, sticky=tk.W)

        # pattern entries grid
        for row in range(3):
            for column in range(3):
                if column == 0:
                    self._pattern_entries[row][column].grid(row=row, column=1,
                                                            sticky=tk.W)
                elif column == 1:
                    self._pattern_entries[row][column].grid(row=row, column=1)
                else:
                    self._pattern_entries[row][column].grid(row=row, column=1,
                                                            sticky=tk.E)

        # item input and block input grid and config
        for index in range(9):
            self._item_input_entries[index].configure(width=15)
            self._block_input_entries[index].configure(width=15)
            self._item_input_entries[index].grid(sticky=tk.E)
            self._block_input_entries[index].grid(sticky=tk.E)
            self._item_key_entries[index].grid(row=4 + index, column=1,
                                               sticky=tk.W)
            self._block_key_entries[index].grid(row=4 + index, column=4,
                                                sticky=tk.W)

    def shapeless_layout(self):
        """Helper function for setting up GUI for shapeless recipe"""

        self._logger.info("Initialize shapeless recipe GUI layout")

        # row and column config
        self._master.grid_columnconfigure(4, pad=30)

        # labels grid
        self._output_label.grid(row=0, column=0, sticky=tk.W)
        self._output_count_label.grid(row=1, column=0, sticky=tk.W)

        # entries grid
        self._output_entry.grid(row=0, column=1)
        self._output_count_entry.grid(row=1, column=1)

    def preview(self):
        """Event handler for Preview button"""

        global preview_open

        self._logger.info("Preview")

        # get json object
        json_object = self.collect_and_verify_data()

        # destroy opened preview window
        if preview_open:
            self._preview_class.master.destroy()

        # create preview window
        new_root = tk.Tk()
        self._preview_class = PreviewPage(new_root, json_object)
        preview_open = True

    def back(self):
        """Event handler for Back button"""

        self._logger.info("Back")
        message = "All the data typed in will be lost if you choose to go back!"
        choice = tk.messagebox.askokcancel("Warning!", message)

        # return to type select page if user confirms the choice
        if choice:
            self._master.destroy()

            new_root = tk.Tk()
            IntroPage(new_root, self._dir_path)

    def reset(self):
        """Event handler for Reset Button"""
        self._logger.info("Reset")
        message = "All the data typed in will be lost if you choose to reset!"
        choice = tk.messagebox.askokcancel("Warning!", message)

        if choice:
            self._master.destroy()

            new_root = tk.Tk()
            MainPage(new_root, self._type, self._dir_path)

    def create(self):
        """Event handler for Create button"""

        self._logger.info("Create")
        recipe_json = self.collect_and_verify_data()

        # create the json file
        complete = recipe_json.generator(self._dir_path)

        if complete:
            message = "The recipe file has been created."
            tk.messagebox.showinfo("Success!", message)
        else:
            message = "The creation of the file has failed."
            tk.messagebox.showerror("Error!", message)

    def collect_and_verify_data(self):
        """Collect the data from entries and return the data to the caller"""

        self._logger.info("Collect and verify data")

        # Retrieve Data from Entries
        # outputs
        output = self._output_entry.get()
        output_count = self._output_count_entry.get() if \
            self._output_count_entry.get() != '' else 1

        # items and blocks
        items, blocks = [], []
        for item_entry, block_entry in zip(self._item_input_entries,
                                           self._block_input_entries):
            if item_entry.get() != '':
                items.append(item_entry.get())
            if block_entry.get() != '':
                blocks.append(block_entry.get())

        # Actions for Shaped Recipe
        if self._type == "Shaped":

            # item keys and block keys
            item_keys, block_keys = [], []
            for item_entry, block_entry in zip(self._item_key_entries,
                                               self._block_key_entries):
                if item_entry.get() != '':
                    item_keys.append(item_entry.get())
                if block_entry.get() != '':
                    block_keys.append(block_entry.get())

            # pattern
            pattern = []
            for row in range(3):
                string_row = ""
                for column in range(3):
                    entry_input = self._pattern_entries[row][column].get()
                    if entry_input == '':
                        string_row += ' '
                    else:
                        string_row += entry_input

                pattern.append(string_row)

            # verify the data
            state, message = verify_data(self._type, output, items, blocks,
                                         item_keys, block_keys, pattern)
            if STATE[state] == "PASS":
                self._logger.info("Data verified")
                recipe_json = create_shaped_json(output.split(':')[1], output,
                                                 output_count, items, blocks,
                                                 item_keys, block_keys, pattern)
            else:
                self._logger.error(message)
                tk.messagebox.showerror("Error!", message)
                raise Exception(message)

        # Actions for Shapeless Recipe
        else:
            # verify the data
            state, message = verify_data(self._type, output, items, blocks)
            if STATE[state] == "PASS":
                self._logger.info("Data verified")
                recipe_json = create_shapeless_json(output.split(':')[1],
                                                    output, output_count, items,
                                                    blocks)
            else:
                self._logger.error(message)
                tk.messagebox.showerror("Error!", message)
                raise Exception(message)

        return recipe_json

    def confirm_close(self):
        """Event handler for Exiting the GUI"""

        self._master.destroy()

        # close preview window if it is open
        if preview_open:
            self._preview_class.master.destroy()

        exit()


class PreviewPage:
    """Class for Preview Page"""

    def __init__(self, master, json_object):
        # VARIABLES
        # gui related
        self.master = master
        master.title("Preview")
        master.geometry("580x370")
        master.protocol("WM_DELETE_WINDOW", self.confirm_close)

        # other variable
        self._json_object = json_object
        self._logger = get_logger('root.PreviewPage')

        # WIDGETS
        self._logger.info("Initialize widgets")
        self._text = tk.Text(master, height=5, width=100, font=DEF_FONT)
        self._text.insert(tk.END, str(json_object))

        # LAYOUT
        self._logger.info("Initialize GUI layout")
        self._text.pack(side=tk.LEFT, fill=tk.Y)

    def confirm_close(self):
        """Event handler for Exiting the GUI"""

        global preview_open

        self.master.destroy()
        preview_open = False


if __name__ == "__main__":
    root = tk.Tk()
    path = expanduser('~')
    gui = IntroPage(root, path)
    root.mainloop()
