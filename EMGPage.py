from RunnablePage import RunnablePage
from EMGPanel import EMGPanel
import tkinter as tk
from tkinter import ttk
from DataReader import DataReader
from Graph import Graph
from Graph import GraphParameters

class EMGPage(RunnablePage):
    
    #The EMGPanel
    emgPanel = None
    #The start button
    startButton = None
    #The DataReader
    dataReader = None
    #The graph
    graph = None
    
    #The constructor
    def __init__(self,parent,controller):
        #Initialize the superclass
        RunnablePage.__init__(self,parent,controller)
        
        #Initialize the EMGPanel
        self.emgPanel = EMGPanel(self,parent)
        #The title
        self.title = tk.Label(self,text = "Interfaz EMG",font = self.emgPanel.getFont())
        #Initialize the start button
        self.startButton = ttk.Button(self,text = "Iniciar Adquisición",command = lambda:self.start())
        #Some parameters for the graph
        graphParameters = GraphParameters()
        graphParameters.setXLabel("Tiempo (s)")
        graphParameters.setYLabel("Amplitud (V)")
        graphParameters.setTitle("EMG")
        
        #Initialize the graph
        self.graph = Graph(self,parent,graphParameters)
        #Pack the stuff
        self.title.pack(pady = 10,padx = 10)
        self.emgPanel.pack()
        self.startButton.pack()
        self.graph.pack()
        #Set the name of the page
        self.setPageName("EMGPage")
        
    def start(self):
        #Initialize the data reader
        self.dataReader = DataReader(self.emgPanel.getBaudRate(),self.emgPanel.getPort())
        #start the data reader
        self.dataReader.startReading(self.emgPanel.getTime(),self.emgPanel.getDirectory())
        #If the option for live signal is checked
        #then we will activate the plot 
        if(self.emgPanel.isSignalLive()):
            #Add the graph to the reader
            #and start it 
            self.graph.startGraph()
            print("Plot activated")