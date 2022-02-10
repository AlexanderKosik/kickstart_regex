[Overview](./overview.md) | [Back (Quantifiers)](./quantifier.md) | [Next (Anchors)](./anchors.md)

# Character classes
In the previous example of validating IP addresses, we used the dot meta character to match any kind of character.

What if we only want to match certain characters, like only vowels? Or only numbers?

For these kinds of use cases we can define character classes. A character class is defined with square brackets `[]`.

A character class matches on every element that is contained:

    - [abc] will match on a or b or c
    - [xyz] will match on x or y or z
    - [0123456789] will on 0, 1, ..., 9

Character classes are kind of their own mini-language within regular expressions. Several symbols within character classes have different meanings than outside character classes. This may confuse some beginners when learning and reading existing regular expressions written by other people. But this confusion comes mostly from the fact that this different usage of the symbols is not well known.

So how can we use these character classes?

```python
print(1, re.search(r"[Ff]atal", "Fatal error"))     # match or no match?
print(2, re.search(r"[Ff]atal", "fatal error"))     # match or no match?

# Let's combine the character class with quantifiers
print(3, re.search(r"[0123456789]{5}", "06081"))    # match or no match?
print(4, re.search(r"[0123456789]{7}", "07231"))    # match or no match?
```

So this is kind of neat. With this knowledge we can improve our IP address validator from the previous chapter.

## Exercise: Improved IP validator

With this new information we can improve our IP validator from the last chapter.

Write a RegEx that will match on `192.168.1.` plus 1 to 3 **numbers**. Characters other than numbers should not be allowed.  

```python
import re

def better_ip_validator(ip_address):
    # Replace ... with valid RegEx
    m = re.match(r"...", ip_address)
    return m is not None

assert better_ip_validator("192.168.1.1") is True
assert better_ip_validator("192.168.1.11") is True
assert better_ip_validator("192.168.1.111") is True
assert better_ip_validator("192.168.1.x") is False
assert better_ip_validator("192.168.1.xx") is False
assert better_ip_validator("192.168.1.xxx") is False
print("Good RegEx!")
```

This looks a lot better than before. But we still have some problems. As you might know, the range of an address segment only ranges from 0 to 255. So all of these examples are actually invalid IP addresses:

    - 192.168.1.256 # invalid address
    - 192.168.1.300 # invalid address
    - 192.168.1.999 # invalid address

But our regex validates everything that is a number. This is a problem. But don't worry - we have a solution for that and we will fix this later on :)

## Character classes simplified
What if we want to match all lowercase characters. It would not be feasible to create a character class like this: `[abcdefghjklmnopqrstuvwxyz]`. This is very tedious so there must be a better way!

And there is! The dash `-` between `a` and `z` defines a range. So it will match every character: `a`, `b`, `c`, ..., `z`.

Look at the examples below and try to predict if they will match or not:

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

As seen in these examples, we can combine these character classes with the already known quantifiers from the last chapter. The examples show the "exactly x times" `{x}` quantifier, but of course they will also work with other quantifiers like `?`, `+` or `*`.

So the ranges look useful. Why not use this to fix our problem with invalid IP addresses like `192.168.1.999` in the following manner:

```python
import re

def better_ip_validator(ip_address):
    # Replace ... with valid RegEx
    m = re.match(r"192\.168\.1\.[0-255]{1}", ip_address)
    return m is not None

assert better_ip_validator("192.168.1.255") is True     # cool, this works
assert better_ip_validator("192.168.1.0") is True       # cool, this also works
assert better_ip_validator("192.168.1.256") is False    # Ouch!
print("Good RegEx!")
```

Can you figure out why this does not work? (The solution is at the end of the chapter)

# Exercise 'Hexadecimal validator'
These new character classes seem very useful. Let's see them in action. We want to validate if a passed string is a valid hexadecimal string.

In this example we define a valid hexadecimal string as followed:

- Starts with `0x`
- Followed by one to **four** hex characters
- Valid hex characters are: `0123456789ABCDEF`
- Characters are case-sensitive

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
# our validate_hex will return True. Can you figure out why?
assert validate_hex("0x12345") is False, "invalid hex"
print("Good hex validator")
```

At the moment we cannot get the hex validator to work as specified. There is one small piece missing. At the moment we must be happy with an okayish hex validator ;)

## Including `-` in the character class
The dash `-` has a special meaning in character classes. With this, we can specify ranges. What if we want the dash to be a character to match?

In this special case, we must place the dash in the very beginning of the character class.

```python
import re

# dash and range 0-9 included
assert re.match(r"[-0-9]{10}", "1984-02-24") is not None
```

## Negating character classes
What if we want to match everything that is not a lowercase character `[a-z]`?

In character classes, we can use a `^` to negate the character class. Have a look at the following examples. Think for yourself whether they will match or not and verify your results.

```python
print(1, re.search(r"[^a-z]", "123"))       # matches everything that is no lowercase char
print(2, re.search(r"[^0-9]", "X"))         # matches everything that is no number
print(3, re.search(r"[^a-cx-z]{3}", "def")) # matches everything that is not abcxyz

print(4, re.search(r"[^a-cx-z]{3}", "abc")) # match or no match?
print(5, re.search(r"[^a-cx-z]{3}", "xyz")) # match or no match?
print(6, re.search(r"[^a-cx-z]{3}", "cde")) # match or no match?
print(7, re.search(r"[^a-cx-z]{3}", "ghi")) # match or no match?
```

One important aspect is that the negated character class must still match. If we look at a RegEx like this `r"[A-Z]{4}[^a-zA-Z]"` we match 4 uppercase characters followed by 1 character that is not a letter. But this last negated character class **still needs a character to match**.

## "Shortcut" for common character classes
Using character classes like [a-z] or [0-9] is very common when writing regular expressions. For that reason there are shortcuts for common character classes.

    \w    Word: [a-zA-Z0-9_]
    \W    Non-Word Character
    \d    Digit: [0-9]
    \D    Non-Digit
    \s    Whitespace: Space, Tab, Newline
    \S    Non-Whitespace


## Exercise: email revisited

Let's add some constraints to our email validation (still far from production ready):

- at least 1 arbitrary character (uppercase or lowercase, no number, no special chars)
- followed by an "`@`" symbol
- followed by at least 3 arbitrary characters
- followed by a dot "`.`"
- followed by at least 2 arbitrary characters (uppercase or lowercase, no number, no special chars)

```python
import re

def bad_email_validator(email):
    # Replace ... with valid RegEx
    m = re.match(r"...", email)
    return m is not None

assert bad_email_validator("peter@gmail.com") is True # valid
assert bad_email_validator("petergmail.com") is False # invalid
assert bad_email_validator("@xyz.com") is False # invalid
assert bad_email_validator("hugo@.com") is False # invalid
assert bad_email_validator("hugo@test.c0m") is False # invalid
print("Good RegEx!")
```

In the next chapter, we can solve our problem with the hex validator and 5 hex values. So stay tuned :)

[Overview](./overview.md) | [Back (Quantifiers)](./quantifier.md) | [Next (Anchors)](./anchors.md)

## Solutions

The character class `[0-255]` will actually be the same as this: `[01255]`. So it will match 0 or 1 or 2 or 5. The redundant 5 is ignored in this case.
