[Overview](./overview.md) | [Back (Lookaround)](./lookaround.md) 

# Substitution

So far we have used RegEx to validate if certain strings match defined criteria. But we can use RegEx also in a way to substitute certain matches with something else. 

How can we use that? We get practical ...

Let's say we have converted a lot of images from the jpg-format to a png-format. Since the strings are referenced in our source code we want to automatically change the file ending. 

We could use the `str.replace` method for that in python.

```python
filenames_jpg = [
    "test.jpg",
    "home.jpg",
    "index.jpg"
]

filenames_png = [s.replace("jpg", "png") for s in filenames_jpg]
print(filenames_png)

```
But what if we have not only converted files with the ending `jpg` but also `jpeg` and `bmp`?

Things get ugly if we keep on repeating the `str.replace` method with different endings, so there must be a better way!

And of course there is by using RegEx. We use the `re.sub` method in Python for that. This will look like this:

```python
import re

filenames_mixed = [
    "test.jpg",
    "home.jpg",
    "index.jpg",
    "sell.png",
    "passwort.bmp",
    "holiday.jpeg"
]

filenames_png = []
for file in filenames_jpg:
    # re.sub(pattern, replace, string)
    png_file = re.sub(r"(\w+)\.(jpg|png|jpeg|bmp)", r"\1.png", file)
    filenames_png.append(png_file)

print(filenames_png)
```
Let's examine the `re.sub` command.

- First we created a capturing group matching any word character `(\w+)`
- This got followed by a literal dot `\.`
- Followed by a group alternation for different file endings `(jpg|png|jpeg|bmp)`

Now comes the interesting part. We referenced our first group in our replacement string by using `\1`. Every opening group can be referenced again by a group number starting from 1. 

So we substitute our match with the content of the first capturing group (the filename without ending), followed by a literal dot and the file ending png. 

That gives us a lot more possibilities :)

## Non-capturing groups
Groups are capturing by default. We can specifiy a group as a non capturing group if we define the group like this: `(?:)`. These groups cannot be back-referenced any more. This feature is more like a documentational feature if we want to make clear, that this match will not be referenced or needed later on. 

# Exercise

We now combine the substituion command with features we learned several chapters ago in this real-world exercise. 

Let's say we have a homepage with a lot of image tags. They look like these:

```python
html_string = '<img src="python.png" alt="Python Skill">'
html_string += '<img src="images/cpp.png" alt="C++ Skill">'
html_string += '<a href="index.html" class="brand-logo left"><img class="responsive-img" id="logo" src="pic.png"/></a>'
```
As you see the images are located in the same directory as the html files. This is no good style so every image file is moved to an image directory.

But now every image tag has to be changed, too. What makes things even worse is, that some images already are in the image directory. Because our homepage has quite a lot of images it is not practical to change every `src-tag` by hand. And since we know RegEx we use our new super power :)

So we want the content of the src-tag to be changed like this:

| Old Src                 | New Src                       | Comment |
|:-----------------------:|:-----------------------------:|---------|
| src="pic.png"           |  src="images/pic.png"         | change
| src="python.png"        |  src="images/python.png"      | change
| src="python.jpeg"       |  src="images/python.jpeg"     | change
| src="images/idx.jpeg"   |  src="images/idx.jpeg"        | **no change**
| src="images/test.jpg"   |  src="images/test.jpg"        | **no change**


At this point our RegEx toolkit is well equiped so we can solve this problem in multiple ways. So there is no "single correct solution". 

```python
import re

lines = [
    'src="pic.png"',
    'src="python.png"',
    'src="python.jpeg"',
    'src="images/idx.jpeg"',
    'src="images/test.jpg"',
]

fixed = []
for line in lines:
    # replace search and replace here
    fix = re.sub(r'...', '...', line)
    fixed.append(fix)

assert fixed[0] == 'src="images/pic.png"'
assert fixed[1] == 'src="images/python.png"'
assert fixed[2] == 'src="images/python.jpeg"'
assert fixed[3] == 'src="images/idx.jpeg"'
assert fixed[4] == 'src="images/test.jpg"'
print("Good RegEx")
```

[Overview](./overview.md) | [Back (Lookaround)](./lookaround.md) 