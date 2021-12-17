# Groups

So far we have printed the whole match object most of the time. What if we only want to print/process the actual match or just a part of the match?

This is where groups come into play. 

```python
import re

match = re.search(r"\d{5}", "07231")
print(match.group())    # will only print the match 07231
```

We can use *groups* in multiple ways. One common use-case is to be able to use quantifiers for multiple characters. 

```python

m = re.search(r"abc{3}", "abccc")
print(m.group())

# How can we match "abc" 3 times 
m = re.search(r"abcabcabc", "abcabcabc")
print(m.group())

# This looks simpler
m = re.search(r"(abc){3}", "abcabcabc")
print(m.group())

# With this we can match any combination of abc 3 times
m = re.search(r"([abc]{3}){3}", "abccbacbca")
print(m.group())
```

## Exercise (Valid mobile number)

We want to validate some mobile numbers. For that we write a function that returns `True` if passed string contains a valid mobile number, or False otherwise.

We define valid numbers as followed:
```python
valid_1 = "+49179/123456789"
valid_2 = "0179/123456789"
invalid = "+490179/123456789"

# Tipp: (aaa|bbb) matches either `aaa` or `bbb`

def is_valid(number):
    # Replace ... with valid RegEx
    return bool(re.search(r"...", number))

assert is_valid(valid_1) == True, "Check valid number with +49"
assert is_valid(valid_2) == True, "Check valid number with 0179"
assert is_valid(invalid)) == False, "Check invalid number"
print("Good RegEx")
```

# Printing groups
If we use *groups* in a regular expression we can use these groups separatly if the RegEx matches. Have a look at this example

```python
number = "0179/123456789"
number_2 = "+49179/123456789"

m = re.search(r"^(\+\d{5}|\d{4})/(\d{9})$", number_2)
print("Complete number:", m.group())
print("First part:", m.group(1))
print("Second part:", m.group(2))

# IndexError. This will not work, because we have no group with index 3
print("Third part:", m.group(3))    # IndexError
```

Every specified group can be extracted using a group index starting from 1 for the first group. The index is increased for every following group. If we want to get a group that is not available, we will get an error.

## Exercise (Valid hour)
We want to write a RegEx which will verify valid times. 
