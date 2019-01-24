from SendFunc import SendFunc
from Signal import Signal
import numpy
import math
#Extends SendFunc
class SquareFunc(SendFunc):
    #Constructor just calls the
    #super class constructor
    
    def __init__(self):
        SendFunc.__init__(self,Signal.SQUARE)
        
    
    
    #We just have to specify our own method for
    #filling the arrays, it HAS to be called
    #buildSignal
    
    
    def buildSignal(self,amplitude,frequency):
        #set the amplitude and frequency
        self.amplitude = amplitude*(self.BITS_RANGE/self.VOLTAGE_RANGE)
        self.frequency = frequency
        #positve signal portion +/total_cycle
        positvePortion = 0.5
        #negative signal portion
        negativePortion = 1-positvePortion
        #x1 is sort of like the point of division between
        #the positive and negative signal
        x1 = int(positvePortion*self.frequency)
        #x2 is the end point
        x2 = int(negativePortion*self.frequency)
        print("x1 "+str(x1))
        print("x2 "+str(x2))
        #The positive amplitude
        positiveAmplitude = int(self.BITS_RANGE+self.amplitude)
        #The negative amplitude  
        negativeAmplitude = int(self.BITS_RANGE)
        #the positive amplitude in bits
        positiveAmplitudeBits = format(positiveAmplitude,'08b')
        #the negative amplitude in bits
        negativeAmplitudeBits = format(negativeAmplitude,'08b')
        
        #Create and fill the signal array
        signalArray = []
        
        #Add the positive portion
        for i in range(0,x1):
            signalArray.append(positiveAmplitudeBits)
        
        #Add the negative portion
        for i in range(0,x2):
            signalArray.append(negativeAmplitudeBits)
        
        #return the array
        self.yArray = signalArray
        print(self.getLength())