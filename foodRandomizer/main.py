import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
import time
import os

class MyGUI:

    def __init__(self):

        #initialize tk object
        self.root = tk.Tk()

        #sets the bounds of the window (x, y)
        self.root.geometry("600x550")

        #sets window title
        self.root.title("Food Randomizer")

        #initializes parent menu bar
        self.menubar = tk.Menu(self.root)

        #initializes file menu on parent menu bar
        self.filemenu = tk.Menu(self.menubar, tearoff = 0)

        #adds a file options to the menu
        self.filemenu.add_command(label = "Refresh", command = self.doNothing)
        self.filemenu.add_command(label = "Share", command = self.doNothing)
        #add separator bar to sub-menu
        self.filemenu.add_separator()
        self.filemenu.add_command(label = "Exit", command = self.on_closing)
        self.filemenu.add_command(label = "Force Quit", command = exit)

        #add mode menu to the parent menu bar
        #mode menu to select between different food randomizer modes
        self.modeMenu = tk.Menu(self.menubar, tearoff = 0)
        self.modeMenu.add_command(label = "All Restaurants", command = self.doNothing)
        self.modeMenu.add_command(label = "Fast Food", command = self.doNothing)
        self.modeMenu.add_command(label = "Genre Selector", command = self.doNothing)
        self.modeMenu.add_command(label = "Battle Royale", command = self.doNothing)

        #adds the filemenu to the menubar
        self.menubar.add_cascade(menu = self.filemenu, label = "File")
        self.menubar.add_cascade(menu = self.modeMenu, label = "Mode")

        #add parent menu to the window
        self.root.config(menu = self.menubar)

        #add label to top of the window as program title
        self.programTitle = tk.Label(self.root, text = "Welcome", font = ('Chalkboard', 40))
        self.programTitle.pack(padx = 5)

        #add label to below program title for description
        self.programTitle = tk.Label(self.root, text = "<     Please select one of the following options     >", font = ('Chalkboard', 18))
        self.programTitle.pack(padx = 5, pady = 16)

        #   ****  ADDS TEXTBOX  ****
        #self.label = tk.Label(self.root, text = "Your Message", font = ('Arial', 18))
        #self.label.pack(padx = 10, pady = 10)
        #self.textbox = tk.Text(self.root, height = 5, font = ('Arial', 16))
        #bind a keypress to an action
        #self.textbox.bind("<KeyPress>", self.shortcut)
        #self.textbox.pack(padx = 10, pady = 10)
        #self.check_state = tk.IntVar()
        #self.check = tk.Checkbutton(self.root, text = "Show Messagebox", font = ('Arial', 16), variable = self.check_state)
        #self.check.pack(padx = 10, pady = 10)
        #self.button = tk.Button(self.root, text = "Show Message", font = ('Arial', 18), command = self.show_message)
        #self.button.pack(padx = 10, pady = 10)
        #self.clearbutton = tk.Button(self.root, text = "Clear", font = ('Arial', 18), command = self.clear)
        #self.clearbutton.pack(padx = 10, pady = 10)

        #initialize a button frame
        buttonframe = tk.Frame(self.root)

        #stretch the 2 buttons to fill the y-axis
        buttonframe.columnconfigure(0, weight = 1)
        buttonframe.columnconfigure(1, weight = 1)
        buttonframe.columnconfigure(2, weight = 1)
        buttonframe.columnconfigure(3, weight = 1)

        #initialize all restaurants button to the frame
        firstButton = tk.Button(buttonframe, text = "All Restaurants", font = ('Chalkboard', 22), height = 2, width = 30)
        firstButton.grid(pady = 12, row = 0, column = 0, sticky = tk.W + tk.E)

        #initialize fast food button to the frame
        secondButton = tk.Button(buttonframe, text = "Fast Food", font = ('Chalkboard', 22), height = 2, width = 30)
        secondButton.grid(pady = 12, row = 1, column = 0, sticky = tk.W + tk.E)

        #initialize genre selector button to the frame
        thirdButton = tk.Button(buttonframe, text = "Genre Selector", font = ('Chalkboard', 22), height = 2, width = 30)
        thirdButton.grid(pady = 12, row = 2, column = 0, sticky = tk.W + tk.E)

        #initialize battle royale button to the frame
        fourthButton = tk.Button(buttonframe, text = "Battle Royale", font = ('Chalkboard', 22), height = 2, width = 30)
        fourthButton.grid(pady = 12, row = 3, column = 0, sticky = tk.W + tk.E)

        #stretch into the y-axis
        buttonframe.pack(fill = 'y')

        #   ADDS IMAGES TO THE WINDOW
        #initialize image of dancing cookie
        #cookiePath = Image.open("/Users/james/VSCode/Python/foodRandomizer/question-mark.gif")
        #leftImage = ImageTk.PhotoImage(cookiePath, format = "gif -index 20")
        #initialize image of dancing taco
        #tacoPath = Image.open("/Users/james/VSCode/Python/foodRandomizer/question-mark.gif")
        #rightImage = ImageTk.PhotoImage(tacoPath)
        #create image labels to place the images onto the window
        #imageLabel_one = tk.Label(image = leftImage)
        #imageLabel_two = tk.Label(image = rightImage)
        #position images
        #imageLabel_one.place(x = 0, y = 190)
        #imageLabel_two.place(x = 210, y = 190)
        #imageLabel_one.pack(padx = 10, side = "right", fill = 'x')
        #imageLabel_two.pack(side = "left")

        #set default closing protocol
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    def shortcut(self, event):
        #print("--------")        
        #print(event.keysym)
        #print("--------")     
        #print(event.state)
        #print("--------")     
        
        if event.state == 0 and event.keysym == "apostrophe":
            self.show_message()

    
    def on_closing(self):
        if messagebox.askyesno(title = "Quit?", message = "Do you really want to quit?"):
            #actually closes the window
            self.root.destroy()

    def doNothing(self):
        pass


MyGUI()