[Overview](./overview.md) | [Back (Introduction)](./introduction.md) | [Next (Quantifier)](./quantifier.md)

# Meta Characters

As before we show the usage of Regular Expressions with the Python Programming Language. In Python we have a module named `re` for Regular Expressions. Before using the module, we have to import it.

We start our journey by using the `re.search` method. Have a look at the help output.

``` python
# import the regular expression module
import re
help(re.search)

# will deliver this output:
# Help on function search in module re:
#
# search(pattern, string, flags=0)
#    Scan through string looking for a match to the pattern, returning
#    a Match object, or None if no match was found.
```

The function `re.search` takes a pattern as the first parameter. This pattern is searched in the passed string (2nd parameter). The 3rd paramter (`flags`) can be ignored at the moment.

We use a similar example as before by searching a string literal (a string literal is a fixed string like `"Fatal error"`) in another string.

```python
import re

# search(pattern, string, flags=0)
m = re.search(r"Fatal error", "Successful login to bender007")
print(m)    # prints None because `Fatal error` was not found in string

m = re.search(r"error", "Random error message just to annoy you.")
print(m)    # <re.Match object; span=(7, 12), match='error'>
```

In these two examples we used the `re.search` method to search for a string within a string. That is nothing fancy, we did more or less the same by using the `in` operator in the example from the introduction. The only new thing is the usage of the Regular Expression module in Python.

Python has a special string prefix to create a `raw string`. Since these `raw strings` are very useful in the context of RegEx we will take a closer look at them in brief.

## Using Pythons string prefix "`r`"
When using the Python Programming language we have several special string prefixes available. By using the string prefix `r` we create a `raw string`.

By using this raw strings escaped characters like `\n` (New line) will not be interpreted. Let's look at an example and see raw strings in action.

```python
# We print a `normal string`.
# \n is an 'escaped char' and every occurence will result in a new line
print("Dear Sir or Madamme\n\nI like to inform you about a fire in the basement!\n")

# We now create a raw string by using the string prefix 'r'
# \n will not be interpreted
# So everything is in a one line with literal \n
print(r"Dear Sir or Madamme\n\nI like to inform you about a fire in the basement!")
```

When using Regular Expressions we want in nearly all cases that `escaped characters` are not interpreted.

So the general rule of thumb is: Use raw strings whenever you use RegEx. This will save a lot of trouble.

## Another RegEx Example

After this short outline about raw strings back to the original topic: the use of the `re module`.

The `re.search` method returns a `Match object` if the RegEx string is found in the passed string. If nothing is found, `re.search` returns None.

```python
m = re.search(r"100€", "The price is 100€")
print(m)    # <re.Match object; span=(18, 22), match='100€'>

m = re.search(r"100€", "The price is $100")
print(m)    # None
```

Still we can implement this example quite easily without RegEx. For example like this:

```python
# Without using RegEx
b_euro = r"100€" in "The price is 100€"
b_dollar = r"100€" in "The price is $100"

print(b_euro, b_dollar)
```

So what's the matter with RegEx?!

## The Power of Meta Characters
Most characters match exactly on itself. The pattern `r"100€"` from the previous examples will match exactly on the string literal `100€`, `r"test"` will match exactly on the string literal `test`.

But there are exceptions. These exceptions are called `meta characters`.

A RegEx may contain the following `meta characters`:

`Meta characters: . ^ $ * + ? { } [ ] \ | ( )`

We start by having a closer look on the meta character `.` (dot).

### Meta Characeter . (dot)
The meta character `.` matches any character. It does not matter if it is a letter, a number or a special character like `!`. The dot will match.

Let's have a closer look on the usage and what it will match:

```python
import re
print(re.search(r"gr.y", "grey"))   # <re.Match object; span=(0, 4), match='grey'>
print(re.search(r"gr.y", "gray"))   # <re.Match object; span=(0, 4), match='gray'>
print(re.search(r"gr.y", "gr7y"))   # <re.Match object; span=(0, 4), match='gr7y'>
print(re.search(r"gr.y", "great"))  # None
print(re.search(r"gr.y", "gr.y"))   # <re.Match object; span=(0, 4), match='gr.y'>
print(re.search(r"gr.y", "gr!y"))   # <re.Match object; span=(0, 4), match='gr!y'>
```

In this example the meta character `.` will match on `e a 7 . !`.

Let's have a detailed description of how the RegEx will work internally if we use the search pattern `"gr.y"` on the target string `"grey"`.

- Is the first character of the target string a `g`? Yes, so we proceed.
- Is the second character of the target string a `r`? Yes, so we proceed.
- Is a third character available (not matter what it is)? Yes, so we proceed.
- Is the forth character of the target string a `y`? Yes, so we are done and have a match.

Why does `"gr.y"` not match on `"great"`? Let's inspect.

- Is the first character of the target string a `g`? Yes, so we proceed.
- Is the second character of the target string a `r`? Yes, so we proceed.
- Is a third character available (not matter what it is)? Yes, it is an `e` and we proceed.
- Is the forth character of the target string a `y`? No, it is an `a`. The search will abort.

What if we want to match multiple arbitrary characters? Can we repeat the `.` character?

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

In this case we have to quote the dot by using a backslash. This tells the RegEx interpreter not interpret the dot as an "any character".

```python
s = "This line ends with a dot."
print(re.search(r"\.", s))      # match the '.'

s_2 = "This line does not end with a dot"
print(re.search(r"\.", s_2))    # None
```

So the meta character `.` is kind of cool and with this simple extension we can do much more than with "normal string methods".

# Exercise

We want to know if a passed filename will match a specific pattern. In this example a valid filename is defined as followed:

- Has exactly 8 arbitrary characters
- Followed by a literal dot
- Followed by exactly 3 arbitrary characters

Copy the following code into a Python file or an interactive sessions and replace the `"..."` with a valid RegEx.

If your RegEx is correct you should see a message `"Good RegEx!"` or an assertion otherwise.

```python
import re

def simple_validator(filename):
    # Replace ... with valid RegEx
    m = re.match(r"...", filename)
    return m is not None

assert simple_validator("test.txt") is False
assert simple_validator("autofile.cmd") is True
assert simple_validator("test0010.txt") is True
assert simple_validator("test001.txt") is False
assert simple_validator("test.tar.gz") is False
assert simple_validator("test00100.tx") is False
print("Good RegEx!")
```

*Using `re.match`: We use the `match` function in most of the validation exercises. Compared to the `search` function `match` tries to apply the pattern at the start of the string and this is exactly what we want in most cases.*

Ok, that was cool! But the solution may look a little bit odd (there are a lot of dots in it, isn't it)?

So how can we do better? And what if we don't know the exact amount of characters? This is where the next chapter comes into play ... So stay tuned!

[Overview](./overview.md) | [Back (Introduction)](./introduction.md) | [Next (Quantifier)](./quantifier.md)
