#!/usr/bin/env python3

class States:
    LOCKED = 0
    UNLOCKED = 1


class Events:
    PUSH = 0
    COIN = 1

def print_state(state):
    """
    prints the current state
    """ 
    match state:
        case States.LOCKED:
            print("locked")
        case States.UNLOCKED:
            print("unlocked")
        case _:
            print("unknown state")


def next_state(state, event):
    match state, event:
        case States.LOCKED, Events.COIN:
            return States.UNLOCKED
        case States.LOCKED, Events.PUSH:
            return States.LOCKED
        case States.UNLOCKED, Events.COIN:
            return States.UNLOCKED
        case States.UNLOCKED, Events.PUSH:
            return States.LOCKED

state = States.LOCKED
while True:
    cmd = input("> ")
    if cmd == "coin":
        state = next_state(state, Events.COIN)
        print_state(state)
    if cmd == "push":
        state = next_state(state, Events.PUSH)
        print_state(state)
    if cmd == "quit":
        import sys
        sys.exit(0)
