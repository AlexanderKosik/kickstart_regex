[Overview](./overview.md) | [Back (Groups)](./groups.md) | [Next (Substitution)](./sub.md) 

# Lookaround

By using anchors like `^` (line beginning) or `$` (line ending) we can define positions in a string that do not consume text but match on the positions. 

Lookaround groups act similar, but we can define exactly how that position should look like. Lookaround groups do not consume any text, they mark a position. With that we can specify positions like "I expect string `subject` to the right" or "I expect something that is not a number to the left". 

## Lookahead
To look ahead we use a lookahead group defined with `(?=)`. This will check if the group content is "on the right side" of the current RegEx position. 

Here is an example:
```python
import re

# will only match Alex if part of Alexander
print(re.search(r"Alex(?=ander)", "My name is Alexander") is not None) 

# will not match because `ander` is missing
print(re.search(r"Alex(?=ander)", "My name is Alex") is not None) 
```

## Lookback
We can do the same in opposite direction by using a lookback group. This group is defined with `(?<=)`. 

So if we want to match a number only if on the left side is a dollar sign we can do something like this:

```python
import re

# will only match if we have a dollar sign before the number
print(re.search(r"(?<=\$)\d+", "The price is $100") is not None) 

# will not match, dollar sign is missing
print(re.search(r"(?<=\$)\d+", "The price is 100€") is not None) 
```

It is important to understand that groups with lookaround do not consume any character. They will check if it will match (back and furth) but they will not be part of the match. 

## Negative Lookaround
So far we have used lookarounds that will match but not consume. Technically speaking these were positive lookahead and positive lookback. We can also define negative lookahead and negative lookbacks. These will only match (but not consume) if something is not followed or not prior to something. 

The syntax for lookaround groups are:

    Lookahead:
    Negative lookahead: (?!)
    Positive lookahead: (?=)

    Lookback
    Negative lookback: (?<!)
    Positive lookback : (?<=)

We will practice these lookarounds in the next chapter.

[Overview](./overview.md) | [Back (Groups)](./groups.md) | [Next (Substitution)](./sub.md) 
