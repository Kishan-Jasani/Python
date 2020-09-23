# --> In these scenarios, we understand that we cannot use any of the linear data structures like array, linked list, stack or queue to represent it. 
# --> Here, we need an arrangement which allows to have a set of vertices and edges between them. Such a data structure is known as graph. 

# --> Graph is a non-linear data structure having a set of vertices(or nodes) and edges between vertices. 
# --> It can have any number of edges and nodes and any node can be connected to any other node by an edge. 
# --> It can be implemented using arrays or linked lists.


# Undirected Graph:-
#--> The graph in which edges are not directed from one vertex to another is known as Undirected graph.

# Directed graph:-
# --> The graph in which edges are directed from one vertex to another is known as directed graph.

# Weighted graph:-
# --> The graph in which weights or values are associated with each edge is called weighted edge.


# Common operations possible on graph are listed below.

'''
 Operation                     Description

createGraph()                Create a graph
addNode(node)                add node or vertex
addEdge(node1,node2)         Adds an edge between two nodes
isEmpty()                    Checks whether the graph is empty
isLink(node1,node2)          check whether the edge exist between two node or not?
deleteNode(node)             deletes a node
deleteEdge(node1,node2)      delete edge between two nodes
getNodes()                   gets all vertices
getEdges()                   gets all edges

'''

# Listed below are two common usage scenarios of graphs:
# --> 1. Find the shortest path where path is defined as a sequence of edges which connect a sequence of vertices. 
# -->    Shortest path is used in a weighted graph to find the path that results in the shortest path from a source node to a destination node. 
# -->    It is used to find shortest routes, profitable routes etc.
# --> 2. Detect a cycle in a graph. 
# -->    Cycle consists of a sequence of vertices starting and ending at the same vertex with no repetitions of vertices and edges other than the starting and ending vertex.