from tkinter import *
from tkinter import filedialog

# Globals
supportedFileTypes = (("JPEG Image",".jpeg"),
                      ("PNG Image", ".png"),
                      ("BMP Image", ".bmp"),
                      ("All Files", "."))

class MainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Image to PDF")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        filetab = Menu(menu)
        filetab.add_command(label="Open...", command=self.open_file)
        filetab.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=filetab)
        

        """self.button1 = Button( self, text = "CLICK HERE", width = 25,
                               command = self.new_window )
        self.button1.grid( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )"""

    def open_file(self):
        filename = filedialog.askopenfilename(initialdir = "/",
                                              title = "Select a File",
                                              filetypes = supportedFileTypes)
        print(filename)

    def client_exit(self):
        exit()
        

root = Tk()
root.geometry("400x300")
app = MainWindow(root)
root.mainloop()