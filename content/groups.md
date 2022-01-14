[Overview](./overview.md) | [Back (Anchors)](./anchors.md) | [Next (Lookaround)](./lookaround.md) 

# Groups

So far we have printed the whole match object most of the time. What if we only want to print or process the actual match or just a specific part of the match?

This is where groups come into play. 

```python
import re

match = re.search(r"\d{5}", "07231")
if match:
    print(match.group())    # will only print the match 07231
```

In the above example we will only print the actual match by using `match.group()`. This requires a match object. If `re.search` finds no match it returns a `None` value. Calling a `group()` method on a None value will result in an exception. So checking if we get an actual match object is a good practice to avoid runtime errors. 

Let's see how we can define groups in a RegEx and how to use them in multiple ways.

## Groups: Remember sub-matches
We define groups in a RegEx with round brackets `( )`. Everything within this group will be captured and can be references later on. 

Let us illustrate this with an example.

`files` is a list of filenames. We now want only PDF files beginning with a specific string like `invoice`. 

Start by writing an RegEx that will match on files beginning with `invoice` and ending with `pdf`. 

```python
import re

files = [
    "holiday1999.png",
    "invoice_car_insurance.pdf",
    "invoice_telekom2021.pdf", 
    "invoice_vattenfall2021.pdf", 
    "manual_mazda_cx5.pdf",
    "passport.jpg",
    "resumee.pdf", 
]

# place your regex here
pattern = r"..."
filtered = [re.match(pattern, file).group() for file in files if re.match(pattern, file)]

assert len(filtered) == 3, "list length is 3"
assert "invoice_car_insurance.pdf" in filtered
assert "invoice_telekom2021.pdf" in filtered
assert "invoice_vattenfall2021.pdf" in filtered
print(filtered)
print("Good RegEx")
```

If your RegEx is correct you will see, that the list contains the 3 invoice files. What if we only want the actual filename, without the file ending `pdf`? We could filter our list afterwards and remove the filename, but it would be nice to have this done by our RegEx. 

We can do this with groups. So your RegEx might look like this: `pattern = r"^invoice_[\w]+\.pdf$"`. If we now want to be able to reference the actual filename without ending, we can put round brackets around these characters. 

```python
import re

files = [
    "holiday1999.png",
    "invoice_car_insurance.pdf",
    "invoice_telekom2021.pdf", 
    "invoice_vattenfall2021.pdf", 
    "manual_mazda_cx5.pdf",
    "passport.jpg",
    "resumee.pdf", 
]

# Usage of round brackets around the file name
pattern = r"^(invoice_[\w]+)\.pdf$"

# we reference the group (we use `group(1)` explicitly)
filtered = [re.match(pattern, file).group(1) for file in files if re.match(pattern, file)]

assert len(filtered) == 3, "list length is 3"
assert "invoice_car_insurance" in filtered
assert "invoice_telekom2021" in filtered
assert "invoice_vattenfall2021" in filtered
print(filtered)
print("Good RegEx")
```
As you see when `filtered` got printed the filenames now only contain the content of our specified group. 

Groups get referenced by index. Every opening round bracket will create a new index we can reference on later. The first group starts with index 1, the next has index 2 and so on. If we want to access a group that is not available, we will get an error. 

So in summary, groups allow us to reference sub-matches later on.

## Groups: Packing things together

Another common use-case is to be able to use quantifiers for multiple characters. Have a look at these examples.

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

As you have seen in the examples above we can use groups to be able to repeat certain patterns with a quantifier. 

## Groups: Alternation
Another use case for groups is using alternations. The meta character `|` means `or` and we can combine multiple RegEx within a group with that. 

Suppose we want to extract the salutation of a letter. The salutation may be "Dear Sir" or Dear Madamme". 

We could write a RegEx which matches one or the other like this: `r"Dear (Sir|Madamme)"`. This will match on both cases but not if Sir **and** Madamme are missing. Be aware, that we can use every meta characters or "Sub RegEx" within the groups, not just string literals as seen in this example. 

## Exercise (Valid mobile number)

We will now apply our new knowledge about *groups* in an exercise.

We want to validate some mobile numbers. For that we write a function that returns `True` if passed string contains a valid mobile number, or False otherwise.

We define valid numbers as followed:
```python
valid_1 = "+49179/123456789"
valid_2 = "0179/123456789"
invalid = "+490179/123456789"

# Tipp: (aaa|bbb) matches either `aaa` or `bbb`

def is_valid(number):
    # Replace ... with valid RegEx
    return bool(re.match(r"...", number))

assert is_valid(valid_1) == True, "Check valid number with +49"
assert is_valid(valid_2) == True, "Check valid number with 0179"
assert is_valid(invalid) == False, "Check invalid number"
print("Good RegEx")
```

# Alternation and capturing example
Have a look at this example which makes use of group alternation and referencing different capture groups for printing.

```python
number = "0179/123456789"
number_2 = "+49179/123456789"

m = re.match(r"(\+\d{5}|\d{4})/(\d{9})$", number_2)
print("Complete number:", m.group())
print("First part:", m.group(1))
print("Second part:", m.group(2))

# IndexError. This will not work, because we have no group with index 3
# print("Third part:", m.group(3))    # IndexError
```

## Exercise (Valid hour)
We want to write a RegEx which will verify valid times. 

```python
def valid_hour(string):
    # insert regex here
    return re.match(r"...", string) is not None

assert valid_hour("00:00") is True
assert valid_hour("23:59") is True
assert valid_hour("24:00") is False
assert valid_hour("25:59") is False
assert valid_hour("15:20") is True
assert valid_hour("23:60") is False
print("Good RegEx")
```

Could you solve the exercise? If yes, congratulations! This was no easy task at all!

### *Hints*
This exercise is not easy. Try to separate to problem into smaller sub-problems.

For that try to solve the "minute-problem" first. 

If you get stuck, use RegEx101 and use this test string for the minute problem. Can you find a pattern? 

```
:00
:01
:02
:03
:04
:05
:06
:07
:08
:09

:10
:11
:12
:13
:14
:15
:16
:17
:18
:19

:20
:21
:22
:23
:29

:30
:39

:40
:49

:50
:59
```
Note: Not every minute is posted in the test data... several minutes were skipped when starting with a `2` and only 2 minutes were posted when starting with 4 or 5. Feel free to extend the test data if the pattern is not clear to you.

### More hints

If the pattern did not emerge, have a look at the last number. It does not matter what number we have here, everything is valid. So we can use `\d`. 

In the first number only 0 to 5 is valid, so we can use `[0-5]`. 

We can combine these two and use: `[0-5]\d`.

### More hints
If you have solved the "minute problem", continue with the hour problem separated. 

If you RegEx101, use this test string:
```
00:
01:
02:
03:
04:
05:
06:
07:
08:
09:

10:
11:
12:
13:
14:
15:
16:
17:
18:
19:

20:
21:
22:
23:
```

Try to find a pattern.

### More hints

If we look at the last pattern we see, that if we have a `0` or a `1` as a first digit, every second digit is valid: `[01]\d`

If we have a `2` as first digit, only `[0-3]` is valid as the second digit. 

--- 
There is another use case for groups, the so called look around groups. We will have a look at them in the next chapter. 



[Overview](./overview.md) | [Back (Anchors)](./anchors.md) | [Next (Lookaround)](./lookaround.md) 