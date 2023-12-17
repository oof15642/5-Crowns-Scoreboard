import tkinter as tk

class Entry_Box:

    def __init__(self, main, bg, font, fg, label, column, row):
        self.main = main
        self.bg = bg
        self.font = font
        self.fg = fg
        self.label = label
        self.column = column
        self.row = row

    def make_box(self):
        self.entry = tk.Entry(self.main, bg="lightblue", fg="black", font=self.font)

        self.entry.grid(column=self.column, row=self.row)