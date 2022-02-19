#!/usr/bin/env python3

# states
LOCKED   = 0
UNLOCKED = 1

# events
PUSH = 0
COIN = 1

def print_state(state):
    """
    prints the current state
    """ 
    if state == LOCKED:
        print("locked")
    if state == UNLOCKED:
        print("unlocked")

def next_state(state, event):
    if state == LOCKED:
        if event == PUSH:
            return LOCKED
        if event == COIN:
            return UNLOCKED

    if state == UNLOCKED:
        if event == PUSH:
            return LOCKED
        if event == COIN:
            return UNLOCKED


state = LOCKED
while True:
    cmd = input("> ")
    if cmd == "coin":
        state = next_state(state, COIN)
        print_state(state)
    if cmd == "push":
        state = next_state(state, PUSH)
        print_state(state)
    if cmd == "quit":
        import sys
        sys.exit(0)


