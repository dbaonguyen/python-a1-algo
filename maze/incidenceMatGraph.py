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
        """
        Initializes the graph with an empty list of vertices and an empty adjacency matrix.
        - self.vertices: A list of vertices in the graph.
        - self.edges: A 2D list (matrix) where each entry represents the presence or absence of an edge between two vertices.
        """
        self.vertices: List[Coordinates] = []
        self.edges: List[List[bool]] = []

    def addVertex(self, label: Coordinates):
        """
        Adds a vertex to the graph if it does not already exist.
        
        Parameters:
        - label: The coordinate of the vertex to be added.
        
        This method also updates the adjacency matrix by adding a new row and column for the new vertex.
        """
        if label not in self.vertices:
            self.vertices.append(label)  # Add the vertex to the list of vertices
            for row in self.edges:  # Add a new column to each row in the adjacency matrix
                row.append(False)  # Initialize new edges as False (no edge)
            self.edges.append([False] * len(self.vertices))  # Add a new row to the adjacency matrix

    def addVertices(self, vertLabels: List[Coordinates]):
        """
        Adds multiple vertices to the graph by calling the addVertex method for each label in the list.
        
        Parameters:
        - vertLabels: A list of coordinates representing the vertices to be added.
        """
        for label in vertLabels:
            self.addVertex(label)

    def addEdge(self, vert1: Coordinates, vert2: Coordinates, addWall: bool = False) -> bool:
        """
        Adds an edge between two vertices if both vertices exist in the graph.
        
        Parameters:
        - vert1: The first vertex in the edge.
        - vert2: The second vertex in the edge.
        - addWall: A boolean indicating whether there is a wall between the vertices (not used in the matrix implementation).

        Returns:
        - True if the edge was successfully added, False otherwise.
        """
        if vert1 in self.vertices and vert2 in self.vertices:
            # Get the indices of the vertices
            index1 = self.vertices.index(vert1)
            index2 = self.vertices.index(vert2)
            # Check if the edge is not already in the graph
            if not self.edges[index1][index2]:
                # Add the edge to the adjacency matrix
                self.edges[index1][index2] = True
                self.edges[index2][index1] = True
                return True
        return False

    def updateWall(self, vert1: Coordinates, vert2: Coordinates, wallStatus: bool) -> bool:
        """
        Updates the wall status of an existing edge between two vertices. 
        In this matrix representation, it updates the adjacency matrix with the wall status.
        
        Parameters:
        - vert1: The first vertex in the edge.
        - vert2: The second vertex in the edge.
        - wallStatus: A boolean indicating the new wall status.

        Returns:
        - True if the wall status was successfully updated, False otherwise.
        """
        if vert1 in self.vertices and vert2 in self.vertices:
            # Get the indices of the vertices
            index1 = self.vertices.index(vert1)
            index2 = self.vertices.index(vert2)
            # Update the wall status in the adjacency matrix
            if self.edges[index1][index2] != wallStatus:
                self.edges[index1][index2] = wallStatus
                self.edges[index2][index1] = wallStatus
                return True
        return False

    def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        """
        Removes an edge between two vertices if it exists in the graph.
        
        Parameters:
        - vert1: The first vertex in the edge.
        - vert2: The second vertex in the edge.

        Returns:
        - True if the edge was successfully removed, False otherwise.
        """
        if vert1 in self.vertices and vert2 in self.vertices:
            # Get the indices of the vertices
            index1 = self.vertices.index(vert1)
            index2 = self.vertices.index(vert2)
            # Remove the edge from the adjacency matrix
            if self.edges[index1][index2]:
                self.edges[index1][index2] = False
                self.edges[index2][index1] = False
                return True
        return False

    def hasVertex(self, label: Coordinates) -> bool:
        """
        Checks if a vertex exists in the graph.
        
        Parameters:
        - label: The coordinate of the vertex to check.

        Returns:
        - True if the vertex exists, False otherwise.
        """
        return label in self.vertices

    def hasEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        """
        Checks if an edge exists between two vertices in the graph.
        
        Parameters:
        - vert1: The first vertex in the edge.
        - vert2: The second vertex in the edge.

        Returns:
        - True if the edge exists, False otherwise.
        """
        # Find the indices of the vertices
        for i in range(len(self.vertices)):
            if self.vertices[i] == vert1:
                index1 = i
            if self.vertices[i] == vert2:
                index2 = i
        return self.edges[index1][index2]

    def getWallStatus(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        """
        Retrieves the wall status between two vertices in the graph.
        
        Parameters:
        - vert1: The first vertex in the edge.
        - vert2: The second vertex in the edge.

        Returns:
        - True if there is a wall between the vertices, False otherwise.
        """
        # Find the indices of the vertices
        for i in range(len(self.vertices)):
            if self.vertices[i] == vert1:
                index1 = i
            if self.vertices[i] == vert2:
                index2 = i
        return self.edges[index1][index2]

    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        """
        Finds all neighbors of a given vertex in the graph.
        
        Parameters:
        - label: The coordinate of the vertex whose neighbors are to be found.

        Returns:
        - A list of coordinates representing the neighbors of the vertex.
        """
        neighbors = []
        if label in self.vertices:
            index = self.vertices.index(label)
            # Check the row corresponding to the vertex in the adjacency matrix
            for i, connected in enumerate(self.edges[index]):
                if connected:  # If there is an edge, add the corresponding vertex to the neighbors list
                    neighbors.append(self.vertices[i])
        return neighbors
    

        