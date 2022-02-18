# Creation of a RegEx Engine

In this chapter we build a RegEx engine from scratch. There are multiple ways of doing this and this implementation is far from production ready. See this chapter as a possibility to learn, how a RegEx engine might work in principal. 

## What is the RegEx engine?
If we use a method from the RegEx module like `re.match(r"^\d\d:\d\d", "12:55")` this will be processed by a RegEx engine which 'understands' all the specific meta characters, quantifiers etc. (let's call these things **units**) explained in the RegEx course. This unterstanding of these units typically contains two steps: first the transformation of the RegEx into a machine friendly syntax and the execution of this as a second step. 

## The simplest of all RegEx engines
Let's start by implementing the simplest of all RegEx engines which can only understand string literals as units. No character classes, no special characters, nothing. 

How can we implement this?

First we create the commonly used functions of the re module: `match` and `search`

```python
def match(regex, string):
    """
    returns a match object if:
        - the passed regex matches from the beginning of the passed string
    or None otherwise
    """
    pass

def search(regex, string):
    """
    returns a match object if:
        - the passed regex is found anywhere in the passed string
    or None otherwise
    """
    pass
```