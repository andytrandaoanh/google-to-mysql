import tkinter as tk
import lexicon_gui



win = tk.Tk()

win.title("Google Definitions To MySQL")
win.geometry("760x420") 
win.resizable(0, 0) 


myGUI = lexicon_gui.LexGUI(win)

myGUI.createGUI()


win.mainloop()