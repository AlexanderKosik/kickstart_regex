[Overview](./overview.md) | [Next (Meta Characters)](./meta.md)

# Introduction

No introduction to Regular Expressions without the famous words of Jamie Zawinski.

![Introduction](ressources/re2.png "Introduction")

Regular Expressions are a powerful tool which should be in every developers toolkit. But be aware, that they are not the solution to every problem.

But what are Regular Expressions (or short: *RegEx*) good for?

**It is all about data**. RegEx offer us a way to control and master data. For example by an automatic extraction of specific rows from a very large file. Or by validating data that comes from a foreign source, for example from a user input.

So in most cases Regular Expressions are used for matching a string within another bigger string or file:

    - We check, if a string is contained in a string (so if it is a substring)
    - We extract information out of a string or file
    - We replace content if it matches certain criteria

Regular Expressions apear in a wide variety of domains. It is very often used in the context of unix operating systems where we have specific tools like *grep*, *sed* and *awk*, all of those support RegEx.

The programming language *Perl* is predestined for RegEx. But also languages like C++ (since C++11) or Java support Regular Expressions.

Within this course we will mostly focus on the Python programming language due to its simple syntax.

## Let's start
Most modern programming language have a built in string type. These string types are quite powerful in themselves.

If we look at methods of the builtin string type in Python we see that it has a lot of functionality. Let's have a look at some of these methods and let's see what we can do with them.

To check if a string is contained in another string is quite easy in Python. We can use the `in` keyword for that.
```python
# Check if a string is contained in another string
exc = "Fatal error occured on system deathstar01"
print("Fatal error" in exc)     # True

ok = "Successful login on system deathstar01"
print("Fatal error" in ok)      # False
```

*Hint: You can always copy and paste the python code into an interactive python session and run the code for yourself*

 It is also quite easy to check, if a string starts or ends with a specific string.

```python
# Check if a string starts with a specific string
s = "Hello World"
print(s.startswith("Hello"))            # case sensitive
print(s.lower().startswith("hello"))    # case insensitive
```

Even more complex checks are possible without the use of RegEx. Have a look at this example:

```python
# Check if we have a vowel in the passed string
def has_vowel(s):
    # case sensitive
    return "a" in s or "e" in s or "i" in s or "o" in s or "u" in s

print(has_vowel("Hello World"))     # True
print(has_vowel("zzz"))             # False

# Use of a generator expression with built-in `any` function
# for a more dense syntax
print("-- Generator Usage --")
print(any(c in "Hello World" for c in 'aeiou'))
```

## Limitations
The shown examples are quite simple and show the usage of builtin functions and methods of the Python string object well. The solutions are not only restricted to Python, similar methods exists in most other modern Programming Languages.

The point is that in most cases we are good to go when we use what's available in our string methods and ignore RegEx at all.

But there are also cases were we reach the limit of what is possible with builting methods. Here are some examples. What if:

- We want to match an arbitrary character
- We want to have `0..x` matches of a specific character or word
- We want to specifiy the position of the match. E.g. at the beginning of the row, end of the row, or word boundary

Then ... well ... we need to:

![Regex all the things](ressources/re3.png "Regex all the things")

Let's dive into this topic by introducting `meta characters`.

[Overview](./overview.md) | [Next (Meta Characters)](./meta.md)
