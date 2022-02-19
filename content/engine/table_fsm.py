#!/usr/bin/env python3


def ascii_to_number(char):
    return ord(char) - 97

class FSM:
    def __init__(self):
        self.states = []
        self.cs = 0

    def add_state(self, *tcs):
        state = [0] * 26
        if ... in tcs:
            for a in range(ascii_to_number(tcs[0]), ascii_to_number(tcs[-1])):
                state[a] = len(self.states) + 1
        else:
            for a in tcs:
                state[ascii_to_number(a)] = len(self.states) +1
        self.states.append(state)

    def next_state(self, char):
        self.cs = self.states[self.cs][ascii_to_number(char)]


    def compile(self, regex):
        self.states = []
        iter_ = iter(regex)
        for char in iter_:
            match char:
                case '.':
                    self.add_state('a', ..., 'z')
                case '[':
                    try:
                        # collect every character within []
                        valid = []

                        while char := next(iter_):
                            if char == ']':
                                break
                            valid.append(char)

                        self.add_state(*valid)
                    except StopIteration:
                        print("Invalid regex: ] expected")
                        return 

                case _:
                    self.add_state(char)

    def match(self, input_str):
        self.cs = 0
        for c in input_str:
            self.next_state(c)
            if self.cs == 0:
                return False
        return self.cs == len(self.states)

    def __str__(self):
        s = ""
        for row in zip(*self.states):
            s += " ".join(str(c) for c in row) + "\n"
        return s
    
    __repr__ = __str__
