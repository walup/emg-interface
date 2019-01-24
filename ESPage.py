from RunnablePage import RunnablePage
from ESPanel import ESPanel
import tkinter as tk
from tkinter import ttk 
from DataSender import DataSender
from Graph import Graph
from Graph import GraphParameters

class ESPage(RunnablePage):
    
    #ESPanel
    esPanel = None
    
    #Start sending button
    startButton = None
    
    #The data sender
    dataSender = None
    
    #the graph
    graph = None
    
    #Constructor
    def __init__(self,parent,controller):
        #Initialize the superclass
        RunnablePage.__init__(self,parent,controller)
        #start the esPanel
        self.esPanel = ESPanel(self,parent)
        #Start the sender
        self.dataSender = DataSender()
        #the title
        self.title = tk.Label(self, text = "Interfaz ES", font = self.esPanel.getFont())
        #StartButton
        self.startButton = ttk.Button(self,text = "Comenzar envío", command = lambda:self.start())
        #graph parameters
        graphParameters = GraphParameters()
        graphParameters.setXLabel("Canal")
        graphParameters.setYLabel("bits")
        graphParameters.setTitle("Electroestimulador")
        
        #Initialize the graph
        self.graph = Graph(self,parent,graphParameters)
        #Pack the stuff
        self.esPanel.pack()
        self.startButton.pack()
        self.graph.pack()
        #Establish the id
        self.setPageName("ESPage")

        
        
    def start(self):
        #get the type of signal
        signalType = self.esPanel.getSignalType().name
        #get the voltage
        amplitude = self.esPanel.getVoltage()
        #get the time
        maxTime = self.esPanel.getTime()
        #get the frequency
        frequency = self.esPanel.getFrequency()
        if(signalType != None and amplitude != None and maxTime != None and frequency != None):
            
            #If the signal is live attach a graph
            ##to the data sender (remember that it extends GraphSocket)
            if(self.esPanel.isSignalLive()):
                print("signal live")
                self.dataSender.attachGraph(self.graph)
                self.dataSender.startSending(signalType,maxTime,frequency,amplitude)
                self.graph.startGraph()
            else:
                self.dataSender.startSending(signalType,maxTime,frequency,amplitude)
                
        else:
            print("No se pudo iniciar el envio")
            return
            
        