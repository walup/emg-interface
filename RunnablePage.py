
#Runnable Page to be overriden by
#Other classes
import tkinter as tk
from tkinter import ttk

class RunnablePage(tk.Frame):
    
    running = False;
    pageName = ""
    title = None
    
    def __init__(self,parent,controller):
        #Call constructor of the superclass
        tk.Frame.__init__(self,parent)
        
    #Sorry i love setters and getters

    def isRunning(self):
        return self.running
        
    def setRunning(self,running):
        self.running = running
        
    def setPageName(self,pageName):
        self.pageName = pageName
    
    def getPageName(self):
        return self.pageName
    def start(self):
        pass
    
    
    