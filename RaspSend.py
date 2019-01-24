
import RPi.GPIO as GPIO

class RaspSend():
    portsOut = [15, 13, 11, 7, 12, 16, 18, 22]
    offConfiguration = [0,0,0,0,1,0,0,0]
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        #configure ports
        self.configurePorts()
        
    def getPortsOut(self):
        return self.portsOut
    def setPortsOut(self,newPorts):
        self.portsOut = newPorts
    def changePort(self,index,newPort):
        self.PortsOut[index] = newPort
    def configurePorts(self):
        for port in self.portsOut:
            GPIO.setup(port, GPIO.OUT)
    
    def turnOff(self):
        for i in range(0,7):
            GPIO.output(self.portsOut[i],self.offConfiguration[i])
    def sendValue(self,index,value):
        GPIO.output(self.portsOut[index],value)
    
    
        
        
        
        
        