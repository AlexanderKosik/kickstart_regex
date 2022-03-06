# Implementation of RegEx Engine from book Algorithms 4th edition
from graph import dfs, digraph

class NFA:
    def __init__(self, regex):
        self.regex = regex
        self.m = len(self.regex)
        self.graph = digraph.Digraph(self.m + 1)

        # parse the regex and add edges to graph
        ops = []
        for i, char in enumerate(regex):
            lp = i
            if char == '(' or char == '|':
                ops.append(i)
            elif char == ')':
                or_ = ops.pop()

                if regex[or_] == '|':
                    lp = ops.pop()
                    self.graph.add_edge(lp, or_ + 1)
                    self.graph.add_edge(or_, i)
                elif regex[or_] == '(':
                    lp = or_

            # closure *
            if i < self.m -i and regex[i+1] == '*':
                self.graph.add_edge(lp, i+1)
                self.graph.add_edge(i+1, lp)
            if char == '(' or char == '*' or char == ')':
                self.graph.add_edge(i, i+1)



        

    def recognizes(self, txt):
        ddfs = dfs.DirectedDFS(self.graph, 0)
        pc = list(ddfs.all_marked())

        # compute all possible NFA states
        for i, _ in enumerate(txt):
            match = []
            for v in pc:
                if v == self.m:
                    continue
                if self.regex[i] == txt[i] or self.regex[i] == ".":
                    match.append(v+1)

            if not match:
                continue

            # multi source DFS
            ddfs = dfs.DirectedDFS(self.graph, *match)
            pc = list(ddfs.all_marked())

            if not pc:
                return False

        # check if we have reached accept state
        return any(v == self.m for v in pc)



regex = '(' + 'aa|bb' + ')'
nfa = NFA(regex)
print(nfa.graph)
txt = 'aa'
#print(nfa.recognizes(txt))
