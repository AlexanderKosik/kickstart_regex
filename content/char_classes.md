[Overview](./overview.md) | [Back (Quantifier)](./quantifier.md) | [Next (Anchors)](./anchors.md) 

# Character classes
With square brackets `[]` we can define `character classes`.

Character classes match on every element that is contained:

    - [abc] will match on a or b or c
    - [xyz] will match on x or y or z
    - [0123456789] will on 0, 1, ...9

Character classes are kind of a own mini-language within Regular Expressions. Several symbols within character classes have different meanings than outside character classes. This may confuse some beginners when reading Regular Expressions. But this confusing comes mostly from the fact, that this different usage of the symbols is not well known. 

So how can we use these character classes?

```python
print(1, re.search(r"[Ff]atal", "Fatal error"))     # match or no match?
print(2, re.search(r"[Ff]atal", "fatal error"))     # match or no match?

# Let's combine the character class with quanitifiers
print(3, re.search(r"[0123456789]{5}", "06081"))    # match or no match?
print(4, re.search(r"[0123456789]{7}", "07231"))    # match or no match?
```

## Character classes simplified
What if we want to match all lower case characters. It would not be feasible to create a character class like this: `[abcdefghjklmnopqrstuvwxyz]`. But this is very tidious so there must be a better way!

And there is. The dash `-` between `a` and `z` defines a range. So it will match every character: `a`, `b`, `c`, ..., `z`. 

Look at the examplpes below and think if they will match or not:

```python
print(1, re.search(r"[a-z]", "x"))                      # match or no match?
print(2, re.search(r"[a-z]", "X"))                      # match or no match?
print(3, re.search(r"[a-zA-Z]", "X"))                   # match or no match?

print(4, re.search(r"[a-z]", "7"))                      # match or no match?
print(5, re.search(r"[a-zA-Z]", "1"))                   # match or no match?

print(6, re.search(r"[0-9]{5}", "06081"))               # match or no match?
print(7, re.search(r"[0-9]{7}", "07231"))               # match or no match?
print(8, re.search(r"[0-9a-zA-Z]{10}", "el1t3h4x0r"))   # match or no match?
```

As we see we can combine these character classes with the already known quantifiers from the last chapter. The examples show the "exactly x times" `{x}` quantifier. Of course they will also work with other quantifiers like `?`, `+` or `*`. 

# Exercise 'Hexadecimal validator'
These new character classes are very useful. Let's see them in action. We want to validate if a passed string is a valid hexadecimal string.

In this example we define a valid hexadecimal string as followed:

- Starts with `0x`
- Followed by one to four hex character 
- Valid hex characters are: `0123456789ABCDEF`
- Characters are case sensitive

```python
import re

def validate_hex(hex_string) -> bool:
    # replace ... with valid regex
    m = re.match(r"...", hex_string)
    return m is not None

assert validate_hex("0x0") is True, "valid hex"
assert validate_hex("0xFF") is True, "valid hex"
assert validate_hex("0xABFF") is True, "valid hex"
assert validate_hex("0x1234") is True, "valid hex"

assert validate_hex("0x") is False, "invalid hex"
assert validate_hex("0xG") is False, "invalid hex"
assert validate_hex("0xabff") is False, "valid hex"
assert validate_hex("0XABFF") is False, "valid hex"
assert validate_hex("AAFF") is False, "invalid hex"
assert validate_hex("xAAFF") is False, "invalid hex"
assert validate_hex("0") is False, "invalid hex"
print("okayish hex validator")

# we cannot get this one to pass yet
assert validate_hex("0x12345") is False, "invalid hex"
print("Good hex validator")
```

At the moment we cannot get the hex validator to work as specified. There is one little peace missing. At the moment we must be happy with an okayish hex validator ;)

### Including `-` in the character class
The dash `-` has a special meaning in character classes. With this we specifiy ranges. What if we want the dash to be a character to match?

In this special case we must place the dash in the very beginning of the character class.
```python
import re

# dash and range 0-9 included
assert re.match(r"[-0-9]{10}", "1984-02-24") is not None
```

## Negating character classes
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

One important aspect is, that the negated character class must still match. If we look at a regex like this `r"[A-Z]{4}[^a-zA-Z]"` we match 4 uppercase characters followed by 1 character that is no letter. But this last negated character class **still needs a character to match**. 

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