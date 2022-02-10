[Overview](./overview.md) | [Back (Character classes)](./char_classes.md) | [Next (Groups)](./groups.md)

# Anchors

In this chapter we will learn about anchors. With anchors we can match positions. For example if we want to match specific characters only at the beginning or end of the line.

The following anchors exist:

    Be aware that a position is not a character
        ^    Matches on beginning of the line
        $    Matches on the end of a line
        \b   Matches on a word boundary (beginning or end of a word)
             Matches, without consuming any characters, immediately between a character
             matched by \w and a character not matched by \w (in either order)

So here we have the caret `^` again. If you remember from the previous chapter we had the `^` specified as a negated character class.

This is why the character classes can be seen as a separate mini-language within RegEx. **Within** a character class a `^` means **negating**, **outside** of character classes it means `beginning of the line`.

So don't confuse these two different uses of the caret `^`. When you encounter a `^`, make sure that you are clear about the context in which you are using it and therefore the meaning of the `^` in that given context.

## Examples with anchors
```python
import re

s = "Error on columbia01. A Fatal Error occurred!"
print(re.findall(r"^Error", s))

s = "Subject: fire. Dear Sir/Madam, I am writing to inform you of a fire"
print(re.findall(r"fire$", s))

s = "A38, 42, 36, 48"
print("With word boundaries:", re.findall(r"\b[0-9]{2}\b", s))

# compare the result of the above print statement with the following findall
print("Without word boundaries:", re.findall(r"[0-9]{2}", s))
```

By using word boundaries you can avoid getting matches within other words, as seen in the last example.

## Exercise "valid filenames" revisited

Let's attempt the valid filenames problem in a more real-world context. In the Windows OS the following symbols may not be used in a filename: `\/:*?"<>|`

![Windows valid filenames](ressources/filename.png "Windows valid filename")

This means our restrictions are as follows:

- at least 1 arbitrary character except for  `\/:*?"<>|`
- followed by a dot (`"."`)
- followed by exactly 3 arbitrary characters, but not `\/:*?"<>|`

```python
# set this to True, if you would like to have the actual match printed
DEBUG = False

def valid_filename(filename):
    # insert regex here
    m = re.search(r'...', filename)

    if DEBUG:
        if m:
            print("The actual match is:", m.group())
        else:
            print("The actual match is: None")

    return m is not None

assert valid_filename("test.txt") is True
assert valid_filename("1.txt") is True
assert valid_filename(".txt") is False
assert valid_filename("test") is False
assert valid_filename("test.tt") is False
assert valid_filename("test.text") is False
assert valid_filename("te:st.txt") is False
assert valid_filename("te*st.txt") is False
assert valid_filename("test.t?t") is False
assert valid_filename("my-test-file.txt") is True
print("Good RegEx")
```

*Attention: The example above uses search, so you are forced to use anchors*

## Exercise "is integer"

Write a function with a regular expression which evaluates whether a given string is an integer.

    is_integer(string) -> bool
    The function should evaluate whether a given string is a valid integer.

    We define valid integers as this:

    Consists of 1 or more digits
    May optionally begin with -
    Does not contain any other non-digit characters.

```python
import re

# set this to True if you would like to have the actual match printed
DEBUG = False

def is_integer(string):
    # Replace ... with regex
    m = re.search(r"...", string)

    if DEBUG:
        if m:
            print("The actual match is:", m.group())
        else:
            print("The actual match is: None")
    return m is not None

assert is_integer("42") is True
assert is_integer("-5000") is True
assert is_integer("-") is False
assert is_integer(" 42") is False
assert is_integer("0.0") is False
assert is_integer("+999") is False
assert is_integer("--500") is False
print("Good RegEx")
```
*Attention: The example above uses search, so you are forced to use anchors*

We finish this chapter with a little smile.

![Problems](ressources/perl_problems.png "Perl problems")

[Overview](./overview.md) | [Back (Character classes)](./char_classes.md) | [Next (Groups)](./groups.md)

<!-- Solution valid filenames:  r'^[^\\/*:?"<>|]+\.[^\\/*:?"<>|]{3}$' -->
