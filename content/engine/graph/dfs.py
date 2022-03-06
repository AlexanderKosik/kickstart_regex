class DirectedDFS:
    def __init__(self, graph, *sources, debug=False):
        self.marked = [False] * graph.v
        for source in sources:
            self.dfs(graph, source)
        if debug:
            print("Reachable from source(s)", *sources)
            print(*[str(v) for v in range(graph.v) if self.marked[v]])

    def dfs(self, graph, v):
        self.marked[v] = True
        for w in graph.adj[v]:
            if not self.marked[w]:
                self.dfs(graph, w)

    def all_marked(self):
        return [i for i in range(len(self.marked)) if self.marked[i]]


