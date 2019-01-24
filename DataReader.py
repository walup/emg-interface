
from Arduino import Arduino
import threading
import time
import csv
from GraphSocket import GraphSocket

class DataReader(Arduino,GraphSocket):
    #time measurement
    start = 0
    end= 0
    t = 0
    #Reading boolean
    reading = False
    
    #The array of times
    timeData = []
    
    #The array of data
    dataArray = []
    
    #The arduino
    arduino = None
    
    #The read thread
    readThread = None
    
    #Stop thread event
    stopEvent = None
    
    #A variable to store the acquisition time
    maxTime = 0
    #Constructor
    
    #The directory where we will export the data
    directory = ''
    
    #Graph
    graph =None
    
    #delta
    delta = 0.01
    
    def __init__(self,baudRate,port):
        #Initialize the super class
        Arduino.__init__(self,baudRate,port)
        
        
    #The start reading function
    def startReading(self,acquisitionTime,directory):
        #Set the acquisition time
        self.maxTime = acquisitionTime
        #Set the directory
        self.directory = directory
        
        #Restart the arrays
        self.timeData = []
        self.dataArray = []
        self. t = 0
        self.start = 0
        self.end = 0
        #Start the thread and the event
        #initialize the stop event
        self.stopEvent = threading.Event()
        #Initialize the thread
        self.readThread = threading.Thread(target = self.read)
        self.readThread.daemon = True
        self.readThread.start()
        
    #Will tell us if the thread was stopped 
    def isStopped(self):
        return self.stopEvent.is_set()
    
    #Call when you want to stop the thread 
    def stop(self):
        self.stopEvent.set()
        self.close()
            
            
    def isReading(self):
        return self.reading
    
    def read(self):
        #Thread will run as long as we don't stop it
        while(not self.isStopped()):
            #Start the clock
            
            #Use the arduino method for reading data
            newData = self.readData()
            #if it is not None then we add it
            if(newData != None):
                self.t += self.delta
                self.timeData.append(self.t)
                self.dataArray.append(newData)
                #update parameters of the graph
                if(self.isGraphAttached()):
                    self.renderGraph()
                if(self.t > self.maxTime):
                    self.stop()
                    if(self.isGraphAttached()):
                        self.stopGraph()
                    #export the data
                    self.exportData()
    def tic(self):
        self.start = time.time()
       
    def toc(self):
        self.end = time.time()
        self.end = self.end-self.start
        
    #Export data function
    def exportData(self):
        with open(self.directory,'w',newline = '') as f:
            #Create the writer
            paperbackWriter  = csv.writer(f)
            #First column
            paperbackWriter.writerow(['time','Voltage'])
            #Write the data 
            for i in range(1,len(self.timeData)):
                paperbackWriter.writerow([self.timeData[i],self.dataArray[i]])
        print("Data exported")
    
    #override the render function
    def renderGraph(self):
        #update the x and y arrays
        self.graph.updateXArray(self.timeData)
        self.graph.updateYArray(self.dataArray)
        #update the current index
        self.graph.updateCurrentIndex(len(self.dataArray)-1)
        