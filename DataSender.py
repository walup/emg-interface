from SignalDictionary import SignalDictionary
from SquareFunc import SquareFunc
import threading
import time
from RaspSend import RaspSend
from GraphSocket import GraphSocket
from BitsConverter import BitsConverter
#The data sender
#extends the SignalDictionary 
class DataSender(SignalDictionary,RaspSend,GraphSocket):
    
    sendThread = None
    currentSignal = None
    threadEvent = None
    maxTime = 0
    t = 0
    startTime = 0
    endTime = 0
    #the constructor
    currentIndex = 0

    
    
    def __init__(self):
        #Initialize the super class
        RaspSend.__init__(self)
        
        #Create the signals
        square = SquareFunc()
        #Add them to the dictionary 
        self.addSignal(square)
        
    def startSending(self,signalType,maxTime,frequency,amplitude):
        #the time
        self.maxTime = maxTime 
        #Establish the current signal
        self.currentSignal = self.getSignal(signalType)
        #If the signal is not none then we procceed to start
        #the thread
        if(self.currentSignal != None):
            #restart times
            self.t = 0
            self.startTime = 0
            self.endTime = 0
            self.currentIndex = 0
            
            #build the signal and start the thread 
            self.currentSignal.buildSignal(self.calibrateAmplitude(amplitude),self.calibrateFrequency(frequency))
            self.threadEvent = threading.Event()
            self.sendThread = threading.Thread(target = self.send)
            self.sendThread.daemon = True
            self.sendThread.start()
            
            if(self.isGraphAttached()):
                array = list(map(BitsConverter.convertBitArray,self.currentSignal.getSignalYArray()))
                self.graph.updateYArray(array)
        #Else we break
        else:
            return
        
    #the function to send data
    def send(self):
        while(not self.isStopped()):
            self.tic()
            #send the signal
            valueArray = self.currentSignal.getYPoint(self.currentIndex)
            print(str(BitsConverter.convertBitArray(valueArray)))
            for i in range(0,7):
                self.sendValue(i,int(valueArray[i]))
            if(self.isGraphAttached()):
                self.renderGraph()
            #increment the index
            self.currentIndex = self.currentIndex+1
            #see if the index has maxed out the size of the array
            if(self.currentIndex >self.currentSignal.getLength()-1):
                self.currentIndex = 0
            #Increment the time and see if it is bigger than the max time
            self.t+= self.endTime
            if(self.t>self.maxTime):
                self.stop()
            self.toc()
            
    #Calibrate amplitude
    def calibrateAmplitude(self,amplitude):
        return (amplitude-0.8054)/1.1003
        
        
    #calibrate frequency 
    def calibrateFrequency(self,frequency):
        return int((frequency/9615.8)**(-0.9699321))
    
    #Function to stop the thread
    def stop(self):
        #set the thread event
        self.threadEvent.set()
        #stop the sender
        self.turnOff()
        if(self.isGraphAttached()):
            self.stopGraph()
        print("Stopped sending")
        
        
    def isStopped(self):
        return self.threadEvent.is_set()
    #starts the clock
    def tic(self):
        self.startTime = time.time()
    #ends the clock
    def toc(self):
        self.endTime = time.time()
        self.endTime = self.endTime-self.startTime
        
    #Methods of GraphSocket
    def renderGraph(self):
        self.graph.updateCurrentIndex(self.currentIndex)
    
        
        
        
        