from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

# Globals
supportedFileTypes = (("PNG Image", ".png"),
                      ("JPEG Image",".jpeg"),
                      ("BMP Image", ".bmp"))

class MainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        
        #class vars
        self.master = master                #master window
        
        self.doc = Document()               #object containing user document
        self.panels = Panels()              #object containing panels
        self.init_window()                  #draw window
    
    #initializes master window and menu
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
    
    #initializes necessary document parameters as well as cleaning up old documents 
    def init_image(self):
        self.panels.docPanel.destroy()                                              #remove prior instances
        self.doc.path = filedialog.askopenfilename(initialdir = "Desktop",          #get path of doc
                                                  title = "Select an image...",     
                                                  filetypes = supportedFileTypes)
        self.doc.raw = Image.open(self.doc.path)                                    #set raw image
        unmodImg = ImageTk.PhotoImage(self.doc.raw)                                 #make PhotoImage to get w and h
        self.doc.aspectRatio = unmodImg.width() / unmodImg.height()                 #calculate aspect ratio
        self.draw_image()                                                           #draw the image

    #draws initial document and sets bind for automatic resizing
    def draw_image(self):
        if not self.doc.raw == None:
            self.doc.set_doc_size()
            docScaled = self.doc.raw.resize((self.doc.previewWidth, self.doc.previewHeight),
                                             Image.ANTIALIAS)               #create properly sized doc
            self.doc.tk = ImageTk.PhotoImage(docScaled)                     #make doc of type PhotoImage
            self.panels.docPanel = Label(self.master)                       #assign doc to master window
            self.panels.docPanel.config(image=self.doc.tk, anchor=CENTER)   #set doc display and center
            self.panels.docPanel.pack(fill=BOTH, expand=YES)                #draw doc on label
            self.panels.docPanel.bind('<Configure>', self.resize_image)     #bind docPanel to resize_image
        else:
            messagebox.showerror("Image to PDF", "No image selected!")
    
    #resizes document to fit in current window with proper aspect ratio
    def resize_image(self, event):
        self.doc.set_doc_size()                                             #set doc size attributes                                            
        docScaled = self.doc.raw.resize((self.doc.previewWidth, self.doc.previewHeight),  #create resized doc
                                Image.ANTIALIAS)
        self.doc.tk = ImageTk.PhotoImage(docScaled)                         #set doc PhotoImage
        self.panels.docPanel.config(image=self.doc.tk)                      #set doc image in panel

    def client_exit(self):
        exit()

class Panels():
    def __init__(self):
        self.docPanel = Label()
    pass

class Document():
    def __init__(self):
        self.path = None            #path to document image
        self.raw = None             #storage of raw document
        self.tk = None              #tk image of document
        self.aspectRatio = None     #aspect ratio of document
        self.previewWidth = None    #current width of document in window
        self.previewHeight = None   #current height of document in window
    
    #initialize document
    def _init_doc(self):
        self.raw = Image.open(self.path)                    #set raw document
        tempTk = ImageTk.PhotoImage(self.raw)               #create PhotoImage for aspect ratio calculation
        self.aspectRatio = tempTk.width() / tempTk.height() #calculate aspect ratio

    #set size parameters
    def set_doc_size(self):
        if not self.aspectRatio == None:
            self.previewWidth = int(root.winfo_height()*self.aspectRatio)
            self.previewHeight = root.winfo_height()
        else:
            print("ERROR: NO ASPECT RATIO SET")

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
main = MainWindow(root)
root.mainloop()