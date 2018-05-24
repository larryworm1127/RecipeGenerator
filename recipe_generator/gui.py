import tkinter as tk


class GUI:

    def __init__(self, master):
        self._master = master
        master.title("Minecraft Recipe Generator")

        self._output_label = tk.Label(master, text="Output")
        self._output_count_label = tk.Label(master, text="Count")
        self._pattern_label = tk.Label(master, text="Pattern")
        self._item_input_label = tk.Label(master, text="Item Input")

        self._output_entry = tk.Entry(master)
        self._pattern_one_entry = tk.Entry(master)
        self._pattern_two_entry = tk.Entry(master)
        self._pattern_three_entry = tk.Entry(master)


if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
