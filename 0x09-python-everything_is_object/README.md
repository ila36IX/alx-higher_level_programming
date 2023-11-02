# Everything is object

![](https://miro.medium.com/v2/resize:fit:640/format:webp/0*XgBeJyBdtLYUXLVb.jpg)

# Some tricks

To get the type of an object you can use `type` function:

```python
>>> type(5)
<class 'int'>
```

To obtain the memory address (also known as the identifier or reference) of a variable you can use the built-in `id` function.

```python
>>> id(15)
9793536
```

### `__slots__` atrribute

In Python, you can stop a class from creating new attributes by using `__slots__`. It's a tuple of allowed attribute names. If you try to add an attribute not in `__slots__`, Python will raise an `AttributeError` error. This helps control which attributes your class can have.

Here's an example of how to use `__slots__` to restrict the attributes of a class:

```python
class MyClass:
    __slots__ = ('attribute1', 'attribute2')  # Define allowed attribute names

    def __init__(self, attr1, attr2):
        self.attribute1 = attr1
        self.attribute2 = attr2

# Creating an instance of MyClass
obj = MyClass('value1', 'value2')

# Valid attribute assignments
obj.attribute1 = 'new_value1'
obj.attribute2 = 'new_value2'

# Attempting to create a new attribute will raise an AttributeError
# obj.new_attribute = 'new_value'  # This line will raise an AttributeError
```

## 1. Objects and Values

- Variables `a` and `b` can refer to the same object or two different objects with the same value.
- Strings are immutable, meaning their values cannot be changed. Python optimizes resources by making variables that refer to the same string value point to the same object.

Example:
```python
a = "banana"
b = "banana"
print(a == b)  # Output: True
print(a is b)  # Output: True
```

## 2. Aliasing

- If one variable is assigned to another, both variables refer to the same object. Changes made using one variable affect the other.
- This behavior is called aliasing and is common with mutable objects like lists.

Example:
```python
a = [1, 2, 3]
b = a
print(a is b)  # Output: True
b[0] = 5
print(a)  # Output: [5, 2, 3]
```

## 3. Cloning Lists

- To modify a list and keep a copy of the original, you need to clone the list.
- Cloning creates a new list, ensuring changes to one list do not affect the other.

Example:
```python
a = [1, 2, 3]
b = a[:]
print(b)  # Output: [1, 2, 3]
b[0] = 5
print(a)  # Output: [1, 2, 3]
```

## 4. Immutable vs. Mutable Types

- Immutable types, like strings, cannot be changed in place. Any operation results in a new object.
- Mutable types, like lists, can be changed both in place and by reassignment.

Example:
```python
x = 'foo'
y = x
y += 'bar'
print(x)  # Output: 'foo'

x = [1, 2, 3]
y = x
y += [3, 2, 1]
print(x)  # Output: [1, 2, 3, 3, 2, 1]
```
