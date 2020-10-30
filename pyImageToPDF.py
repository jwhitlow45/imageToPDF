import tkinter as tk
from tkinter import *
from tkinter import ttk

# Globals


class MainWindow( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Image to PDF")

        self.button1 = Button( self, text = "CLICK HERE", width = 25,
                               command = self.new_window )
        self.button1.grid( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )
    def new_window(self):
        self.newWindow = karl2()

def main(): 
    MainWindow().mainloop()
if __name__ == '__main__':
    main()