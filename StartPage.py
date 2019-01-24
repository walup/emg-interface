#
from RunnablePage import RunnablePage
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

class StartPage(RunnablePage):
    #Contains a title label
    titleLabel = None
    #The font to use for the labels
    TITLE_FONT = ("Verdana",12)
    #The buttons
    emgButton = None
    esButton = None
    completeStudyButton = None
    #the logo
    logo = None
    path = "logo.png"
    imgLabel= None
    LOGO_WIDTH = 250
    LOGO_HEIGHT = 250
    PADDING = 10
    


    #The constructor
    def __init__(self,parent,controller):
        #Call constructor of the superclass
        RunnablePage.__init__(self,parent,controller)
        #Initialize the title
        self.title = tk.Label(self,text = "Interfaz EMG/ES",font = self.TITLE_FONT)
        #initialize the buttons
        self.emgButton = ttk.Button(self,text = "EMG Interface",command = lambda: controller.showFrame("EMGPage"))
        self.esButton = ttk.Button(self,text = "ES Interface",command = lambda: controller.showFrame("ESPage"))
        self.completeStudyButton = ttk.Button(self,text = "EMG && ES", command = lambda: controller.showFrame("FullPage"))
        #the logo
        self.logo = Image.open(self.path)
        self.logo = self.logo.resize((self.LOGO_WIDTH, self.LOGO_HEIGHT), Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(self.logo)
        self.imgLabel = tk.Label(self, image=self.logo)
        #Pack the label
        self.title.pack(pady = 10,padx = 10)
        #Pack the buttons
        self.emgButton.pack(pady = self.PADDING)
        self.esButton.pack(pady = self.PADDING)
        self.completeStudyButton.pack(pady = self.PADDING)
        self.imgLabel.pack(pady = self.PADDING)
        #Set the name of the page
        self.setPageName("StartPage")
        
    
    
