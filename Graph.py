import matplotlib
from matplotlib import style
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import  matplotlib.animation as animation
import tkinter as tk 

class Graph(tk.Frame):
    #The number of points displaying at any given time
    GRAPH_LENGTH = 150
    #The refresh time in miliseconds
    REFRESH_TIME = 1000
    #The data arrays 
    xArray = []
    yArray = []
    #indexes used for displaying the data
    currentIndex = 0
    offset = 0
    #figure
    fig = None
    a = None
    #the animation
    ani = None
    #the title of the graph
    title = None
    yLabel = None
    xLabel = None
    prettify = False
    def __init__(self,parent,controller,params):
        #the style to use
        style.use("ggplot")
        #Initialize the superclass
        tk.Frame.__init__(self,parent)
        #Initialize a figure and add a subplot to it
        self.fig = Figure(figsize = (5,5),dpi = 100)
        self.a = self.fig.add_subplot(1,1,1)
        
        #To begin with we will plot a constant
        #function to the figure
        xArray = [1,2,3]
        yArray = [1,1,1]
        
        #get the params
        if(params != None):
            self.xLabel = params.get("xLabel")
            self.yLabel = params.get("yLabel")
            self.title = params.get("title")
            self.prettify()
        #Plot it
        self.plotStaticSignal(xArray,yArray)
    
    def plotStaticSignal(self,xArray,yArray):
        self.a.plot(xArray,yArray)
        self.adornGraph()
        canvas = FigureCanvasTkAgg(self.fig,self)
        canvas.show()
        canvas.get_tk_widget().pack(side = tk.TOP,fill = tk.BOTH,expand=True)   
        
        #Add the tool bar
        toolBar = NavigationToolbar2TkAgg(canvas,self)
        toolBar.update()
        canvas._tkcanvas.pack(side = tk.TOP,fill = tk.BOTH,expand=True)
        print("plotted")
    
    def updateGraph(self,i):
        print("updating graph")
        self.a.clear()
        #if we are using a particular xArray
        #then we plot both the xArray and the yArray
        #else we will treat the xArray as it was composed of
        #channels
        if(self.isXArrayWorking()):
            #case where we don't have enough points
            if(self.currentIndex <= self.GRAPH_LENGTH):
                self.a.plot(self.xArray[0:self.currentIndex],self.yArray[0:self.currentIndex],color = "blue")
                self.adornGraph()
            elif(self.currentIndex > self.GRAPH_LENGTH):
                #update the offset
                self.updateOffset()
                #plot a sub array
                cutArrayX = self.xArray[self.offset : self.currentIndex]
                cutArrayY = self.yArray[self.offset : self.currentIndex]
                self.a.plot(cutArrayX,cutArrayY,color = "blue")
                self.adornGraph()
        else:
            if(self.currentIndex <= self.GRAPH_LENGTH):
                self.a.plot(self.yArray[0:self.currentIndex],color = "blue")
                self.adornGraph()
            elif(self.currentIndex > self.GRAPH_LENGTH):
                self.updateOffset()
                cutArrayY = self.yArray[self.offset : self.currentIndex]
                self.a.plot(cutArrayY,color = "blue")
                self.adornGraph()
        
    def startGraph(self):
        print("started graph")
        self.ani = animation.FuncAnimation(self.fig,self.updateGraph,repeat = True,interval =1000)
        self.ani._start()
        
    def stopGraph(self):
        self.ani.event_source.stop()
    
    def getLength(self):
        if(self.yArray!= None):
            return len(self.yArray)
        else:
            return 0
        
    def updateYArray(self,yArray):
        self.yArray = yArray
        
    def updateXArray(self, xArray):
        self.xArray = xArray
    def updateCurrentIndex(self,newIndex):
        self.currentIndex = newIndex
    
    def isXArrayWorking(self):
        return len(self.xArray) == len(self.yArray)
    def updateOffset(self):
        self.offset = self.currentIndex-self.GRAPH_LENGTH
    def adornGraph(self):
        if(self.prettify):
            self.a.set(xlabel = self.xLabel,ylabel = self.yLabel,title = self.title)
    def prettify(self):
        #If labels and title are not none then set prettify to true
        if(self.xLabel != None and self.yLabel != None and self.title != None):
            self.prettify = True

class GraphParameters():
    parameters = {}
    #set x label 
    def setXLabel(self,xLabel):
        self.parameters["xLabel"] = xLabel
    def setYLabel(self,yLabel):
        self.parameters["yLabel"] = yLabel
    def setTitle(self,title):
        self.parameters["title"] = title
    def get(self,key):
        try:
            return self.parameters[key]
        except KeyError:
            return None
        
        
        