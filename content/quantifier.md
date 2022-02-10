[Overview](./overview.md) | [Back (Meta-Characters)](./meta.md) | [Next (Character classes)](./char_classes.md)

# Quantifiers

In the last exercise, we wrote a filename validator which might look like this: `r"........\...."`. We had 8 arbitrary characters followed by a literal dot followed by 3 arbitrary characters.

This is kind of hard to read. So there must be a better way to specify how many times we want a character or meta character to match.

With *quantifiers* we can specify exactly that. We can tell the RegEx how often a (Meta-)Character must match.

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

A quantifier must be placed after the thing we want to quantify. In our previous exercise, we could simplify the RegEx like this:

```python
import re

def simple_validator(filename):
    # Replace ... with valid RegEx
    m = re.search(r".{8}\..{3}", filename)
    return m is not None
```

Match an arbitrary character exactly 8 times, then match a dot and then match an arbitrary character exactly 3 times.

Great! That's cool! Our RegEx now looks much simpler.

Of course we can also use the quantifier on literal characters. If we want to match the letter `z` exactly 3 times, we can do this as follows:

```python
import re
print(re.search(r"a{3}", "aaa"))    # match
print(re.search(r"a{5}", "aaa"))    # None
```

Let's have a closer look at some other quantifiers.

## The `?` quantifier
For a character marked with the `?` quantifier to be matched, it must appear exactly once or not at all. So it marks something as *optional*.

How can we use this?

Let's say we have a log file with messages and IP addresses. We now want to extract every message from IP addresses starting with `192.168.0.xxx`

We know that we need at least 1 digit in the last segment of the IP address, but it may also be 2 or 3. How can we do this? The `?` is very handy in this case. Have a look at this implementation:

```python
# ? matches 0..1 times

log_content = [
    "192.168.0.1      Error transmitting 3 Bytes",
    "192.168.0.10     Error transmitting 3 Bytes",
    "192.168.1.42     Error transmitting 2 Bytes",
    "192.168.1.52     Error transmitting 2 Bytes",
    "192.168.0.100    Error transmitting 8 Bytes",
    "172.148.1.1      Error transmitting 2 Bytes",
    "192.168.0.1      Error transmitting 1 Bytes",
]

# RegEx for matching 192.168.0.xxx with at least 1 digit in the last segment
pattern = r"192\.168\.0\...?.?"

# iterate of our log_content and print the row if pattern matches
for row in log_content:
    if re.match(pattern, row):
        print("Error detected:", row)
```

In the example above, we could extract the IP addresses also manually. Our test content has only 7 entries. But in a real world scenario, the log file may have more than 10,000 lines. A manual extraction would be very tedious to say the least!

Look at the next example and try to predict whether the following patterns will match the IP addresses. Write your expected result down and try them out afterwards in an interactive session and compare with your expected results.

```python
print("Example 1", re.match(r"192\.168\.1\..?", "192.168.1.7"))      # Match or no match?
print("Example 2", re.match(r"172\.148\.1\...4", "172.148.1.4"))     # Match or no match?
print("Example 3", re.match(r"172\.148\.1\..?.?4", "172.148.1.4"))   # Match or no match?
print("Example 4", re.match(r"172\.148\.1\..?.?4", "172.148.1.14"))  # Match or no match?
print("Example 5", re.match(r"172\.148\.1\..?.?4", "172.148.1.104")) # Match or no match?

print("Hard Example", re.match(r"192\.168\.1\..?", "192.168.1.10"))     # Match or no match?
```

How many examples did you correctly guess? Whether you got them all correct or none, the important point is that you tried. You must commit mental effort to learn, so stay motivated :)

If you have tried the examples in an interactive prompt you will see that the last RegEx will match. This is actually a very dangerous RegEx and, in most cases, an invalid match.

First of all, it will also match an invalid IP address like `192.168.1.` which itself is kind of odd. But it also prints a "wrong" match by only printing `192.168.1.1` which may not be the IP address we are looking for.

We will learn better ways to improve our RegEx, both readability *and* functionality wise. But let's look at the `*` quantifier first.

## `*` quantifier
The `*` quantifier specifies that a character may have any number of hits. Any number means **zero** hits, as well as 1,000,000 hits, as well as 40 hits, as well as ... I think you get it.

```python
# * matches 0..x

print(1, re.match(r"192.168.*", "192.168.1.42"))          # match
print(2, re.match(r"192.168.1.10.*", "192.168.1.10"))     # match
print(3, re.match(r"192.168.1.10.*", "192.168.1.100"))    # match
print(4, re.match(r"192.168.1..*", "192.168.1.xxx"))      # match
```

The `*` quantifier is **greedy**. This means it tries to match as many characters as possible. We have a look at an example to describe what this means exactly.

Let's say we want to match opening HTML-Tags `<` starting with an `h`. We do not want the closing ones, so we would only expect: `<html>, <head>, <h1> and <h3>`.

As we know RegEx, it sounds like a great idea to use our new tool in the toolkit.

```python
# This is our example html homepage
html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Example Page</title>
    </head>
    <body>
        <h1>Hello World</h1>
        <h3>This is some smaller heading</h3>
    </body>
</html>
"""

# we now want to find every occurrence of <html-tags> starting with a lower case `h`.
# Our pattern might look like this:
pattern = r"<h.*>"

# so we have a literal `<` followed by a literal `h`
# followed by any number of arbitrary characters (to match html, head, h1, ...)
# and a literal `>`

# we use findall to find all results
# have a look at the results. Is this what we wanted?!
print(re.findall(pattern, html))
```

The result might look something like this:
```python
['<head>', '<h1>Hello World</h1>', '<h3>This is some smaller heading</h3>']
```

So instead of printing just the opening tag, it prints the opening tag, the content (if present) and the closing tag!

The `*` quantifier wants to match **as much as possible** (as said - it's greedy) so it also matches the first occurrence of our closing tag as long as there is another `>` following.

So be very careful if find yourself using a `.*` within a RegEx. In most cases, the behaviour is not what you want!

*Pro tip: We can change the greediness of the `*` quantifier by using `*?`. But that is more of an advanced feature.*

## `+` quantifier
The `+` quantifier specifies that a character may have one to any number of hits. So we must have **at least** 1 hit.

Look at these examples. Will they match?
```python
# + matches 1..x times

print(7, re.search(r"a.+z", "abz"))     # Match or no match?
print(8, re.search(r"a.+z", "az"))      # Match or no match?
```

Try to figure out if the following statements are a match, or no match. You can test your results afterwards.

## Fix number of matches

As seen in the beginning of the chapter, we can specify the quantity of (meta-)characters with an exact number or a range.

```python
# {3} matches exactly 3 times
# {3, } matches 3..x times
# {3, 5} matches 3, 4 or 5 times, but not more

print(4, re.search(r"a.{3}z", "abz"))           # Match or no match?
print(5, re.search(r"a.{3,}z", "abcdz"))        # Match or no match?
print(6, re.search(r"a.{3,}z", "abcdedfgz"))    # Match or no match?
```

## Exercise IP address
With this exact specification, we can improve the matching of IP addresses. Can you figure out how?

The solution is at the end of the file.

## Exercise valid filename
Let's revisit the valid filename exercise again.

A valid filename is now specified as this:

- at least 1 arbitrary character
- followed by a dot "`.`"
- followed by at least 3 arbitrary characters

```python
import re
# Validate file names

def valid_filename(filename):
    # Replace ... with valid RegEx
    m = re.match(r"...", filename)
    return m is not None

assert valid_filename("test.txt") is True
assert valid_filename(".txt") is False
assert valid_filename("test") is False
assert valid_filename("test.tt") is False
assert valid_filename("test.text") is True
print("Good RegEx!")
```

## Exercise "Valid emails"
In this simplified example, we want to validate emails. In our example, a valid email is defined as follows:

- at least 1 arbitrary character
- followed by an "`@`" symbol
- followed by at least 3 arbitrary characters
- followed by a dot "`.`"
- followed by at least 2 arbitrary characters

*Please be aware that validating an email is a lot more complex in the real world. This is just a simplified version. So do not use this validator in production code! ;)*

```python
import re

def bad_email_validator(email):
    # Replace ... with valid RegEx
    m = re.match(r"...", email)
    return m is not None

assert bad_email_validator("peter@gmail.com") is True       # valid
assert bad_email_validator("petergmail.com") is False       # invalid
assert bad_email_validator("@xyz.com") is False             # invalid
assert bad_email_validator("hugo@.com") is False            # invalid
print("Good RegEx!")
```

You are well on the way to becoming a RegEx Hero!

![Save the world](ressources/re1.png "Save the world")

We finish this chapter by giving an overview of our known quantifiers.

| Quantifier   | Min           |  Max          | Meaning           |
|:------------:|:-------------:|:-------------:|-------------------|
| `?`          |  none         | 1             | *one optional*  |
| `*`          |    none       |   no limit    | *any amount okay* |
| `+`          |        1      |    no limit   | *at least one*|
| `{x}`        |        x      |    x          | *exactly x times*|
| `{x,y}`      |        x      |    y          | *between x and y times*|

*Hint: Pay attention that there is no space after the `,` in `{x,y}`. So a quantifier like this will **not** work: `{3, 10}`.*


## Problems in the IP address validation

Our IP address validation will currently match any last 3 characters. So it will also match something like this:

```python
# match 1-3 arbitrary characters

regex = r"192\.168\.1\..{1,3}"
print("Matches 1-3", re.match(regex, "192.168.1.7xx"))
print("Matches 1-3", re.match(regex, "192.168.1.17x"))
print("Matches 1-3", re.match(regex, "192.168.1.xxx"))
```

This is definitely not what we want. Can we fix this? Sure, we can! We will see how in the next chapter :)

[Overview](./overview.md) | [Back (Meta-Characters)](./meta.md) | [Next (Character classes)](./char_classes.md)

## Solutions

Match IP address starting with `192.168.1.`

```python
# match 1-3 arbitrary characters

regex = r"192\.168\.1\..{1,3}"
print("Matches 1-3", re.match(regex, "192.168.1.7"))
print("Matches 1-3", re.match(regex, "192.168.1.17"))
print("Matches 1-3", re.match(regex, "192.168.1.117"))
```
