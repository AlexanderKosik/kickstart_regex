
There is no single one correct solution to the exercises.

Solutions might differ regarding complexity, how general they are and how easy they are to understand and change. These solutions are just here to give you an idea about how to solve the exercises if you get stuck.

# Meta
```python
m = re.match(r"........\....", filename)
```

# Quantifier

## Valid filename
```python
m = re.match(r".+\..{3,}", filename)
```

## Valid email
```python
m = re.match(r".+@.{3,}\..{2,}", email)
```

# Character classes

### Better IP validator
```python
m = re.match(r"192\.168\.1\.[0-9]{1,3}", ip_address)
```

### Hexadecimal validator
```python
m = re.match(r"0x[0-9A-F]{1,4}", hex_string)
```

### Email revisited
```python
m = re.match(r"[a-zA-Z]+@.{3,}\.[a-zA-Z]{2,}", email)
```

# Anchors

### Valid filenames Windows
```python
m = re.search(r'^[^\/:*?"]+\.[^\/:*?"]{3}$', filename)
```

### Is integer
```python
m = re.search(r"^-?\d+$", string)
```

# Groups

### submatch
```python
pattern = r"^invoice_[\w]+\.pdf$"
```

## Exercise Phone number
```python
return bool(re.match(r"(\+?\d{5}|\d{4})/\d{7,}", number))
```

## Exercise Valid hour
```python
return re.match(r"([01]\d|[2][0-3]):[0-5]\d", string) is not None
```
## Valid ip address
```python
m = re.match(r"^192\.168\.1\.([0-9]|\d\d|1\d\d|2[0-5][0-5])$", ip_address
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
