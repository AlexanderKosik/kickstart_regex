class DirectedDFS:
    def __init__(self, graph, source):
        self.marked = [False] * graph.v
        self.dfs(graph, source)
        print("Reachable from source", source)
        print(*[str(v) for v in range(graph.v) if self.marked[v]])

    def dfs(self, graph, v):
        self.marked[v] = True
        for w in graph.adj[v]:
            if not self.marked[w]:
                self.dfs(graph, w)

    def all_marked(self):
        return [i for i in range(len(self.marked)) if self.marked[i]]


