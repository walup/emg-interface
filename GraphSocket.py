
class GraphSocket():
    graph = None
    
    def isGraphAttached(self):
        return self.graph != None
    
    def attachGraph(self,graph):
        self.graph = graph
    def renderGraph(self):
        pass
    def stopGraph(self):
        self.graph.stopGraph()
        self.graph = None
    