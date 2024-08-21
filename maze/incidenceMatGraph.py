# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent matrix implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List
from maze.util import Coordinates
from maze.graph import Graph


class IncMatGraph(Graph):
    """
    Represents an undirected graph using an adjacency matrix.
    """

    def __init__(self):
        self.vertices: List[Coordinates] = []
        self.edges: List[List[bool]] = []

    def addVertex(self, label: Coordinates):
        if label not in self.vertices:
            self.vertices.append(label)
            for row in self.edges:
                row.append(False)
            self.edges.append([False] * len(self.vertices))

    def addVertices(self, vertLabels: List[Coordinates]):
        for label in vertLabels:
            self.addVertex(label)

    def addEdge(self, vert1: Coordinates, vert2: Coordinates, addWall: bool = False) -> bool:
        if vert1 in self.vertices and vert2 in self.vertices:
            index1 = self.vertices.index(vert1)
            index2 = self.vertices.index(vert2)
            if not self.edges[index1][index2]:
                self.edges[index1][index2] = True
                self.edges[index2][index1] = True
                return True
        return False

    def updateWall(self, vert1: Coordinates, vert2: Coordinates, wallStatus: bool) -> bool:
        if vert1 in self.vertices and vert2 in self.vertices:
            index1 = self.vertices.index(vert1)
            index2 = self.vertices.index(vert2)
            if self.edges[index1][index2] != wallStatus:
                self.edges[index1][index2] = wallStatus
                self.edges[index2][index1] = wallStatus
                return True
        return False

    def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        if vert1 in self.vertices and vert2 in self.vertices:
            index1 = self.vertices.index(vert1)
            index2 = self.vertices.index(vert2)
            if self.edges[index1][index2]:
                self.edges[index1][index2] = False
                self.edges[index2][index1] = False
                return True
        return False

    def hasVertex(self, label: Coordinates) -> bool:
        return label in self.vertices

    def hasEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        if vert1 in self.vertices and vert2 in self.vertices:
            index1 = self.vertices.index(vert1)
            index2 = self.vertices.index(vert2)
            return self.edges[index1][index2]
        return False

    def getWallStatus(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        if vert1 in self.vertices and vert2 in self.vertices:
            index1 = self.vertices.index(vert1)
            index2 = self.vertices.index(vert2)
            return self.edges[index1][index2]
        return False

    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        neighbors = []
        if label in self.vertices:
            index = self.vertices.index(label)
            for i, connected in enumerate(self.edges[index]):
                if connected:
                    neighbors.append(self.vertices[i])
        return neighbors

    
        
        


    def hasVertex(self, label:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        return label in self.vertices
        pass



    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        for i in range(len(self.vertices)):
            if self.vertices[i] == vert1:
                index1 = i
            if self.vertices[i] == vert2:
                index2 = i
        return self.edges[index1][index2]
    
        pass



    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        ### Implement me! ###
        # remember to return booleans
        for i in range(len(self.vertices)):
            if self.vertices[i] == vert1:
                index1 = i
            if self.vertices[i] == vert2:
                index2 = i
        return self.edges[index1][index2]
    
        pass



    def neighbours(self, label:Coordinates)->List[Coordinates]:
        ### Implement me! ###
        # remember to return list of coordinates
        neighbours = []
        for i in range(len(self.vertices)):
            if self.vertices[i] == label:
                index = i
        for i in range(len(self.edges[index])):
            if self.edges[index][i]:
                neighbours.append(self.vertices[i])
        return neighbours
    
        pass
        