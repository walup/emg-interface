from Signal import Signal 

#This will be the class to be extended by all the SendFunctions that
#we create

class SendFunc():
    BITS_RANGE =128
    VOLTAGE_RANGE = 24
    
    #signal
    signalType = None
    
    #The x array
    xArray = None
    
    #The y array
    yArray  = None
    
    #Amplitude and frequency
    amplitude = 0
    frequency = 0
    
    
    #The constructor
    def __init__(self,signalType):
        #Set the signal
        self.signalType = signalType
        
        
        #Initialize the arrays
        self.xArray = []
        self.yArray = []
        
    def buildSignal(self,amplitude,frequency):
        pass
    
    #Return the length of the signal
    def getLength(self):
        return len(self.yArray)
    
    #Get the signal type
    def getSignalType(self):
        return self.signalType
    
    #Returns the frequency of the signal
    def getFrequency(self):
        return self.frequency
    
    #Returns the amplitude of the signal
    def getAmplitude(self):
        return self.amplitude
    #Returns the name of the signal
    def getSignalName(self):
        return self.signalType.name
    
    def getSignalYArray(self):
        return self.yArray
    
    def setAmplitude(self,amplitude):
        self.amplitude = amplitude
    
    def setFrequency(self,frequency):
        self.frequency = frequency
        
    def getYPoint(self,index):
        return self.yArray[index]