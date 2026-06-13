class Graph:
    def __init__(self):
        self.size = 0
        self.nodes = {}

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def createNode(self, node):
        if node in self.nodes:
            raise KeyError(f"Node {node} already exists.")
        
        self.nodes[node] = {}
    
    def connectNode(self, node1, node2):
        self.nodes[node1][node2] = None
        self.nodes[node2][node1] = None
    
    def deleteNode(self, node):
        if node not in self.nodes:
            raise KeyError(f"Node {node} does not exist.")
        
        for neighbour in list(self.nodes[node]):
            del self.nodes[neighbour][node]

        del self.nodes[node]
    
    def weightConnection(self, node1, node2, weight):
        if node1 not in self.nodes or node2 not in self.nodes:
            raise KeyError(f"Both nodes {node1} & {node2} need to exist.")
        
        if weight < 0:
            raise ValueError(f"Weight {weight} cannot be negative.")

        self.nodes[node1][node2] = weight
        self.nodes[node2][node1] = weight
    
    def neighbours(self, node):
        if node not in self.nodes:
            raise KeyError(f"Node {node} does not exist.")
        
        return self.nodes[node]