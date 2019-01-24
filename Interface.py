import tkinter as tk
from StartPage import StartPage
from EMGPage import EMGPage
from ESPage import ESPage
from FullStudyPage import FullStudyPage

class Interface(tk.Tk):
    #containter
    container = None
    
    #The pages
    startPage = None
    emgPage = None
    esPage = None
    fullStudyPage = None
    
    #Page dictionary
    pageDictionary = {}
    
    #Current page
    currentPage = None
    
    #The constructor
    def __init__(self,*args,**kwargs):
        #Initialize the super class
        tk.Tk.__init__(self,*args,**kwargs)
        # The title of the window
        tk.Tk.wm_title(self,"Interfaz EMG/ES")
        #Frame of the window
        self.container = tk.Frame(self)
        #Pack the window
        self.container.pack(side = "top",fill = "both",expand = True)
        #=First parameter is min size, second is priority=#
        self.container.grid_rowconfigure(0,weight = 1)
        self.container.grid_columnconfigure(0,weight = 1)
        #Create the pages notice that the controller is this class
        self.startPage = StartPage(self.container,self)
        self.startPage.grid(row = 0,column = 0,sticky = "nsew")
        self.emgPage = EMGPage(self.container,self)
        self.emgPage.grid(row = 0,column = 0,sticky = "nsew")
        self.esPage = ESPage(self.container,self)
        self.esPage.grid(row = 0,column = 0,sticky = "nsew")
        self.fullStudyPage = FullStudyPage(self.container,self)
        self.fullStudyPage.grid(row = 0,column = 0,sticky = "nsew")
        
        #Add the pages to the dictionary
        self.pageDictionary[self.startPage.getPageName()] = self.startPage
        self.pageDictionary[self.emgPage.getPageName()] = self.emgPage
        self.pageDictionary[self.esPage.getPageName()] = self.esPage
        self.pageDictionary[self.fullStudyPage.getPageName()] = self.fullStudyPage
        
        for x in self.pageDictionary:
            print(x)
        
        #Now we start with the StartPage on the front
        self.showFrame("StartPage")
        
    def showFrame(self,frameName):
        #You look in the dictionary for the requested frame
        #and then raise it to the front
        self.currentPage = self.pageDictionary[frameName]
        self.currentPage.tkraise()
        #Announce that you've raised the page
        print("New Page Raised: "+frameName)
        

        
        
        
        
    