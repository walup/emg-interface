
#This will be basically
#A signal dictionary

from Signal import Signal

class SignalDictionary():
    #the dictionary
    signalDictionary = {}
    
    #The constructor 
    def __init__(self):
        pass
        
        
    def addSignal(self,sendFunc):
        #get the name
        name = sendFunc.getSignalName()
        #get the signal array
        signal = sendFunc
        #add it to the dictionary
        self.signalDictionary[name] = signal

    def getSignal(self,signalName):
        try:
            return self.signalDictionary[signalName]
            
        except KeyError:
            print("La señal escogida aun no existe")
            print(signalName)
            return None
    
        
        