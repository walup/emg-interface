import tkinter as tk
#This are going to be frames which we
#can add to the pages if we want.
#We have one EMGPanel and one ESPanel


class EMGPanel(tk.Frame):
    
    #Font
    FONT = ("Verdana",12)
    ENTRY_WIDTH = 10
    
    #Fields
    timeField = None
    comField = None
    directoryField = None
    baudRateField = None
    
    #A checkbox
    watchSignalBox = None
    watchSignal = None
    
    #The labels
    timeLabel = None
    comLabel = None
    directoryLabel = None
    watchSignalLabel = None
    baudRateFieldLabel = None
    
    
    def __init__(self,parent,controller):
        #Initialize the super class
        tk.Frame.__init__(self,parent,bd = 1)
        
        #Initialize the labels
        self.timeLabel = tk.Label(self,text = "Tiempo",font = self.FONT)
        self.comLabel = tk.Label(self,text = "Puerto",font = self.FONT)
        self.directoryLabel = tk.Label(self,text = "Directorio",font = self.FONT)
        self.baudRateLabel = tk.Label(self,text = "Baud Rate", font = self.FONT)
        
        
        #Initialize the fields
        self.timeField=tk.Entry(self,width = self.ENTRY_WIDTH)
        self.comField = tk.Entry(self,width = self.ENTRY_WIDTH)
        self.directoryField = tk.Entry(self,width = self.ENTRY_WIDTH)
        self.baudRateField = tk.Entry(self,width = self.ENTRY_WIDTH)
        
        #The predefined values of some of the fields
        self.timeField.insert(0,'60')
        self.comField.insert(0,'/dev/ttyACM0')
        self.baudRateField.insert(0,'9600')
        self.directoryField.insert(0,'data.csv')
        
    
        #Initialize the checkbutton
        self.watchSignal = tk.BooleanVar()
        self.watchSignalBox = tk.Checkbutton(self, text = "Ver registro en vivo", variable = self.watchSignal,onvalue = True, offvalue = False, height=5,width = 20)
        
    
        
        #Add it to the grid
        self.timeLabel.grid(row = 0,column = 0)
        self.timeField.grid(row = 0,column = 1)
        self.comLabel.grid(row = 0,column = 2)
        self.comField.grid(row = 0,column = 3)
        self.baudRateLabel.grid(row = 1,column = 0)
        self.baudRateField.grid(row = 1,column = 1)
        self.directoryLabel.grid(row = 1,column = 2)
        self.directoryField.grid(row = 1,column = 3)
        self.watchSignalBox.grid(row = 2,column = 0)
    
    #Funciones para regresar los datos de los campos
        
    def getDirectory(self):
        return self.directoryField.get()
    
    def getTime(self):
        time = self.timeField.get()
        #Try to cast it to a float
        try:
            time = float(time)
            return time
            
        except valueError:
            print("El tiempo introducido debe ser un número")
            return None
    
    def getBaudRate(self):
        baudRate = self.baudRateField.get()
        #Try to cast it to an int
        try:
            baudRate = int(baudRate)
            return baudRate
        except ValueError:
            print("BaudRate debe ser un entero")
            return None
    
    def isSignalLive(self):
        print("Value "+str(self.watchSignal.get()))
        return self.watchSignal.get()
    
    def getPort(self):
        return self.comField.get()
    
    def getFont(self):
        return self.FONT
    
    #Returns a string with all the parameters
    #Packed in a neat way
    
    def toString(self):
        str = ""
        str += "Tiempo: "
        str+= getTime()
        str+= "\tPuerto: "
        str+= getPort()
        #Salto de linea
        str+="\n"
        str += "Directorio: "
        str+= getDirectory()
        str+= "\tBaudRate: "
        str+= getBaudRate()
        str+="\n"
        str += "Signal live: "
        str+= isSignalLive()
        
        return str
        
    
    
    
    
        
        
    
    