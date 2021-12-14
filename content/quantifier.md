[Overview](./overview.md) | [Back (Meta-Characters)](./meta.md) | [Next (Character classes)](./char_classes.md) 

# Quantifiers

With *quantifiers* we can specify how often a (Meta-)Character will be matched. 

The following quantifiers are available:
```
    *        0..x
    +        1..x
    ?        0..1
    {3}      exactly 3 
    {42}     exactly 42
    {3,}     3..x
    {10,20}  10..20
```

A quantifier must be places behind the character to match.

## Examples
### `*` quantifier
```python
# * matches 0..x

print(1, re.search(r"abc.*", "abc"))            # matched abc
print(2, re.search(r"abc.*", "abcd"))           # matched abcd
print(3, re.search(r"abc.*", "abcdefghijklmz")) # matched abcdefghijklmz
```

Try to figure out if the following statements are a match, or no match. You can test your results afterwards

```python
# {3} matches exactly 3 times
# {3, } matches 3..x times

print(4, re.search(r"a.{3}z", "abz"))           # Match or no match?
print(5, re.search(r"a.{3,}z", "abcdz"))        
print(6, re.search(r"a.{3,}z", "abcdedfgz"))    
```

### `+` and `?` quantifier
```python
# + matches 1..x times

print(7, re.search(r"a.+z", "abz"))
print(8, re.search(r"a.+z", "az"))
```

```python
# ? matches 0..1 times

print(9, re.search("a.?z", "abz"))
print(10, re.search("a.?z", "az"))
print(11, re.search("a.?z", "abcz"))
```

## Exercise "Valid Filenames"
Let's do an exercise. 

We want to validate file names. In our case valid file names contain:

- at least 1 arbitrary character
- followed by a dot "`.`"
- followed by at least 3 arbitrary characters

If you are using Python copy the following code in an interactive session:
```python
import re
# Validate file names

def valid_filename(filename):
    # Replace ... with valid RegEx
    m = re.search(r"...", filename)
    return m is not None

assert valid_filename("test.txt") is True
assert valid_filename(".txt") is False
assert valid_filename("test") is False
assert valid_filename("test.tt") is False
assert valid_filename("test.text") is True
print("Good RegEx!")
```

## Exercise "Valid emails"
In this simplified example we want to validate emails. In our example a valid email is definied as followed:

- at least 1 arbitrary character
- followed by an "`@`" symbol
- followed by at least 3 arbitrary characters
- followed by a dot "`.`"
- followed by at least 2 arbitrary characters

*Please be aware that validating email is a lot more complex in real world. This is just a simplfied version. So do not use this in production code! ;)* 

```python
import re

def bad_email_validator(email):
    # Replace ... with valid RegEx
    m = re.search(r"...", email)
    return m is not None

assert bad_email_validator("peter@gmail.com") is True       # valid
assert bad_email_validator("petergmail.com") is False       # invalid
assert bad_email_validator("@xyz.com") is False             # invalid
assert bad_email_validator("hugo@.com") is False            # invalid
print("Good RegEx!")
```

![Save the world](ressources/re1.png "Save the world")

[Overview](./overview.md) | [Back (Meta-Characters)](./meta.md) | [Next (Character classes)](./char_classes.md) 