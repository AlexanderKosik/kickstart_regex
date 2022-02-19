#!/usr/bin/env python3


class States:
    LOCKED = 0
    UNLOCKED = 1


class Events:
    PUSH = 0
    COIN = 1

def ascii_to_number(char):
    return ord(char) - 97

class FSM:
    def __init__(self):
        self.states = []
        self.cs = 0

    def add_state(self, transition_char):
        state = [0] * 26
        state[ascii_to_number(transition_char)] = len(self.states) + 1
        self.states.append(state)

    def next_state(self, char):
        self.cs = self.states[self.cs][ascii_to_number(char)]


    def __str__(self):
        s = ""
        for row in zip(*self.states):
            s += " ".join(str(c) for c in row) + "\n"
        return s

    def compile(self, regex):
        self.states = []
        for char in regex:
            self.add_state(char)

    def match(self, input_str):
        self.cs = 0
        for c in input_str:
            self.next_state(c)
            if self.cs == 0:
                return False
        return self.cs == len(self.states)

