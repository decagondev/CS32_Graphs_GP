from queue import Queue
from stack import Stack
# lets do a graph adjacency list
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex Does not exist!")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        # create an empty queue and enqueue a starting vertex

        # create a set to store the visited vertices

        # while the queue is not empty
            # dequeue the first vertex

            # if vertex has not been visited
                # mark the vertex as visited
                # print it for debug

                # add all of it's neighbors to the back of the queue
        pass

    def dft(self, starting_vertex_id):
        pass
    
    def bfs(self, starting_vertex_id, target_vertex_id):
        pass

    def dfs(self, starting_vertex_id, target_vertex_id):
        pass
    