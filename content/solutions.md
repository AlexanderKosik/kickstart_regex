
There is no single one correct solution to the exercises. 

Solutions might differ regarding complexity, how generell they are and how easy they are to understand and to change. They will give you just an idea how you could solve the exercises if you get stuck.

# Groups

## Exercise Phone number
```python

```

## Exercise Valid hour
```python

```

# Sub

## Exercise
```python
fix = re.sub(r'"(\w+\.\w{3,4})"', r'"images/\1"', line)
```

## Extended Exercise
```python
fix = re.sub(r'src=\"(?!images)(?:[a-zA-Z0-9/_])*?/?(\w+\.\w+)\"', r'src="images/\1"', line)
```
