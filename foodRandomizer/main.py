import tkinter as tk
import os
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
from random import *


#API key for Yelp Fusion API
#api_key = "z947pXoeRdPjiu-erKgwOIZNgVKGdDsCeF8jRdKjo5TBxGtPldWvsP9YqgB-y4MRS0DMRt4OkN4y68sgBM8s4u4plRbWlaIk4FLWJcTwcbv6h5LmEtIqcJmM4kIXZXYx"


class Page(tk.Frame):
    
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.configure(bg='#293241')  # Set the background color of the frame

    def show(self):
        self.lift()
        
    def doNothing(self):
        pass

    #GOAL: Refresh all pages whenever another page is selected
    def reset(self):

        #retrieve directory path
        dir_path = os.path.dirname(os.path.realpath(__file__))

        #initialize image of restaurant logo
        self.imagePath = Image.open(dir_path + "/images/question-mark.gif")
        
        #initializes random image
        self.randomImage = ImageTk.PhotoImage(self.imagePath)

        #create image labels to place the images onto the window
        self.imageLabel = tk.Label(self, image = self.randomImage, borderwidth=4, relief="solid")

        # Position images with padding
        self.imageLabel.pack(side="bottom", expand="true", padx=10, pady=10)


class CasualDining(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        self.someNumber = 0

        #retrieve directory path
        dir_path = os.path.dirname(os.path.realpath(__file__))

        # Define a dictionary to map restaurant numbers to image paths
        restaurant_images = {
            1: "/images/restaurants/applebees.jpg",
            2: "/images/restaurants/c-dropout.jpg",
            3: "/images/restaurants/chillis.jpg",
            4: "/images/restaurants/oreganos.jpg",
            5: "/images/restaurants/pita-jungle.jpg",
            6: "/images/restaurants/postinos.jpg",
            7: "/images/restaurants/t-roadhouse.jpg",
            8: "/images/restaurants/fourpeaks.jpg",
            9: "/images/restaurants/fuzzys.png",
            10: "/images/restaurants/chuckbox.jpg",
            11: "/images/restaurants/ipetes.png",
            12: "/images/restaurants/theporch.jpg",
            13: "/images/restaurants/sauce.jpg",
            14: "/images/restaurants/cheesecake.png",
            15: "/images/restaurants/thelodge.jpg",
            15: "/images/restaurants/keg.png",
            16: "/images/restaurants/rrobin.jpg",
            17: "/images/restaurants/bdubs.png",
            18: "/images/restaurants/ogarden.jpg",
            19: "/images/restaurants/bjs.jpg",
        }

        def randomizeNum():
            
            #self.after(5)
            temp = randint(1,19)
            self.someNumber = temp

            # Get the image path from the dictionary
            image_path = dir_path + restaurant_images.get(self.someNumber, "/images/question-mark.gif")

            # Initialize image of restaurant logo
            image = Image.open(image_path)
            self.randomImage = ImageTk.PhotoImage(image)
            self.imageLabel.config(image=self.randomImage)

        #add label to top of the window as program title
        self.programTitle = tk.Label(self, text = "Casual Dining", font = ('Chalkboard', 60), bg='#293241', fg='#e0fbfc')
        self.programTitle.pack(padx = 5, pady = 20)

        #initialize a button frame
        buttonframe = tk.Frame(self, bg='#293241')

        #stretch the button to fill the x-axis
        buttonframe.columnconfigure(0, weight = 1)

        #initialize randomize button
        button = tk.Button(buttonframe, text = "Randomize", font = ('Chalkboard', 30), height = 2, width = 30, command = randomizeNum, bg='#3d5a80', fg='#98c1d9', activebackground='#ee6c4d', activeforeground='#000000')

        #add button the grid
        button.grid(padx = 30,pady = 12, row = 0, column = 0, sticky = tk.W + tk.E)
        
        #stretch into the x-axis
        buttonframe.pack(fill = 'x')
   
        #initialize image of restaurant logo
        image_path = dir_path + restaurant_images.get(self.someNumber, "/images/question-mark.gif")
        self.randomImage = ImageTk.PhotoImage(Image.open(image_path))

        #create image labels to place the images onto the window
        self.imageLabel = tk.Label(self, image = self.randomImage, bg="#293241")

        #position images
        self.imageLabel.pack(side = "bottom", expand = "true", padx=10, pady=10)
        

class FastFood(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        self.someNumber = 0

        #retrieve directory path
        dir_path = os.path.dirname(os.path.realpath(__file__))

        # Define a dictionary to map restaurant numbers to image paths
        fastfood_images = {
            1: "/images/fast_food/mcdonalds.jpg",
            2: "/images/fast_food/in-n-out.jpg",
            3: "/images/fast_food/canes.jpg",
            4: "/images/fast_food/c-fil-a.jpg",
            5: "/images/fast_food/culvers.jpg",
            6: "/images/fast_food/j-in-b.jpg",
            7: "/images/fast_food/sonic.jpg",
            8: "/images/fast_food/wendys.jpg",
            9: "/images/fast_food/burger-king.jpg",
            10: "/images/fast_food/chipotle.jpg",
            11: "/images/fast_food/dominos.jpg",
            12: "/images/fast_food/five-guys.jpg",
            13: "/images/fast_food/ikes.jpg",
            14: "/images/fast_food/panda.jpg",
            15: "/images/fast_food/pei-wei.jpg",
            16: "/images/fast_food/popeyes.jpg",
            17: "/images/fast_food/portillos.jpg",
            18: "/images/fast_food/subway.jpg",
            19: "/images/fast_food/whataburger.jpg",
            20: "/images/fast_food/wingstop.jpg",
            21: "/images/fast_food/tacobell.jpg"
        }
        
        def randomizeNum():
            temp = randint(1,21)
            self.someNumber = temp

            # Get the image path from the dictionary
            image_path = dir_path + fastfood_images.get(self.someNumber, "/images/question-mark.gif")

            # Initialize image of restaurant logo
            image = Image.open(image_path)
            self.randomImage = ImageTk.PhotoImage(image)
            self.imageLabel.config(image=self.randomImage)

        
        #add label to top of the window as program title
        self.programTitle = tk.Label(self, text = "Fast Food", font = ('Chalkboard', 60), bg='#293241', fg='#e0fbfc')
        self.programTitle.pack(padx = 5, pady = 20)

        #initialize a button frame
        buttonframe = tk.Frame(self, bg='#293241')

        #stretch the button to fill the x-axis
        buttonframe.columnconfigure(0, weight = 1)

        #initialize randomize button
        button = tk.Button(buttonframe, text = "Randomize", font = ('Chalkboard', 30), height = 2, width = 30, command = randomizeNum, bg='#3d5a80', fg='#98c1d9', activebackground='#ee6c4d', activeforeground='#000000')
        
        #add button the grid
        button.grid(padx = 30,pady = 12, row = 0, column = 0, sticky = tk.W + tk.E)
        
        #stretch into the x-axis
        buttonframe.pack(fill = 'x')

        #initialize image of restaurant cookie
        imagePath = Image.open(dir_path + "/images/question-mark.gif")
        self.randomImage = ImageTk.PhotoImage(imagePath)

        #create image labels to place the images onto the window
        self.imageLabel = tk.Label(self, image = self.randomImage, bg="#293241")

        #position images
        self.imageLabel.pack(side = "bottom", expand = "true", padx=10, pady=10)


class BreakfastFood(Page):
    
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        #add label to top of the window as program title
        self.programTitle = tk.Label(self, text = "Breakfast Foods", font = ('Chalkboard', 60), bg='#293241', fg='#e0fbfc')
        self.programTitle.pack(padx = 5, pady = 20)

        self.someNumber = 0

        #retrieve directory path
        dir_path = os.path.dirname(os.path.realpath(__file__))

        # Define a dictionary to map breakfast numbers to image paths
        breakfast_images = {
            1: "/images/breakfast/snooze.jpg",
            2: "/images/breakfast/crepe-club.jpg",
            3: "/images/breakfast/einsteins.jpg",
            4: "/images/breakfast/morning-squeeze.jpg",
            5: "/images/breakfast/sunnys.jpg",
            6: "/images/breakfast/first-watch.jpg",
            7: "/images/breakfast/nektar.jpg",
            8: "/images/breakfast/starbucks.jpg",
            9: "/images/breakfast/dutch.jpg",
            10: "/images/breakfast/jamba.jpg",
            11: "/images/fast_food/mcdonalds.jpg",
            12: "/images/fast_food/c-fil-a.jpg",
            13: "/images/breakfast/ihop.jpg"
        }
        
        def randomizeNum():
            temp = randint(1,13)
            self.someNumber = temp

            # Get the image path from the dictionary
            image_path = dir_path + breakfast_images.get(self.someNumber, "/images/question-mark.gif")

            # Initialize image of restaurant logo
            image = Image.open(image_path)
            self.randomImage = ImageTk.PhotoImage(image)
            self.imageLabel.config(image=self.randomImage)
            
        
        #initialize a button frame
        buttonframe = tk.Frame(self, bg='#293241')

        #stretch the button to fill the x-axis
        buttonframe.columnconfigure(0, weight = 1)

        #initialize randomize button
        button = tk.Button(buttonframe, text = "Randomize", font = ('Chalkboard', 30), height = 2, width = 30, command = randomizeNum, bg='#3d5a80', fg='#98c1d9', activebackground='#ee6c4d', activeforeground='#000000')
        
        #add button the grid
        button.grid(padx = 30,pady = 12, row = 0, column = 0, sticky = tk.W + tk.E)
        
        #stretch into the x-axis
        buttonframe.pack(fill = 'x')

        #initialize image of restaurant cookie
        imagePath = Image.open(dir_path + "/images/question-mark.gif")
        self.randomImage = ImageTk.PhotoImage(imagePath)

        #create image labels to place the images onto the window
        self.imageLabel = tk.Label(self, image = self.randomImage, bg="#293241")

        #position images
        self.imageLabel.pack(side = "bottom", expand = "true", padx=10, pady=10)


class TitlePage(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        #add label to top of the window as program title
        self.programTitle = tk.Label(self, text = "Welcome", font = ('Chalkboard', 90), bg='#293241', fg='#e0fbfc')
        self.programTitle.pack(padx = 5, pady = 80)

        #add label to below program title for description
        self.programTitle = tk.Label(self, text = "Please select an option", font = ('Chalkboard', 30), bg='#293241', fg='#e0fbfc')
        self.programTitle.pack(padx = 5, pady = 20)

class MainView(tk.Frame):

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        
        #initialize objects
        p1 = TitlePage(self)
        p2 = CasualDining(self)
        p3 = FastFood(self)
        p4 = BreakfastFood(self)

        #create frame for the buttons
        buttonframe = tk.Frame(self, bg='#293241')

        #create container for switching between the 4 modes
        container = tk.Frame(self, bg='#293241')
        
        # stretch the 4 buttons to fill the x-axis
        buttonframe.columnconfigure(0, weight = 1)
        buttonframe.columnconfigure(1, weight = 1)
        buttonframe.columnconfigure(2, weight = 1)
        buttonframe.columnconfigure(3, weight = 1)

        #place the container onto the window
        container.pack(side='top', fill='both', expand = True)

        #place all objects on the container on one another
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        #initialize all restaurants button to the frame
        firstButton = tk.Button(buttonframe, text = "Main Menu", font = ('Chalkboard', 14), height = 2, width = 30, command = p1.show, bg='#3d5a80', fg='#98c1d9', activebackground='#ee6c4d', activeforeground='#000000')
        firstButton.grid(pady = 12, row = 0, column = 0, sticky = tk.W + tk.E)

        #initialize fast food button to the frame
        secondButton = tk.Button(buttonframe, text = "Casual Dining", font = ('Chalkboard', 14), height = 2, width = 30, command = p2.show, bg='#3d5a80', fg='#98c1d9', activebackground='#ee6c4d', activeforeground='#000000')
        secondButton.grid(pady = 12, row = 0, column = 1, sticky = tk.W + tk.E)

        #initialize genre selector button to the frame
        thirdButton = tk.Button(buttonframe, text = "Fast Food", font = ('Chalkboard', 14), height = 2, width = 30, command = p3.show, bg='#3d5a80', fg='#98c1d9', activebackground='#ee6c4d', activeforeground='#000000')
        thirdButton.grid(pady = 12, row = 0, column = 2, sticky = tk.W + tk.E)

        #initialize breakfast button to the frame
        fourthButton = tk.Button(buttonframe, text = "Breakfast", font = ('Chalkboard', 14), height = 2, width = 30, command = p4.show, bg='#3d5a80', fg='#98c1d9', activebackground='#ee6c4d', activeforeground='#000000')
        fourthButton.grid(pady = 12, row = 0, column = 3, sticky = tk.W + tk.E)

        #stretch into the y-axis
        buttonframe.pack(fill = 'y')
        
        #start program by showing title page
        p1.show()

        def reset_all(self):
            p1.reset


if __name__ == '__main__':
    root = tk.Tk()
    main = MainView(root)
    main.pack(side='top', fill='both', expand=True)
    root.wm_geometry('600x650')
    root.mainloop()
