import tkinter as tk
from tkinter import messagebox

class MyGUI:

    def __init__(self):

        #initialize tk object
        self.root = tk.Tk()

        #sets window title
        self.root.title("foodRandomizer.exe")

        #initializes parent menu bar
        self.menubar = tk.Menu(self.root)

        #initializes menu bar
        self.filemenu = tk.Menu(self.menubar, tearoff = 0)

        #adds a command to close the program onto the file menu
        self.filemenu.add_command(label = "Exit", command = self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label = "Force Quit", command = exit)

        #add another menu to the parent menu
        self.actionmenu = tk.Menu(self.menubar, tearoff = 0)
        self.actionmenu.add_command(label = "Show Message", command = self.show_message)

        #adds the filemenu to the menubar
        self.menubar.add_cascade(menu = self.filemenu, label = "File")
        self.menubar.add_cascade(menu = self.actionmenu, label = "Actions")

        
        self.root.config(menu = self.menubar)

        self.programTitle = tk.Label(self.root, text = "FOOD RANDOMIZER", font = ('Chalkboard', 25))
        self.programTitle.pack(padx = 10, pady = 40)

        self.label = tk.Label(self.root, text = "Your Message", font = ('Arial', 18))
        self.label.pack(padx = 10, pady = 10)

        self.textbox = tk.Text(self.root, height = 5, font = ('Arial', 16))

        #bind a keypress to an action
        self.textbox.bind("<KeyPress>", self.shortcut)

        self.textbox.pack(padx = 10, pady = 10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text = "Show Messagebox", font = ('Arial', 16), variable = self.check_state)
        self.check.pack(padx = 10, pady = 10)

        self.button = tk.Button(self.root, text = "Show Message", font = ('Arial', 18), command = self.show_message)
        self.button.pack(padx = 10, pady = 10)

        self.clearbutton = tk.Button(self.root, text = "Clear", font = ('Arial', 18), command = self.clear)
        self.clearbutton.pack(padx = 10, pady = 10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    def show_message(self):
            #check if the checkbox is not clicked
            if self.check_state.get() == 0:
                #print the textbox contents to the console
                print(self.textbox.get('1.0', tk.END))
            else:
                #show the entered message as a pop-up window
                messagebox.showinfo(title = "Message", message = self.textbox.get('1.0', tk.END))

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

    def clear(self):
        self.textbox.delete('1.0', tk.END)

MyGUI()