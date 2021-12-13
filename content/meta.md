[Overview](./overview.md) | [Back (Introduction)](./introduction.md) | [Next (Quantifier)](./quantifier.md) 

# Meta Characters

Python has a builtin module for Regular Expressions: `module re`. 

```python
# let's import python regular expression module
import re
help(re.search)

# will deliver this output:
# Help on function search in module re:
# 
# search(pattern, string, flags=0)
#    Scan through string looking for a match to the pattern, returning
#    a Match object, or None if no match was found.

```

Let's try the search method:

```python
import re

# search(pattern, string, flags=0)
m = re.search(r"Fatal error", "Successful login to bender007")
print(m)    # None

m = re.search(r"error", "Random errormessage just to annoy you.")
print(m)    # <re.Match object; span=(7, 12), match='error'>
```

## Using string prefix "`r`"
When using the Python Programming language we have special string prefix available. By using the string prefix `r` we create a `raw string`. 

Raw strings to not intepret escaped chars like `\n`. And at least for RegEx this is what we need so it is highly recommended to use these raw strings in Python for RegEx. 

```python
# Create a raw string by using prefix 'r'
# \n is an 'escaped char' and will result in a new line
print("Row\nRow2\n")
print(r"Everything \n in a row\n")
```
Make sure that you always use raw strings when using RegEx in Python. This will save a lot of trouble.

## Another Example
```python
m = re.search(r"100€", "The price is 100€")
print(m)    # <re.Match object; span=(18, 22), match='100€'>

m = re.search(r"100€", "The price is $100")
print(m)    # None
```

We can implement this without RegEx quite easily. 
```python
# Without using RegEx
b_euro = r"100€" in "The price is 100€"
b_dollar = r"100€" in "The price is $100"

print(b_euro, b_dollar)
```
So what's the matter with RegEx?!

## The power of Meta Characters
Most characters match exactly on itself. The RegEx `r"test"` will match exactly on the string `test`. But there are exceptions. These exceptions are called `meta characters`. 

`Meta characters: . ^ $ * + ? { } [ ] \ | ( )`

### Meta Characeter . (dot)
The meta character `.` matches on any character

Let's have a look what the meta character `.` will match in these cases:
```python
import re
print(re.search(r"gr.y", "grey"))   # <re.Match object; span=(0, 4), match='grey'> 
print(re.search(r"gr.y", "gray"))   # <re.Match object; span=(0, 4), match='gray'>
print(re.search(r"gr.y", "gr7y"))   # <re.Match object; span=(0, 4), match='gr7y'>
print(re.search(r"gr.y", "great"))  # None
print(re.search(r"gr.y", "gr.y"))   # <re.Match object; span=(0, 4), match='gr.y'>
print(re.search(r"gr.y", "gr!y"))   # <re.Match object; span=(0, 4), match='gr!y'>
```
So in this example the meta character `.` will match on `e a 7 . !`

Can we repeat the `.` character?
```python
import re
print(re.search(r"gr..", "grey"))       # <re.Match object; span=(0, 4), match='grey'> 
print(re.search(r"gr..", "grad"))       # <re.Match object; span=(0, 4), match='grad'>
print(re.search(r"gr..", "gr:43"))      # <re.Match object; span=(0, 4), match='gr:4'>

# "gr" followd by 4(!) any characters
print(re.search(r"gr....", "great"))    # None
```
So repeating the meta character will match multiple "any characters". 

*Attention: As you see in the last example, matching 6 characters in total will not match on a string of length 5. The last 4 characters are arbitrary but not optional!*

What if we want to match a literal dot `.`?

In this case we have to quote the dot by using a backslash. This tells the RegEx interpreter not use the dot literally. 

```python
s = "This line ends with a dot."
print(re.search(r"\.", s))      # match the '.'

s_2 = "This line does not end with a dot"
print(re.search(r"\.", s_2))    # None
```

What if we don't know the exact amount of characters? This is where the next chapter comes into play ...

[Overview](./overview.md) | [Back (Introduction)](./introduction.md) | [Next (Quantifier)](./quantifier.md) 