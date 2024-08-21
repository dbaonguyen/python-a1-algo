# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent list implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List, Tuple
from maze.util import Coordinates
from maze.graph import Graph


class EdgeListGraph(Graph):
    """
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    def __init__(self):
        ### Implement me! ###
        self.edges: List[Tuple[Coordinates, Coordinates, bool]] = []
        self.vertices: set[Coordinates] = set()
        
    


        
    def addVertex(self, label:Coordinates):
        ### Implement me! ###
        if label not in self.vertices:
            self.vertices.add(label)
        



    def addVertices(self, vertLabels:List[Coordinates]):
        ### Implement me! ###
        for label in vertLabels:
            self.addVertex(label)
        



    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        ### Implement me! ###
        if vert1 in self.vertices and vert2 in self.vertices:
            if (vert1, vert2, addWall) not in self.edges:
                self.edges.append((vert1, vert2, addWall))
                return True
            
        return False
        # remember to return booleans
        
        


    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        ### Implement me! ###
        for i, (v1, v2, _) in enumerate(self.edges):
            if (v1 == vert1 and v2 == vert2) or (v1 == vert2 and v2 == vert1):
                self.edges[i] = (v1, v2, wallStatus)
                return True
            
        return False
        
        # remember to return booleans
        
        



    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        for edge in self.edges:
            if (edge[0] == vert1 and edge[1] == vert2) or (edge[0] == vert2 and edge[1] == vert1):
                self.edges.remove(edge)
                return True
        return False
        
        # remember to return booleans
        
        


    def hasVertex(self, label:Coordinates)->bool:
        ### Implement me! ###
        return label in self.vertices
        # remember to return booleans
        



    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        for v1, v2, _ in self.edges:
            if (v1 == vert1 and v2 == vert2) or (v1 == vert2 and v2 == vert1):
                return True
        return False
        # remember to return booleans
        



    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        for v1, v2, wall in self.edges:
            if (v1 == vert1 and v2 == vert2) or (v1 == vert2 and v2 == vert1):
                return wall
        return False
        # remember to return booleans
        
        
    


    def neighbours(self, label:Coordinates)->List[Coordinates]:
        ### Implement me! ###
        neighbours = []
        for v1, v2, _ in self.edges:
            if v1 == label:
                neighbours.append(v2)
            elif v2 == label:
                neighbours.append(v1)
        return neighbours
        # remember to return list of coordinates
        
        