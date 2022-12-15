import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
from random import *


class Page(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()

    def doNothing(self):
        pass

    def on_closing(self):
        if messagebox.askyesno(title = "Quit?", message = "Do you really want to quit?"):
            #actually closes the window
            self.destroy()

class Randomizer():

    def randomNum(self, lower, upper):
        num = randint(lower, upper)
        return num


class AllRestaurants(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        #add label to top of the window as program title
        self.programTitle = tk.Label(self, text = "All Restuarants", font = ('Chalkboard', 60))
        self.programTitle.pack(padx = 5, pady = 20)
        
        r = Randomizer()

        num = r.randomNum(0, 10)

        #initialize a button frame
        buttonframe = tk.Frame(self)

        #stretch the button to fill the x-axis
        buttonframe.columnconfigure(0, weight = 1)

        #initialize randomize button
        button = tk.Button(buttonframe, text = "Randomize", font = ('Chalkboard', 30), height = 2, width = 30)
        
        #add button the grid
        button.grid(padx = 30,pady = 12, row = 0, column = 0, sticky = tk.W + tk.E)
        
        #stretch into the x-axis
        buttonframe.pack(fill = 'x')

        #initialize image of dancing cookie
        #imagePath = Image.open("/Users/james/VSCode/Python/freeSpace/mcdonalds.jpeg")
        #randomImage = ImageTk.PhotoImage(imagePath)

        #create image labels to place the images onto the window
        #imageLabel = tk.Label(image = randomImage)

        #position images
        #imageLabel.place(x = 200, y = 250)  
        #imageLabel.pack(padx = 10, fill = 'x')



class FastFood(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        #add label to top of the window as program title
        self.programTitle = tk.Label(self, text = "Fast Food", font = ('Chalkboard', 60))
        self.programTitle.pack(padx = 5, pady = 20)

        #initialize a button frame
        buttonframe = tk.Frame(self)

        #stretch the button to fill the x-axis
        buttonframe.columnconfigure(0, weight = 1)

        #initialize randomize button
        button = tk.Button(buttonframe, text = "Randomize", font = ('Chalkboard', 30), height = 2, width = 30)
        
        #add button the grid
        button.grid(padx = 30,pady = 12, row = 0, column = 0, sticky = tk.W + tk.E)
        
        #stretch into the x-axis
        buttonframe.pack(fill = 'x')


class GenreSelector(Page):
    
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        #add label to top of the window as program title
        self.programTitle = tk.Label(self, text = "Genre Selector", font = ('Chalkboard', 60))
        self.programTitle.pack(padx = 5, pady = 20)

        #initialize a button frame
        buttonframe = tk.Frame(self)

        #stretch the button to fill the x-axis
        buttonframe.columnconfigure(0, weight = 1)

        #initialize randomize button
        button = tk.Button(buttonframe, text = "Randomize", font = ('Chalkboard', 30), height = 2, width = 30)
        
        #add button the grid
        button.grid(padx = 30,pady = 12, row = 0, column = 0, sticky = tk.W + tk.E)
        
        #stretch into the x-axis
        buttonframe.pack(fill = 'x')


class BattleRoyale(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        #add label to top of the window as program title
        self.programTitle = tk.Label(self, text = "Battle Royale", font = ('Chalkboard', 60))
        self.programTitle.pack(padx = 5, pady = 20)

        #initialize a button frame
        buttonframe = tk.Frame(self)

        #stretch the 4 buttons to fill the y-axis
        buttonframe.columnconfigure(0, weight = 1)
        buttonframe.columnconfigure(1, weight = 1)

        #initialize option selection buttons
        leftButton = tk.Button(buttonframe, text = "Option 1", font = ('Chalkboard', 22), height = 2, width = 30)
        rightButton = tk.Button(buttonframe, text = "Option 2", font = ('Chalkboard', 22), height = 2, width = 30)

        leftButton.grid(pady = 12, row = 0, column = 0, sticky = tk.W + tk.E)
        rightButton.grid(pady = 12, row = 0, column = 1, sticky = tk.W + tk.E)

        #stretch into the y-axis
        buttonframe.pack(padx = 20, fill = 'x')

class TitlePage(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        #add label to top of the window as program title
        self.programTitle = tk.Label(self, text = "Welcome", font = ('Chalkboard', 60))
        self.programTitle.pack(padx = 5, pady = 60)

        #add label to below program title for description
        self.programTitle = tk.Label(self, text = "<     Please select one of the following options     >", font = ('Chalkboard', 24))
        self.programTitle.pack(padx = 5, pady = 90)

class MainView(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        
        #initialize objects
        p1 = TitlePage(self)
        p2 = AllRestaurants(self)
        p3 = FastFood(self)
        p4 = GenreSelector(self)
        p5 = BattleRoyale(self)

        #create frame for the buttons
        buttonframe = tk.Frame(self)

        #create container for switching between the 4 modes
        container = tk.Frame(self)
        
        # stretch the 4 buttons to fill the x-axis
        buttonframe.columnconfigure(0, weight = 1)
        buttonframe.columnconfigure(1, weight = 1)
        buttonframe.columnconfigure(2, weight = 1)
        buttonframe.columnconfigure(3, weight = 1)
        buttonframe.columnconfigure(4, weight = 1)

        #place the container onto the window
        container.pack(side='top', fill='both', expand = True)

        #place all objects on the container on one another
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        #initialize all restaurants button to the frame
        firstButton = tk.Button(buttonframe, text = "Main Menu", font = ('Chalkboard', 14), height = 2, width = 30, command = p1.show)
        firstButton.grid(pady = 12, row = 0, column = 0, sticky = tk.W + tk.E)

        #initialize fast food button to the frame
        secondButton = tk.Button(buttonframe, text = "All Restaurants", font = ('Chalkboard', 14), height = 2, width = 30, command = p2.show)
        secondButton.grid(pady = 12, row = 0, column = 1, sticky = tk.W + tk.E)

        #initialize genre selector button to the frame
        thirdButton = tk.Button(buttonframe, text = "Fast Food", font = ('Chalkboard', 14), height = 2, width = 30, command = p3.show)
        thirdButton.grid(pady = 12, row = 0, column = 2, sticky = tk.W + tk.E)

        #initialize battle royale button to the frame
        fourthButton = tk.Button(buttonframe, text = "Genre Selector", font = ('Chalkboard', 14), height = 2, width = 30, command = p4.show)
        fourthButton.grid(pady = 12, row = 0, column = 3, sticky = tk.W + tk.E)

        #initialize battle royale button to the frame
        fifthButton = tk.Button(buttonframe, text = "Battle Royale", font = ('Chalkboard', 14), height = 2, width = 30, command = p5.show)
        fifthButton.grid(pady = 12, row = 0, column = 4, sticky = tk.W + tk.E)

        #stretch into the y-axis
        buttonframe.pack(fill = 'y')

        #start program by showing title page
        p1.show()


if __name__ == '__main__':
    root = tk.Tk()
    main = MainView(root)
    main.pack(side='top', fill='both', expand=True)
    root.wm_geometry('600x650')
    root.mainloop()
