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
        q = Queue()
        q.enqueue(starting_vertex_id)

        # create a set to store the visited vertices
        visited = set()

        # while the queue is not empty
        while q.size > 0:
            # dequeue the first vertex
            v = q.dequeue()

            # if vertex has not been visited
            if v not in visited:
                # mark the vertex as visited
                visited.add(v)
                # print it for debug
                print(v)

                # add all of it's neighbors to the back of the queue
                for next_vertex in self.get_neighbors(v):
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex_id):
        # create an empty stack and push a starting vertex
        s = Stack()
        s.push(starting_vertex_id)

        # create a set to store the visited vertices
        visited = set()

        # while the stack is not empty
        while s.size > 0:
            # pop the first vertex
            v = s.pop()

            # if vertex has not been visited
            if v not in visited:
                # mark the vertex as visited
                visited.add(v)
                # print it for debug
                print(v)

                # add all of it's neighbors to the top of the stack
                for next_vertex in self.get_neighbors(v):
                    s.push(next_vertex)
    
    def bfs(self, starting_vertex_id, target_vertex_id):
        # create an empty queue and enqueue PATH To the Starting Vertex ID

        # q.enqueue([starting_vertex_id])
        # create a set to store visited vertices

        # while the queue is not empty
            # dequeue the first PATH
            # grab the last vertex from the Path

            # check if the vertex has not been visited
                # is this vertex the target?
                    # return the path
                # mark it as visited

                # then add A Path to its neighbors to the back of the queue

                # make a copy of the path
                # append the neighbor to the back of the path
                # enqueue out new path

        # return none
                

        pass

    def dfs(self, starting_vertex_id, target_vertex_id):
        pass
    

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('1', '0')
graph.add_edge('0', '3')
graph.add_edge('3', '0')
print(graph.vertices)