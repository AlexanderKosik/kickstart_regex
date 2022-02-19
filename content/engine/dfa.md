[Back](./engine.md) | [Next](./dfa.md)

# Building a DFA machine
To build a DFA RegEx engine we need to implement a finite state machine. 

A finite state machine consists of **states** and **events**. With events we can transmit from one state to another (or also stay in the same state). But we can only be at one state at any given time.

Let's have a look a the example from the wikipedia page of finite state machines. 

# Turnstile as a state machine
If we look at as turnstile as a state machine it has two states: it can be *locked* and no one can pass it, or it can be *unlocked* and let exactly one person through. 

![Turnstile](images/turnstile.jpg "Turnstile")

To start a transition from state *locked* to *unlocked* we need an event to occure: this event is inserting a coin. Once we inserted a coin we can get through the turnstile by pushing and therfore implicitly changing its state from *unlocked* to *locked*. 

Drawn as a state machine the descibed behaviour looks like this:
![turnstile state machine](images/state_machine_turnstile.png "Turnstile State Machine")

## Implementing a state machine in `python`

We now look at multiple implementations of a state machine in python. 

## A regular expression as a Finite State Machine
