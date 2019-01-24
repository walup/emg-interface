#Arduino will be a serial object
#with its own cycle and with advanced
#capabilities for acquiring data

import serial

class Arduino():
    #The serial object
    arduinoSerial = None
    
    def __init__(self, baudRate, port):
        #Initialize the serial
        print("puerto abierto "+port)
        print("baudRate "+ str(baudRate))
        self.arduinoSerial = serial.Serial(port,baudRate)        

    #Funcion de lectura de datos
    def readData(self):
        if(self.arduinoSerial.inWaiting() > 0):
            newData = self.arduinoSerial.readline()
            try:
                newData.decode('utf-8')
                newData = float(newData)
                return newData
            except ValueError:
                print("No se pudo procesar el número leido")
                return None
    #Function for closing the serial object
    def close(self):
        self.arduinoSerial.close()
    
        
        
        
    