#########   PLEASE LOOK AT PREVIOUS COMMIT SUMMARRY   #########

import classes
import tkinter as tk

main = tk.Tk()
main.title("First Tkinter Window")
main.geometry("600x400")

playerCountEntry2 = classes.Entry_Box(main, "lightblue", "black", ("Courier New CYR", 14), ("Courier New CYR", 16), "How many players are there?", "Submit", 0, 1)
playerCountEntry2.make_box()

if classes.playerCount > 0:
    print("hey")

main.mainloop()