# the full study page
from EMGPanel import EMGPanel
from ESPanel import ESPanel
from Graph import Graph
import tkinter as tk
from tkinter import ttk
from EMGPanel import EMGPanel
from ESPanel import ESPanel
from Graph import Graph
from DataReader import DataReader
from DataSender import DataSender
from RunnablePage import RunnablePage
from Graph import Graph
from Graph import GraphParameters
class FullStudyPage(RunnablePage):
    #Emg Panel
    emgPanel = None
    #ES panel
    esPanel = None
    #start full study button
    startButton = None
    #We have two graphs, one for the emg and one for the elctroestimulator
    emgGraph = None
    esGraph = None
    #The sender and the reader
    dataReader = None
    dataSender = None
    
    #the constructor
    def __init__(self,parent,controller):
        #initialize the super class
        RunnablePage.__init__(self,parent,controller)
        
        #initialize the EMGPanel
        self.emgPanel = EMGPanel(self,parent)
        
        #initalize the ESPanel
        self.esPanel = ESPanel(self,parent)
        
        #initialize the emg graph with its parameters
        
        emgParameters = GraphParameters()
        emgParameters.setXLabel("Tiempo (s)")
        emgParameters.setYLabel("Voltaje (V)")
        emgParameters.setTitle("EMG")
        self.emgGraph = Graph(self,parent,emgParameters)
        #initialize the es graph
        esParameters = GraphParameters()
        esParameters.setXLabel("Canal")
        esParameters.setYLabel("Voltaje (V)")
        esParameters.setTitle("Electroestimulador")
        self.esGraph = Graph(self,parent,esParameters)
        
        #initialize the button
        self.startButton = ttk.Button(self,text = "Comenzar Envio/Adquisición",command = lambda : self.start())
        
        #add everithing to the grid
        self.emgPanel.grid(row = 0,column = 0)
        self.esPanel.grid(row = 0,column = 1)
        self.emgGraph.grid(row = 1,column = 0)
        self.esGraph.grid(row = 1,column = 1)
        self.startButton.grid(row = 2,column = 0)
        
        self.setPageName("FullPage")
        
        
    #override the start method
    def start(self):
        #lets divide this first get everything from the esPanel
        esTime = self.esPanel.getTime()
        esFrequency = self.esPanel.getFrequency()
        esAmplitude = self.esPanel.getVoltage()
        esType = self.esPanel.getSignalType()
        esSignalLive= self.esPanel.isSignalLive()
        #boolen that tells us we can start the ES
        
        startES = esTime != None and esFrequency != None and esAmplitude != None and esType != None and esSignalLive != None
        #now get everything from the emgPanel
        emgTime = self.emgPanel.getTime()
        emgBaudRate = self.emgPanel.getBaudRate()
        emgDirectory = self.emgPanel.getDirectory()
        emgPort = self.emgPanel.getPort()
        emgSignalLive = self.emgPanel.isSignalLive()
        
        #boolean that tells us we can start the EMG
        startEMG = emgTime != None and emgBaudRate != None and emgDirectory != None and emgPort != None and emgSignalLive != None
        
        print("got here")
        if(startEMG and startES):
            print("started")
            #Remember how we start stuff
            #for EMG first create the object with the specified baudrate and port
            self.dataReader = DataReader(emgBaudRate,emgPort)
            #now start the reading with the specified time
            #and the specified directory
            self.dataReader.startAcquisition(emgTime,emgDirectory)
            #attach a graph if specified
            if(emgSignalLive):
                self.dataReader.attachGraph(self.emgGraph)
                self.emgGraph.startGraph()
            
            #For the ES we start the sender first
            #it doesnt really require any parameter initially
            self.dataSender = DataSender()
            if(esSignalLive):
                #attach the graph
                self.dataSender.attachGraph(self.esGraph)
                #start sending
                self.dataSender.startSending(esType.name,esTime,esFrequency,esAmplitude)
                #start the graph
                self.graph.startGraph()
            else:
                self.dataSender.startSending(esType.name,esTime,esFrequency,esAmplitude)
        
        else:
            return
            
        
        
    