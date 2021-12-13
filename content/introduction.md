[Overview](./overview.md) | [Next (Meta characters)](./meta.md) 

# Introduction

No introduction to Regular Expressions without the famous words of Jamie Zawinski.

![Introduction](ressources/re2.png "Introduction")

Regular Expressions are a powerful tool which should be in every developers toolkit. But be aware, that they are not the solution to every problem.

But what are Regular Expressions (or short: RegEx)?

Regular Expressions are used for matching a string within a string. They can:
    - check, if a string is contained
    - extract information (e.g. substrings) out of a string

If we look at modern programming languages like Python, the builtin string method is already quite powerful. 

```python
# Check if a string is contained in another string
exc = "Fatal error occured on system deathstar01"
print("Fatal error" in exc)

ok = "Successful login on system deathstar01"
print("Fatal error" in ok)
```
To check if a string is contained in another string is quite easy. It is also quite easy to check, if a string starts or ends with a specific string.

```python
# Check if a string starts with a specific string
s = "Hello World"
print(s.startswith("Hello")) # case sensitive
print(s.lower().startswith("hello")) # case insensitive
```

Even more complex checks are possible, all without the use of RegEx.

```python
# Check if we have a vowel in the passed string
def has_vowel(s):
    # case sensitive
    return "a" in s or "e" in s or "i" in s or "o" in s or "u" in s 

print(has_vowel("Hello World"))
print(has_vowel("zzz"))

print("-- Generator --")
# Generator expression with built-in `any` functio 
print(any(c in "Hello World" for c in 'aeiou'))
```

## Limitations
The shown examples are quite easy to solve with the builtin functions and methods of the string object. Not only in Python, but also in most other Programming Languages (like Java or C++). 

But with some task we reach the limit of what is possible. What if:
- I want to match an arbitrary character
- I want to have 0..x matches of a character
- I want to specifiy the position of the match. E.g. at the beginning of the row, end of the row, or word boundary

Then ... well ... we need to:

![Regex all the things](ressources/re3.png "Regex all the things")

[Overview](./overview.md) | [Next (Meta characters)](./meta.md) 