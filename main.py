import classes
import tkinter as tk

main = tk.Tk()
main.title("First Tkinter Window")
main.geometry("600x400")

playerCountEntry = classes.Entry_Box(main, "#00FFFF", "#00FFFF", ("Courier New",14), "#000000", "heyy", 0, 0)
playerCountEntry.make_box()

playerCountEntry2 = classes.Entry_Box(main, "#00FFFF", "#00FFFF", ("Bahnschrift",14), "#000000", "heyy", 0, 1)
playerCountEntry2.make_box()
main.mainloop()