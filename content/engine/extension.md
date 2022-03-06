
- FSM als eine Ausprägung eines Graphen, genaugenommen eines gerichteten Graphen.

- Aus der Graphentheorie: DFS, BFS Algorithm

- Repräsentation einer State Machine

- Unterschied DFA/MFA


Wenn wir kein "OR" und keine Quantifier wie +, * in unserem RegEx hätten, dann wäre es ein DFA. Der Zustand wäre deterministisch. Es gibt nur einen Zustandsübergang zwischen den States. Ein Character des Eingabetexts sorgt für eine State-Transition in einen anderen Zustand.

Da wir aber OR haben, quasi ein Sprung des RegEx, handelt es sich um einen NFA. Ebenso der Quantifier `*`, wir wissen nicht, wie lange wir uns in diesem Zustand befinden.

Kleenes theorem beweist, dass es für jeden RegEx auch einen entsprechenden finiten Automaten gibt.


