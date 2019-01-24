import tkinter as tk
from Signal import Signal
#This is the electrostimulation panel
#like the EMGPanel it will contiani
#ALl the entry widgets and will have
#methods to access them

class ESPanel(tk.Frame):
    
    #The font
    FONT = ('Verdana',12)
    ENTRY_WIDTH = 10
    
    #Labels
    amplitudeLabel = None
    frequencyLabel = None
    signalLabel = None
    timeLabel = None
    wathSignalLabel = None
    
    #Fields
    amplitudeField = None
    frequencyField = None
    timeField = None
    
    #signal list
    signalList = None
    
    #signal
    signal = None
    
    #option to see signal live
    watchSignalBox = None
    watchSignal = None
    
    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        
        #Initialize the labels
        self.amplitudeLabel = tk.Label(self,text = "Amplitud (Volts)")
        self.frequencyLabel = tk.Label(self,text = "Frecuencia (Hz)")
        self.signalLabel = tk.Label(self,text = "Tipo de señal")
        self.timeLabel = tk.Label(self,text = "Tiempo de envío")
        #Initialize the fields
        self.amplitudeField = tk.Entry(self,width = self.ENTRY_WIDTH)
        self.frequencyField = tk.Entry(self,width = self.ENTRY_WIDTH)
        self.timeField = tk.Entry(self,width = self.ENTRY_WIDTH)
        #Predefined values for the fields
        self.amplitudeField.insert(0,"10")
        self.frequencyField.insert(0,"1000")
        self.timeField.insert(0,"60")
        
        self.watchSignal = tk.BooleanVar()
        self.watchSignalBox = tk.Checkbutton(self, text = "Ver registro en vivo", variable = self.watchSignal, \
                 onvalue = True, offvalue = False, height=5, \
                 width = 20)
        #Initialize the signal list
        self.signalList = tk.Listbox(self)
        #Add all the members of Signal to it
        for element in Signal:
            self.signalList.insert(0,element.name)
        self.signalList.select_set(4)    
        #Add everything to the grid
        self.amplitudeLabel.grid(row = 0,column = 0)
        self.amplitudeField.grid(row = 0,column = 1)
        self.frequencyLabel.grid(row = 0,column = 2)
        self.frequencyField.grid(row = 0,column = 3)
        self.timeLabel.grid(row = 1,column = 0)
        self.timeField.grid(row = 1,column = 1)
        self.watchSignalBox.grid(row = 1, column = 2)
        self.signalLabel.grid(row = 2,column = 0)
        self.signalList.grid(row = 2,column = 1)
        
        
    
    #Return the voltage as a number
    def getVoltage(self):
        voltage = self.amplitudeField.get()
        try:
            voltage = float(voltage)
            return voltage
        except ValueError:
            print("El voltaje introducido debe ser un número")
            return None
    #Returens the frequency as a number    
    def getFrequency(self):
        frequency = self.frequencyField.get()
        try:
            frequency = float(frequency)
            return frequency
        except ValueError:
            print("La frecuencia introducida debe ser un número")
            return None
        
    #Return the signal type according to the
    #selected option
    def getSignalType(self):
        try:
            #Get the marked option
            signalOption = self.signalList.get(tk.ACTIVE)
            print(signalOption)
            #assign the correct signal
            self.signalType = Signal[signalOption]
            return self.signalType
                
        except ValueError:
            print("Ninguna opcion seleccionada")
            return None
    
    def getFont(self):
        return self.FONT
    
    def getTime(self):
        maxTime = self.timeField.get()
        try:
            maxTime = float(maxTime)
            return maxTime
        except ValueError:
            print("El tiempo introducido no es un número")
            return None
    
    def isSignalLive(self):
        print("signal live "+str(self.watchSignal.get()))
        return self.watchSignal.get()
        
            
    
    
        
        
        
        
        
        
        
        
        
        
        
        
    