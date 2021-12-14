[Overview](./overview.md) | [Back (Quantifier)](./quantifier.md) | [Next (Anchors)](./anchors.md) 

# Character classes
With square brackets `[]` we can define `character classes`.

Character classes match on every element that is contained:

    - [abc] will match on a or b or c
    - [xyz] will match on x or y or z
    - [0123456789] will on 0, 1, ...9

How can we use these character classes?

```python
print(1, re.search(r"[Ff]atal", "Fatal error"))     # match or no match?
print(2, re.search(r"[Ff]atal", "fatal error"))     # match or no match?

# Let's combine the character class with quanitifiers
print(3, re.search(r"[0123456789]{5}", "06081"))    # match or no match?
print(4, re.search(r"[0123456789]{7}", "07231"))    # match or no match?
```

## Character classes simplified
What if we want to match all lower case characters. It would not be feasible to create a character class like this: `[abcdef....xyz]`. There must be a better way!

And there is. We can do something like this:

```python
print(1, re.search(r"[a-z]", "x"))                      # match or no match?
print(2, re.search(r"[a-z]", "X"))                      # match or no match?
print(3, re.search(r"[a-zA-Z]", "X"))                   # match or no match?

print(4, re.search(r"[0-9]{5}", "06081"))               # match or no match?
print(5, re.search(r"[0-9]{7}", "07231"))               # match or no match?
print(6, re.search(r"[0-9a-zA-Z]{10}", "el1t3h4x0r"))   # match or no match?
```
## Negate character classes
What if we want to match everything that is no lower case character `[a-z]`? 

In character classes we can use a `^` to negate the character class. Have a look at the following examples. Think for yourself if they will match or not and verify your results.

```python
print(1, re.search(r"[^a-z]", "123"))       # matches everything that is no lower case char
print(2, re.search(r"[^0-9]", "X"))         # matches everything that is no number
print(3, re.search(r"[^a-cx-z]{3}", "def")) # matches everything that is not abcxyz 

print(4, re.search(r"[^a-cx-z]{3}", "abc")) # match or no match?
print(5, re.search(r"[^a-cx-z]{3}", "xyz")) # match or no match?
print(6, re.search(r"[^a-cx-z]{3}", "cde")) # match or no match?
print(7, re.search(r"[^a-cx-z]{3}", "ghi")) # match or no match?
```

## "Shortcut" for common character classes
Using character classes like [a-z] or [0-9] is very common when writing Regular Expressions. For that reason there are shortcuts for common character classes. 

    \w    Word: [a-zA-Z0-9_]
    \W    Non Word Character
    \d    Digit: [0-9]
    \D    Non Digit
    \s    Whitespace: Space, Tab, Newline
    \S    Non Whitespace


## Exercise: email revisited

We add some constraints to our email validation (still far from production ready):

- at least 1 arbitrary character (upper or lowercase)
- followed by an "`@`" symbol
- followed by at least 3 arbitrary characters
- followed by a dot "`.`"
- followed by at least 2 arbitrary characters (but no numbers)

```python
import re

def bad_email_validator(email):
    # Replace ... with valid RegEx
    m = re.search(r"...", email)
    return m is not None

assert bad_email_validator("peter@gmail.com") is True # valid
assert bad_email_validator("petergmail.com") is False # invalid
assert bad_email_validator("@xyz.com") is False # invalid
assert bad_email_validator("hugo@.com") is False # invalid
assert bad_email_validator("hugo@test.c0m") is False # invalid
print("Good RegEx!")
```

[Overview](./overview.md) | [Back (Quantifier)](./quantifier.md) | [Next (Anchors)](./anchors.md) 