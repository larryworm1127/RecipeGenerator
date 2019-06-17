#!/usr/bin/env python

"""Run Script

@date: 06/17/2019
@author: Larry Shi
"""
import tkinter as tk
from os.path import expanduser

from recipes.gui import IntroPage

if __name__ == "__main__":
    root = tk.Tk()
    path = expanduser('~')
    gui = IntroPage(root, path)
    root.mainloop()
