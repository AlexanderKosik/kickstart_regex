[Overview](./overview.md) | [Back (Character classes)](./char_classes.md) | [Next (Groups)](./groups.md) 

# Anchors

In this chapter we will learn about anchors. With anchors we can match positions. For example if we want to match specific characters only on the beginning of the line or the end of the line.

The following anchors exist:

    Be aware that a position is no character
        ^    Matches on beginning of the line
        $    Matches on the end of a line
        \b   Matches on a word boundary (beginning or end of a word)
             Matches, without consuming any characters, immediately between a character 
             matched by \w and a character not matched by \w (in either order)

So here we have the circumflex `^` again. If you remember from the previous chapter we had the `^` specified as a negated character class. 

This is why the character classes can be seen as a separate mini-language within RegEx. **Within** a character class a `^` means **negating**, **outside** of character classes it means `beginning of the line`.

So don't be confused with that. When you encounter an `^` make sure in which context you are and depending on that context the `^` has different meanings.

## Examples with anchors
```python
import re

s = "Error on columbia01. A Fatal Error occured!"
print(re.findall(r"^Error", s))

s = "Subject: fire. Dear Sir/Madam, I am writing to inform you of a fire"
print(re.findall(r"fire$", s))

s = "A38, 42, 36, 48"
print("With word boundaries:", re.findall(r"\b[0-9]{2}\b", s))

# compare the result of the upper print with the following findall
print("Without word boundaries:", re.findall(r"[0-9]{2}", s))
```

By using word boundaries you can avoid getting hits within other words, as seen in the last example. 

## Exercise "valid file names" revisited

Let's take the valid file names more seriously. In the Windows OS the following symbols may no be used in a file name: `\/:*?"<>|`

![Windows valid filenames](ressources/filename.png "Windows valid filename")

This means our restrictions are as followed:

- at least 1 arbitrary character except of  `\/:*?"<>|`
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

We write a function with a regular expression which evaluates, if a given string is an integer. 

    is_integer(string) -> bool
    The function should evaluate if given string is a valid integer. 

    We define valid integers as this:

    Consists of 1 or more digits
    May optionally begin with -
    Does not contain any other non-digit characters.

```python
import re

# set this to True, if you would like to have the actual match printed
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
