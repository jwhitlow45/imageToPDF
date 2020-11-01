from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

# Globals
supportedFileTypes = (("PNG Image", ".png"),
                      ("JPEG Image",".jpeg"),
                      ("BMP Image", ".bmp"),
                      ("All Files", "."))

class MainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        
        #class vars
        self.master = master                    #master window
        self.imgPath = None                     #image path
        self.imgRaw = None                      #image file opened
        self.imgScaled = None                   #displayed image
        self.imgTk = None                       #imagetk photo image
        
        self.init_window()                      #draw window

    def init_window(self):
        self.master.title("Image to PDF")   #application title
        self.pack(fill=BOTH, expand=1)      #smart application sizing
        
        #menubar
        menu = Menu(self.master)            #menubar declaration
        self.master.config(menu=menu)       #menubar initialization
        
        #menubar - file cascade
        fileTab = Menu(menu)
        fileTab.add_command(label="Open...", command=self.init_image)
        fileTab.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=fileTab)
        
        """self.button1 = Button( self, text = "CLICK HERE", width = 25,
                               command = self.new_window )
        self.button1.grid( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )"""

    def init_image(self):
        self.imgPath = filedialog.askopenfilename(initialdir = "Desktop",
                                                  title = "Select an image...",
                                                  filetypes = supportedFileTypes)
        self.imgRaw = Image.open(self.imgPath)
        self.draw_image()


    def draw_image(self):
        if not self.imgRaw == None:
            unmodImg = ImageTk.PhotoImage(self.imgRaw)
            aspectRatio = unmodImg.width() / unmodImg.height()
            self.imgScaled = self.imgRaw.resize((int(self.master.winfo_height()*aspectRatio),   #draw image to window size
                                                 self.master.winfo_height()),             #with proper aspect ratio
                                                Image.ANTIALIAS)
            self.imgTk = ImageTk.PhotoImage(self.imgScaled)
            panel = Label(self.master, image = self.imgTk)
            panel.pack(pady=20)
        else:
            messagebox.showerror("Image to PDF", "No image selected!")

    def client_exit(self):
        exit()

class DragManager():
    def add_dragable(self, widget):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)
        widget.configure(cursor="hand1")

    def on_start(self, event):
        # you could use this method to create a floating window
        # that represents what is being dragged.
        pass

    def on_drag(self, event):
        # you could use this method to move a floating window that
        # represents what you're dragging
        pass

    def on_drop(self, event):
        # find the widget under the cursor
        x,y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x,y)
        try:
            target.configure(image=event.widget.cget("image"))
        except:
            pass
        

root = Tk()
root.geometry("400x300")
app = MainWindow(root)
root.mainloop()