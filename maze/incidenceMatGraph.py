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
        # check if the vertex is already in the graph
        if label not in self.vertices:
            self.vertices.append(label) # add the vertex to the list of vertices
            for row in self.edges: # add a new column to the adjacency matrix
                row.append(False) # set all the new edges to False
            self.edges.append([False] * len(self.vertices)) # add a new row to the adjacency matrix

    def addVertices(self, vertLabels: List[Coordinates]):
        # add all the vertices in the list
        for label in vertLabels:
            self.addVertex(label)

    def addEdge(self, vert1: Coordinates, vert2: Coordinates, addWall: bool = False) -> bool:
        # check if the vertices are in the graph
        if vert1 in self.vertices and vert2 in self.vertices:
            # get the indices of the vertices
            index1 = self.vertices.index(vert1)
            index2 = self.vertices.index(vert2)
            # check if the edge is not already in the graph
            if not self.edges[index1][index2]:
                # add the edge to the adjacency matrix
                self.edges[index1][index2] = True
                self.edges[index2][index1] = True
                return True
        return False

    def updateWall(self, vert1: Coordinates, vert2: Coordinates, wallStatus: bool) -> bool:
        # check if the vertices are in the graph
        if vert1 in self.vertices and vert2 in self.vertices:
            # get the indices of the vertices
            index1 = self.vertices.index(vert1)
            index2 = self.vertices.index(vert2)
            # check if the edge is in the graph
            if self.edges[index1][index2] != wallStatus:
                self.edges[index1][index2] = wallStatus
                self.edges[index2][index1] = wallStatus
                return True
        return False

    def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        # check if the vertices are in the graph
        if vert1 in self.vertices and vert2 in self.vertices:
            # get the indices of the vertices
            index1 = self.vertices.index(vert1)
            index2 = self.vertices.index(vert2)
            # check if the edge is in the graph
            if self.edges[index1][index2]:
                # remove the edge from the adjacency matrix
                self.edges[index1][index2] = False
                self.edges[index2][index1] = False
                return True
        return False

    def hasVertex(self, label: Coordinates) -> bool:
        return label in self.vertices

        



    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        for i in range(len(self.vertices)):
            if self.vertices[i] == vert1:
                index1 = i
            if self.vertices[i] == vert2:
                index2 = i
        return self.edges[index1][index2]




    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        for i in range(len(self.vertices)):
            if self.vertices[i] == vert1:
                index1 = i
            if self.vertices[i] == vert2:
                index2 = i
        return self.edges[index1][index2]
    


    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        neighbors = []
        if label in self.vertices:
            index = self.vertices.index(label)
            for i, connected in enumerate(self.edges[index]):
                if connected:
                    neighbors.append(self.vertices[i])
        return neighbors
    

        