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


from typing import List, Tuple, Set
from maze.util import Coordinates

class EdgeListGraph:
    """
    Represents an undirected graph using an edge list. Each edge is stored as a tuple containing two vertices
    and a boolean indicating the presence of a wall between them.
    """

    def __init__(self):
        """
        Initializes the graph with an empty list of edges and an empty set of vertices.
        - self.edges: A list of tuples, where each tuple is of the form (vertex1, vertex2, hasWall).
        - self.vertices: A set of unique vertices (nodes) in the graph.
        """
        self.edges: List[Tuple[Coordinates, Coordinates, bool]] = []
        self.vertices: Set[Coordinates] = set()

    def addVertex(self, label: Coordinates):
        """
        Adds a vertex to the graph if it does not already exist.
        
        Parameters:
        - label: The coordinate of the vertex to be added.
        """
        if label not in self.vertices:
            self.vertices.add(label)

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
        Adds an edge between two vertices if both vertices exist in the graph and the edge does not already exist.
        The edge is represented as a tuple of the form (vertex1, vertex2, hasWall).
        
        Parameters:
        - vert1: The first vertex in the edge.
        - vert2: The second vertex in the edge.
        - addWall: A boolean indicating whether there is a wall between the vertices.

        Returns:
        - True if the edge was successfully added, False otherwise.
        """
        if vert1 in self.vertices and vert2 in self.vertices:
            if (vert1, vert2, addWall) not in self.edges:
                self.edges.append((vert1, vert2, addWall))
                return True
        return False

    def updateWall(self, vert1: Coordinates, vert2: Coordinates, wallStatus: bool) -> bool:
        """
        Updates the wall status of an existing edge between two vertices. If the edge exists, the wall status is updated.
        
        Parameters:
        - vert1: The first vertex in the edge.
        - vert2: The second vertex in the edge.
        - wallStatus: A boolean indicating the new wall status.

        Returns:
        - True if the wall status was successfully updated, False otherwise.
        """
        for i, (v1, v2, _) in enumerate(self.edges):
            if (v1 == vert1 and v2 == vert2) or (v1 == vert2 and v2 == vert1):
                self.edges[i] = (v1, v2, wallStatus)
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
        for edge in self.edges:
            if (edge[0] == vert1 and edge[1] == vert2) or (edge[0] == vert2 and edge[1] == vert1):
                self.edges.remove(edge)
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
        for v1, v2, _ in self.edges:
            if (v1 == vert1 and v2 == vert2) or (v1 == vert2 and v2 == vert1):
                return True
        return False

    def getWallStatus(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        """
        Retrieves the wall status between two vertices in the graph.
        
        Parameters:
        - vert1: The first vertex in the edge.
        - vert2: The second vertex in the edge.

        Returns:
        - True if there is a wall between the vertices, False otherwise.
        """
        for v1, v2, wall in self.edges:
            if (v1 == vert1 and v2 == vert2) or (v1 == vert2 and v2 == vert1):
                return wall
        return False

    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        """
        Finds all neighbors of a given vertex in the graph.
        
        Parameters:
        - label: The coordinate of the vertex whose neighbors are to be found.

        Returns:
        - A list of coordinates representing the neighbors of the vertex.
        """
        neighbours = []
        for v1, v2, _ in self.edges:
            if v1 == label:
                neighbours.append(v2)
            elif v2 == label:
                neighbours.append(v1)
        return neighbours
