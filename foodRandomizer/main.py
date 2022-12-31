import tkinter as tk
import os
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

    def refresh(self):
        self.refresh
        #self.__init__()
        

class Randomizer():

    def randomNum(self, lower, upper):
        num = randint(lower, upper)
        return num


class AllRestaurants(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        self.someNumber = 0

        #retrieve directory path
        dir_path = os.path.dirname(os.path.realpath(__file__))
        
        def randomizeNum():
            
            #self.after(5)
            temp = randint(1,7)
            self.someNumber = temp

            #randomizes image placed onto frame when randomize is clicked
            if(self.someNumber == 1):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/restaurants/applebees.jpg")

            elif(self.someNumber == 2):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/restaurants/c-dropout.jpg")

            elif(self.someNumber == 3):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/restaurants/chillis.jpg")

            elif(self.someNumber == 4):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/restaurants/oreganos.jpg")

            elif(self.someNumber == 5):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/restaurants/pita-jungle.jpg")

            elif(self.someNumber == 6):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/restaurants/postinos.jpg")
            
            else:
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/restaurants/t-roadhouse.jpg")

            #initializes random image
            self.randomImage = ImageTk.PhotoImage(imagePath)

            self.imageLabel.config(image = self.randomImage)

        #add label to top of the window as program title
        self.programTitle = tk.Label(self, text = "All Restuarants", font = ('Chalkboard', 60))
        self.programTitle.pack(padx = 5, pady = 20)
        
        #RANDOM NUMBER GENERATION TESTING
        #r = Randomizer()
        #num = r.randomNum(0, 10)

        #initialize a button frame
        buttonframe = tk.Frame(self)

        #stretch the button to fill the x-axis
        buttonframe.columnconfigure(0, weight = 1)

        #initialize randomize button
        button = tk.Button(buttonframe, text = "Randomize", font = ('Chalkboard', 30), height = 2, width = 30, command = randomizeNum)

        #add button the grid
        button.grid(padx = 30,pady = 12, row = 0, column = 0, sticky = tk.W + tk.E)
        
        #stretch into the x-axis
        buttonframe.pack(fill = 'x')
   
        #initialize image of restaurant logo
        imagePath = Image.open(dir_path + "/images/question-mark.gif")
        
        #initializes random image
        self.randomImage = ImageTk.PhotoImage(imagePath)

        #create image labels to place the images onto the window
        self.imageLabel = tk.Label(self, image = self.randomImage)

        #position images
        self.imageLabel.place(y = 250, x = 140)
        

class FastFood(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        self.someNumber = 0

        #retrieve directory path
        dir_path = os.path.dirname(os.path.realpath(__file__))
        
        def randomizeNum():
            temp = randint(1,20)
            self.someNumber = temp

            #randomizes image placed onto frame when randomize is clicked
            if(self.someNumber == 1):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/fast_food/mcdonalds.jpg")

            elif(self.someNumber == 2):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/fast_food/in-n-out.jpg")

            elif(self.someNumber == 3):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/fast_food/canes.jpg")

            elif(self.someNumber == 4):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/fast_food/c-fil-a.jpg")

            elif(self.someNumber == 5):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/fast_food/culvers.jpg")

            elif(self.someNumber == 6):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/fast_food/j-in-b.jpg")

            elif(self.someNumber == 7):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/fast_food/sonic.jpg")
            
            elif(self.someNumber == 8):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/fast_food/wendys.jpg")
            
            elif(self.someNumber == 9):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/fast_food/burger-king.jpg")
            
            elif(self.someNumber == 10):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/fast_food/chipotle.jpg")
            
            elif(self.someNumber == 11):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/fast_food/dominos.jpg")
            
            elif(self.someNumber == 12):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/fast_food/five-guys.jpg")
            
            elif(self.someNumber == 13):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/fast_food/ikes.jpg")

            elif(self.someNumber == 14):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/fast_food/panda.jpg")
            
            elif(self.someNumber == 8):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/fast_food/pei-wei.jpg")
            
            elif(self.someNumber == 15):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/fast_food/popeyes.jpg")

            elif(self.someNumber == 16):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/fast_food/portillos.jpg")
            
            elif(self.someNumber == 17):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/fast_food/subway.jpg")

            elif(self.someNumber == 18):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/fast_food/whataburger.jpg")

            elif(self.someNumber == 19):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/fast_food/wingstop.jpg")

            else:
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/fast_food/tacobell.jpg")


            #initializes random image
            self.randomImage = ImageTk.PhotoImage(imagePath)

            self.imageLabel.config(image = self.randomImage)

        
        #add label to top of the window as program title
        self.programTitle = tk.Label(self, text = "Fast Food", font = ('Chalkboard', 60))
        self.programTitle.pack(padx = 5, pady = 20)

        #initialize a button frame
        buttonframe = tk.Frame(self)

        #stretch the button to fill the x-axis
        buttonframe.columnconfigure(0, weight = 1)

        #initialize randomize button
        button = tk.Button(buttonframe, text = "Randomize", font = ('Chalkboard', 30), height = 2, width = 30, command = randomizeNum)
        
        #add button the grid
        button.grid(padx = 30,pady = 12, row = 0, column = 0, sticky = tk.W + tk.E)
        
        #stretch into the x-axis
        buttonframe.pack(fill = 'x')

        #initialize image of restaurant cookie
        imagePath = Image.open(dir_path + "/images/question-mark.gif")
        self.randomImage = ImageTk.PhotoImage(imagePath)

        #create image labels to place the images onto the window
        self.imageLabel = tk.Label(self, image = self.randomImage)

        #position images
        self.imageLabel.place(y = 250, x = 140)


class BreakfastFood(Page):
    
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        #add label to top of the window as program title
        self.programTitle = tk.Label(self, text = "Breakfast Foods", font = ('Chalkboard', 60))
        self.programTitle.pack(padx = 5, pady = 20)

        self.someNumber = 0

        #retrieve directory path
        dir_path = os.path.dirname(os.path.realpath(__file__))
        
        def randomizeNum():
            temp = randint(1,13)
            self.someNumber = temp

            #randomizes image placed onto frame when randomize is clicked
            if(self.someNumber == 1):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/breakfast/snooze.jpg")

            elif(self.someNumber == 2):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/breakfast/crepe-club.jpg")

            elif(self.someNumber == 3):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/breakfast/einsteins.jpg")

            elif(self.someNumber == 4):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/breakfast/morning-squeeze.jpg")

            elif(self.someNumber == 5):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/breakfast/sunnys.jpg")

            elif(self.someNumber == 6):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/breakfast/first-watch.jpg")

            elif(self.someNumber == 7):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/breakfast/nektar.jpg")

            elif(self.someNumber == 8):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/breakfast/starbucks.jpg")   

            elif(self.someNumber == 9):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/breakfast/dutch.jpg")

            elif(self.someNumber == 10):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/breakfast/jamba.jpg")

            elif(self.someNumber == 11):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/fast_food/mcdonalds.jpg")

            elif(self.someNumber == 12):
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/fast_food/c-fil-a.jpg") 
            
            else:
                #initialize image of restaurant logo
                imagePath = Image.open(dir_path + "/images/breakfast/ihop.jpg")


            #initializes random image
            self.randomImage = ImageTk.PhotoImage(imagePath)

            self.imageLabel.config(image = self.randomImage)
            
        
        #initialize a button frame
        buttonframe = tk.Frame(self)

        #stretch the button to fill the x-axis
        buttonframe.columnconfigure(0, weight = 1)

        #initialize randomize button
        button = tk.Button(buttonframe, text = "Randomize", font = ('Chalkboard', 30), height = 2, width = 30, command = randomizeNum)
        
        #add button the grid
        button.grid(padx = 30,pady = 12, row = 0, column = 0, sticky = tk.W + tk.E)
        
        #stretch into the x-axis
        buttonframe.pack(fill = 'x')

        #initialize image of restaurant cookie
        imagePath = Image.open(dir_path + "/images/question-mark.gif")
        self.randomImage = ImageTk.PhotoImage(imagePath)

        #create image labels to place the images onto the window
        self.imageLabel = tk.Label(self, image = self.randomImage)

        #position images
        self.imageLabel.place(y = 250, x = 140)


class BattleRoyale(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        #retrieve directory path
        dir_path = os.path.dirname(os.path.realpath(__file__))
        
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

        #initialize image of restaurant cookie
        imagePath = Image.open(dir_path + "/images/question-mark.gif")
        self.randomImage1 = ImageTk.PhotoImage(imagePath)
        self.randomImage2 = ImageTk.PhotoImage(imagePath)

        #create image labels to place the images onto the window
        self.imageLabel1 = tk.Label(self, image = self.randomImage1)
        #create image labels to place the images onto the window
        self.imageLabel2 = tk.Label(self, image = self.randomImage2)

        #position images
        self.imageLabel1.place(y = 250, x = 5)
        self.imageLabel2.place(y = 250, x = 290)

class TitlePage(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        #add label to top of the window as program title
        self.programTitle = tk.Label(self, text = "Welcome\n---------------------------", font = ('Chalkboard', 80))
        self.programTitle.pack(padx = 5, pady = 30)

        #add label to below program title for description
        self.programTitle = tk.Label(self, text = "<     Please select one of the following options     >", font = ('Chalkboard', 24))
        self.programTitle.pack(padx = 5, pady = 40)

        #initialize a button frame
        buttonframe = tk.Frame(self)

        #stretch the button to fill the x-axis
        buttonframe.columnconfigure(0, weight = 1)

        #initialize randomize button
        button = tk.Button(buttonframe, text = "Reset Program", font = ('Chalkboard', 14), height = 2, width = 30, command = self.refresh)
        
        #add button the grid
        button.grid(padx = 30,pady = 16, row = 0, column = 0, sticky = tk.W + tk.E)
        
        #stretch into the x-axis
        buttonframe.pack(fill = 'x')

class MainView(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        
        #initialize objects
        p1 = TitlePage(self)
        p2 = AllRestaurants(self)
        p3 = FastFood(self)
        p4 = BreakfastFood(self)
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
        fourthButton = tk.Button(buttonframe, text = "Breakfast", font = ('Chalkboard', 14), height = 2, width = 30, command = p4.show)
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
