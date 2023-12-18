import tkinter as tk

playerCount = 0
#playerDict =

class Entry_Box:

    def __init__(self, main, bg, fg, font, labelFont, label, buttonText, column, row):
        self.main = main
        self.bg = bg
        self.fg = fg
        self.font = font
        self.labelFont = labelFont
        self.label = label
        self.buttonText = buttonText
        self.column = column
        self.row = row

    def make_box(self):
        self.entryLabel = tk.Label(self.main, font=self.labelFont, text=self.label)
        self.entryLabel.grid(column=self.column, row=self.row, sticky="w")

        self.entry = tk.Entry(self.main, bg=self.bg, fg=self.fg, font=self.font)
        self.entry.grid(column=self.column, row=self.row+1)

        self.button = tk.Button(self.main, bg=self.bg, command=self.return_text, fg=self.fg, text=self.buttonText)
        self.button.grid(column=self.column+1, row=self.row+1)

    def return_text(self):
        global playerCount
        global playerDict

        playerCount = self.entry.get()
        print(playerCount)

        self.entryLabel.grid_remove()
        self.entry.grid_remove()
        self.button.grid_remove()

        for player in playerCount:
            #self.playerEntryLabel = tk.Label(self.main, font=)


            playerDict = {player: num*num for num in range(1, 11)}
