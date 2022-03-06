# Directed Graph implementation

class Digraph:
    @classmethod
    def from_file(cls, filename):
        f = open(filename)
        return cls(f)

    @classmethod
    def from_iterable(cls, iterable):
        """
        Use format as in Algorithms 4th edition:
        int: num vertices
        int: num edges
        int, int: v w for edge v -> w
        int, int: a b for edge a -> b
        ...
        """
        v = int(next(iterable))
        self = cls(v)
        self.v = v
        self.e = int(next(iterable))

        # create adjacency list
        self.adj = {v:[] for v in range(self.v)}

        for line in iterable:
            v, w = map(int, line.split(" "))
            self.add_edge(v, w)

        return self

    def __init__(self, vertex_number):
        self.v = vertex_number
        self.e = 0

        self.adj = {v:[] for v in range(self.v)}


    def add_edge(self, v: int, w: int):
        self.adj[v].append(w)

    
    def __str__(self):
        return str(self.adj)

# f = open("tinyDG.txt")
# g = Digraph.from_iterable(f)
# print(g)
