import tkinter as tk
import os
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
from random import *
import webbrowser


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
        self.dir_path = os.path.dirname(os.path.realpath(__file__))

        # Define a dictionary to map restaurant numbers to image paths
        self.restaurant_images = {
            1: {"image": "/images/restaurants/applebees.jpg", "website": "https://www.applebees.com"},
            2: {"image": "/images/restaurants/c-dropout.jpg", "website": "https://www.culinarydropout.com"},
            3: {"image": "/images/restaurants/chillis.jpg", "website": "https://www.chilis.com"},
            4: {"image": "/images/restaurants/oreganos.jpg", "website": "https://www.oreganos.com"},
            5: {"image": "/images/restaurants/pita-jungle.jpg", "website": "https://www.pitajungle.com"},
            6: {"image": "/images/restaurants/postinos.jpg", "website": "https://www.postinowinecafe.com"},
            7: {"image": "/images/restaurants/t-roadhouse.jpg", "website": "https://www.texasroadhouse.com"},
            8: {"image": "/images/restaurants/fourpeaks.jpg", "website": "https://www.fourpeaks.com"},
            9: {"image": "/images/restaurants/fuzzys.png", "website": "https://www.fuzzystacoshop.com"},
            10: {"image": "/images/restaurants/chuckbox.jpg", "website": "https://www.thechuckbox.com"},
            11: {"image": "/images/restaurants/ipetes.png", "website": "https://www.ikessandwich.com/"},
            12: {"image": "/images/restaurants/theporch.jpg", "website": "https://www.porcharcadia.com"},
            13: {"image": "/images/restaurants/sauce.jpg", "website": "https://www.saucepizzaandwine.com"},
            14: {"image": "/images/restaurants/cheesecake.png", "website": "https://www.thecheesecakefactory.com"},
            15: {"image": "/images/restaurants/thelodge.jpg", "website": "https://www.lodgetucson.com"},
            16: {"image": "/images/restaurants/keg.png", "website": "https://www.kegsteakhouse.com"},
            17: {"image": "/images/restaurants/rrobin.jpg", "website": "https://www.redrobin.com"},
            18: {"image": "/images/restaurants/bdubs.png", "website": "https://www.buffalowildwings.com"},
            19: {"image": "/images/restaurants/ogarden.jpg", "website": "https://www.olivegarden.com"},
            20: {"image": "/images/restaurants/bjs.jpg", "website": "https://www.bjsrestaurants.com"},
            21: {"image": "/images/breakfast/panera.png", "website": "https://www.panerabread.com/en-us/home.html"}
        }

        def randomizeNum():
            
            #self.after(5)
            temp = randint(1,20)
            self.someNumber = temp

            # Get the dictionary for the selected restaurant
            restaurant_dict = self.restaurant_images.get(self.someNumber)

            # If the dictionary exists, get the image path; otherwise, use the default image path
            image_path = self.dir_path + (restaurant_dict["image"] if restaurant_dict else "/images/question-mark.gif")

            # Initialize image of restaurant logo
            image = Image.open(image_path)
            self.randomImage = ImageTk.PhotoImage(image)
            self.imageLabel.config(image=self.randomImage)

            # Bind the click event to the image label
            self.imageLabel.bind("<Button-1>", self.open_webpage)

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
        image_path = self.dir_path + self.restaurant_images.get(self.someNumber, "/images/question-mark.gif")
        self.randomImage = ImageTk.PhotoImage(Image.open(image_path))

        #create image labels to place the images onto the window
        self.imageLabel = tk.Label(self, image = self.randomImage, bg="#293241")

        #position images
        self.imageLabel.pack(side = "bottom", expand = "true", padx=10, pady=10)

    def open_webpage(self, event):
        # Get the selected restaurant number
        restaurant_number = self.someNumber

        # Get the image path and website URL for the selected restaurant
        restaurant_dict = self.restaurant_images[restaurant_number]
        image_path = self.dir_path + restaurant_dict["image"]
        website_url = restaurant_dict["website"]

        # Update the image in the imageLabel widget
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        self.imageLabel.config(image=photo)
        self.imageLabel.image = photo  # Keep a reference to the image object to prevent it from being garbage collected

        # Open the website in the default web browser
        webbrowser.open(website_url)
        

class FastFood(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        self.someNumber = 0

        #retrieve directory path
        self.dir_path = os.path.dirname(os.path.realpath(__file__))

        self.fastfood_images = {
            1: {"image": "/images/fast_food/mcdonalds.jpg", "website": "https://www.mcdonalds.com"},
            2: {"image": "/images/fast_food/in-n-out.jpg", "website": "https://www.in-n-out.com"},
            3: {"image": "/images/fast_food/canes.png", "website": "https://www.raisingcanes.com"},
            4: {"image": "/images/fast_food/c-fil-a.png", "website": "https://www.chick-fil-a.com"},
            5: {"image": "/images/fast_food/culvers.jpg", "website": "https://www.culvers.com"},
            6: {"image": "/images/fast_food/j-in-b.png", "website": "https://www.jackinthebox.com"},
            7: {"image": "/images/fast_food/sonic.jpg", "website": "https://www.sonicdrivein.com"},
            8: {"image": "/images/fast_food/wendys.jpg", "website": "https://www.wendys.com"},
            9: {"image": "/images/fast_food/burger-king.png", "website": "https://www.bk.com"},
            10: {"image": "/images/fast_food/chipotle.png", "website": "https://www.chipotle.com"},
            11: {"image": "/images/fast_food/dominos.png", "website": "https://www.dominos.com"},
            12: {"image": "/images/fast_food/five-guys.jpg", "website": "https://www.fiveguys.com"},
            13: {"image": "/images/fast_food/ikes.png", "website": "https://www.ikesplace.com"},
            14: {"image": "/images/fast_food/panda.jpg", "website": "https://www.pandaexpress.com"},
            15: {"image": "/images/fast_food/pei-wei.png", "website": "https://www.peiwei.com"},
            16: {"image": "/images/fast_food/popeyes.jpg", "website": "https://www.popeyes.com"},
            17: {"image": "/images/fast_food/portillos.png", "website": "https://www.portillos.com"},
            18: {"image": "/images/fast_food/subway.png", "website": "https://www.subway.com"},
            19: {"image": "/images/fast_food/whataburger.jpg", "website": "https://www.whataburger.com"},
            20: {"image": "/images/fast_food/wingstop.jpg", "website": "https://www.wingstop.com"},
            21: {"image": "/images/fast_food/tacobell.jpg", "website": "https://www.tacobell.com"},
            22: {"image": "/images/breakfast/panera.png", "website": "https://www.panerabread.com/en-us/home.html"}
        }
        
        def randomizeNum():
            temp = randint(1,21)
            self.someNumber = temp

            # Get the dictionary for the selected fastfood
            fastfood_dict = self.fastfood_images.get(self.someNumber)

            # If the dictionary exists, get the image path; otherwise, use the default image path
            image_path = self.dir_path + (fastfood_dict["image"] if fastfood_dict else "/images/question-mark.gif")

            # Initialize image of restaurant logo
            image = Image.open(image_path)
            self.randomImage = ImageTk.PhotoImage(image)
            self.imageLabel.config(image=self.randomImage)

            # Bind the click event to the image label
            self.imageLabel.bind("<Button-1>", self.open_webpage)

        
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
        imagePath = Image.open(self.dir_path + "/images/question-mark.gif")
        self.randomImage = ImageTk.PhotoImage(imagePath)

        #create image labels to place the images onto the window
        self.imageLabel = tk.Label(self, image = self.randomImage, bg="#293241")

        #position images
        self.imageLabel.pack(side = "bottom", expand = "true", padx=10, pady=10)

    def open_webpage(self, event):
        # Get the selected fastfood number
        fastfood_number = self.someNumber

        # Get the image path and website URL for the selected fastfood
        fastfood_dict = self.fastfood_images[fastfood_number]
        image_path = self.dir_path + fastfood_dict["image"]
        website_url = fastfood_dict["website"]

        # Update the image in the imageLabel widget
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        self.imageLabel.config(image=photo)
        self.imageLabel.image = photo  # Keep a reference to the image object to prevent it from being garbage collected

        # Open the website in the default web browser
        webbrowser.open(website_url)


class BreakfastFood(Page):
    
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        # Define a dictionary to map breakfast numbers to image paths and websites
        self.breakfast_images = {
            0: {"image": "/images/question-mark.gif", "website": "http://www.jameszanetti.com"},
            1: {"image": "/images/breakfast/snooze.png", "website": "http://www.snooze.com"},
            2: {"image": "/images/breakfast/crepe-club.png", "website": "https://www.thecrepeclub.com/"},
            3: {"image": "/images/breakfast/einsteins.png", "website": "https://www.einsteinbros.com/"},
            4: {"image": "/images/breakfast/morning-squeeze.jpg", "website": "http://www.morningsqueeze.com"},
            5: {"image": "/images/breakfast/sunnys.jpg", "website": "http://www.sunnys.com"},
            6: {"image": "/images/breakfast/first-watch.jpg", "website": "http://www.firstwatch.com"},
            7: {"image": "/images/breakfast/nektar.png", "website": "http://www.nektar.com"},
            8: {"image": "/images/breakfast/starbucks.jpg", "website": "http://www.starbucks.com"},
            9: {"image": "/images/breakfast/dutch.jpg", "website": "http://www.dutchbros.com"},
            10: {"image": "/images/breakfast/jamba.png", "website": "http://www.jamba.com"},
            11: {"image": "/images/fast_food/mcdonalds.jpg", "website": "http://www.mcdonalds.com"},
            12: {"image": "/images/fast_food/c-fil-a.png", "website": "http://www.chick-fil-a.com"},
            13: {"image": "/images/breakfast/ihop.png", "website": "http://www.ihop.com"},
            14: {"image": "/images/breakfast/eggstacy.png", "website": "https://eggstasyaz.com/"},
            15: {"image": "/images/breakfast/br.png", "website": "https://br.coffee/"},
            16: {"image": "/images/breakfast/egg-joe.png", "website": "https://eggnjoe.com/"},
            17: {"image": "/images/breakfast/panera.png", "website": "https://www.panerabread.com/en-us/home.html"},
            18: {"image": "/images/breakfast/black-bear.jpg", "website": "https://blackbeardiner.com/"},
            19: {"image": "/images/breakfast/mimis.jpg", "website": "https://www.mimiscafe.com/"}
        }
        
        #add label to top of the window as program title
        self.programTitle = tk.Label(self, text = "Breakfast Foods", font = ('Chalkboard', 60), bg='#293241', fg='#e0fbfc')
        self.programTitle.pack(padx = 5, pady = 20)

        self.someNumber = 0

        #retrieve directory path
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        
        def randomizeNum():
            temp = randint(1,19)
            self.someNumber = temp

            # Get the dictionary for the selected breakfast
            breakfast_dict = self.breakfast_images.get(self.someNumber)

            # If the dictionary exists, get the image path; otherwise, use the default image path
            image_path = self.dir_path + (breakfast_dict["image"] if breakfast_dict else "/images/question-mark.gif")

            # Initialize image of restaurant logo
            image = Image.open(image_path)
            self.randomImage = ImageTk.PhotoImage(image)
            self.imageLabel.config(image=self.randomImage)

            # Bind the click event to the image label
            self.imageLabel.bind("<Button-1>", self.open_webpage)
            
        
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
        imagePath = Image.open(self.dir_path + "/images/question-mark.gif")
        self.randomImage = ImageTk.PhotoImage(imagePath)

        #create image labels to place the images onto the window
        self.imageLabel = tk.Label(self, image = self.randomImage, bg="#293241")

        #position images
        self.imageLabel.pack(side = "bottom", expand = "true", padx=10, pady=10)
    
    def open_webpage(self, event):
        # Get the selected breakfast number
        breakfast_number = self.someNumber

        # Get the image path and website URL for the selected breakfast
        breakfast_dict = self.breakfast_images[breakfast_number]
        image_path = self.dir_path + breakfast_dict["image"]
        website_url = breakfast_dict["website"]

        # Update the image in the imageLabel widget
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        self.imageLabel.config(image=photo)
        self.imageLabel.image = photo  # Keep a reference to the image object to prevent it from being garbage collected

        # Open the website in the default web browser
        webbrowser.open(website_url)


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
