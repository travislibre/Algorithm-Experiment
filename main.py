from asyncio.windows_events import NULL


class Dijkstra:
    def __init__(self, edges, nodes, start):
        self.edges = edges
        self.nodes = nodes
        self.start = start

        self.distances = {}  # Dictionary that keeps track of the distance from a node to the start node. If it hasnt been visited it is initialized to "INF"
        self.previous = {}  # Dictionary that keep track of previous nodes
        for node in self.nodes:  #
            self.distances[node] = "INF"
            self.previous[node] = None
        self.distances[start] = 0
        self.H = PriorityQueue(self.nodes)

    def update(self,
               edge):  # Each edge is represented by an array where the first element is the start vertex, the second element is the distance, and the third element is the end vertex
        v = edge[2]
        u = edge[0]
        length = edge[1]
        if (self.distances[v] > self.distances[u] + length) and self.distances[u] != 100:  # TODO and
            self.distances[v] = self.distances[u] + length
            self.previous[v] = u
            self.H.decrease_key(v)

    def dijkstra(self):
        while self.H.is_empty() == False:
            u = self.H.delete_min(self.distances)
            for edge in self.edges:
                self.update(edge)


class BellmanFord:
    def __init__(self, edges, nodes, start):
        self.edges = edges
        self.nodes = nodes
        self.start = start

        self.distances = {}  # Dictionary that keeps track of the distance from a node to the start node. If it hasnt been visited it is initialized to "INF"
        self.previous = {}  # Dictionary that keep track of previous nodes
        for node in self.nodes:  #
            self.distances[node] = 10000000
            self.previous[node] = "N"
        self.distances[start] = 0

    def print_current_state(self):  # This method prints the current nodes distances and their previous nodes
        for node in self.nodes:
            dist = self.distances[node]
            prev = self.previous[node]
            # print(f'{dist:>3n}/{prev:<1} | ', end="")
            print(f'{dist:3n} / {prev:1},', end=" ")
        print()

    def update(self,
               edge):  # Each edge is represented by an array where the first element is the start vertex, the second element is the distance, and the third element is the end vertex
        v = edge[2]
        u = edge[0]
        length = edge[1]
        if (self.distances[v] > self.distances[u] + length) and self.distances[u] != 10000000:
            # self.print_current_state()
            self.distances[v] = self.distances[u] + length
            self.previous[v] = u

    def bellman_ford(self):
        print(self.nodes)
        for i in range(len(self.nodes) - 1):
            # self.print_current_state()
            for edge in self.edges:
                self.update(edge)
                # self.update(edge.reverse())#TODO the edges given are directed(as of now) so we need to go both ways on the edge
        # print("end")


class Project3Runner:
    # 37
    edges = [
        ["College Square", 300, "Prince Center"],
        ["College Square", 200, "Lewis Science Center"],
        ["Lewis Science Center", 150, "Computer Science"],
        ["Lewis Science Center", 250, "Speech Language Hearing"],
        ["Speech Language Hearing", 100, "Burdick"],
        ["Speech Language Hearing", 120, "Maintenance College"],
        ["Burdick", 30, "Computer Science"],
        ["Burdick", 80, "Torreyson Library"],
        ["Burdick", 200, "McALister Hall"],
        ["Burdick", 300, "Maintenance College"],
        ["Maintenance College", 150, "McALister Hall"],
        ["Maintenance College", 100, "Wingo"],
        ["Maintenance College", 150, "New Business Building"],
        ["Maintenance College", 160, "Oak Tree Apt."],
        ["Oak Tree Apt.", 30, "New Business Building"],
        ["Oak Tree Apt.", 40, "Brewer-Hegeman"],
        ["Brewer-Hegeman", 350, "Bear village Apt."],
        ["Brewer-Hegeman", 200, "Student Health Center"],
        ["Brewer-Hegeman", 20, "New Business Building"],
        ["New Business Building", 100, "Wingo"],
        ["New Business Building", 110, "Student Center"],
        ["Wingo", 50, "McALister Hall"],
        ["Wingo", 100, "Student Center"],
        ["Student Center", 100, "McALister Hall"],
        ["Student Center", 80, "Fine Art"],
        ["Student Center", 50, "Student Health Center"],
        ["Fine Art", 50, "Police Dept."],
        ["Fine Art", 90, "Old Main"],
        ["Fine Art", 180, "McALister Hall"],
        ["Police Dept.", 100, "Student Health Center"],
        ["Police Dept.", 200, "Old Main"],
        ["Police Dept.", 100, "Prince Center"],
        ["Old Main", 30, "Torreyson Library"],
        ["Old Main", 100, "McALister Hall"],
        ["Torreyson Library", 30, "Prince Center"],
        ["Torreyson Library", 40, "Computer Science"],
        ["Computer Science", 80, "Prince Center"],
        # Reverse of edges
        ["Prince Center", 300, "College Square"],
        ["Lewis Science Center", 200, "College Square"],
        ["Computer Science", 150, "Lewis Science Center"],
        ["Speech Language Hearing", 250, "Lewis Science Center"],
        ["Burdick", 100, "Speech Language Hearing"],
        ["Maintenance College", 120, "Speech Language Hearing"],
        ["Computer Science", 30, "Burdick"],
        ["Torreyson Library", 80, "Burdick"],
        ["McALister Hall", 200, "Burdick"],
        ["Maintenance College", 300, "Burdick"],
        ["McALister Hall", 150, "Maintenance College"],
        ["Wingo", 100, "Maintenance College"],
        ["New Business Building", 150, "Maintenance College"],
        ["Oak Tree Apt.", 160, "Maintenance College"],
        ["New Business Building", 30, "Oak Tree Apt."],
        ["Brewer-Hegeman", 40, "Oak Tree Apt."],
        ["Bear village Apt.", 350, "Brewer-Hegeman"],
        ["Student Health Center", 200, "Brewer-Hegeman"],
        ["New Business Building", 20, "Brewer-Hegeman"],
        ["Wingo", 100, "New Business Building"],
        ["Student Center", 110, "New Business Building"],
        ["McALister Hall", 50, "Wingo"],
        ["Student Center", 100, "Wingo"],
        ["McALister Hall", 100, "Student Center"],
        ["Fine Art", 80, "Student Center"],
        ["Student Health Center", 50, "Student Center"],
        ["Police Dept.", 50, "Fine Art"],
        ["Old Main", 90, "Fine Art"],
        ["McALister Hall", 180, "Fine Art"],
        ["Student Health Center", 100, "Police Dept."],
        ["Old Main", 200, "Police Dept."],
        ["Prince Center", 100, "Police Dept."],
        ["Torreyson Library", 30, "Old Main"],
        ["McALister Hall", 100, "Old Main"],
        ["Prince Center", 30, "Torreyson Library"],
        ["Computer Science", 40, "Torreyson Library"],
        ["Prince Center", 80, "Computer Science"]
    ]


    for edge in edges: #Used to reverse edges for edge array
        print('[\"',edge[2],'\", ', edge[1], ', \"',edge[0],'\"],',sep="")


    nodes = ["Computer Science", "College Square", "Lewis Science Center", "Prince Center",
             "Police Dept.", "Student Health Center", "Torreyson Library", "Old Main", "Fine Art",
             "Student Center", "Burdick", "McALister Hall", "Wingo", "New Business Building",
             "Brewer-Hegeman", "Bear village Apt.", "Speech Language Hearing",
             "Maintenance College", "Oak Tree Apt."]  # Starting node has to be first node in nodes array

    '''
    edges = [                 #Test data from HW
                ["S", 7, "A"],
                ["S", 6, "C"],
                ["S", 6, "E"],
                ["S", 5, "F"],
                ["A", 4, "B"],
                ["A", -2, "C"],
                ["B", -2, "G"],
                ["B", -4, "H"],
                ["C", 2, "D"],
                ["C", 1, "F"],
                ["E", -2, "F"],
                ["E", 3, "H"],
                ["F", 3, "D"],
                ["G", -1, "I"],
                ["H", 1, "G"],
                ["I", 1, "H"],
    ]
    nodes = ["S", "A", "B", "C", "D", "E", "F", "G", "H", "I"]
    '''

    bf = BellmanFord(edges, nodes, nodes[0])
    bf.bellman_ford()
    bf.print_current_state()


class PriorityQueue(object):
    def __init__(self, nodes):
        self.queue = nodes

    def make_queue(self):
        pass

    def delete_min(self, distances):
        min = node[0]
        for node in self.queue[1:]:
            if distances[node] < distances[min]:
                min = node
        self.queue.remove(min)  # TODO
        return min

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def decrease_key(self, v):
        pass
