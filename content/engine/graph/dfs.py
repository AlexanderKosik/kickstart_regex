class DirectedDFS:
    def __init__(self, graph, destination):
        self.marked = [False] * graph.v
        self.dfs(graph, destination)
        print("Route to destination:")
        print(*[str(v) for v in range(graph.v) if self.marked[v]])

    def dfs(self, graph, v):
        self.marked[v] = True
        for w in graph.adj[v]:
            if not self.marked[w]:
                self.dfs(graph, w)


