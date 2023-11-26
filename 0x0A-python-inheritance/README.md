# Python - Inheritance
![](https://media.tenor.com/1SwdfIZZkx4AAAAd/wes-dst.gif)


# Understanding `setattr`, `getattr`, `__eq__`, and `__ne__` in Python

## `setattr` and `getattr`

### `setattr`:

- **Syntax:** `setattr(object, name, value)`

- **Usage:**
  - Sets the attribute with the given name on the specified object.
  - Useful for dynamically adding attributes during runtime.

- **Example:**
  ```python
  setattr(obj, 'new_attribute', 42)
  ```

### `getattr`:

- **Syntax:** `getattr(object, name[, default])`

- **Usage:**
  - Gets the value of the attribute with the given name from the specified object.
  - Allows optional default value if the attribute is not found.

- **Example:**
  ```python
  value = getattr(obj, 'existing_attribute', default_value)
  ```

## `__eq__` and `__ne__`

### Introduction:

In Python, `__eq__` and `__ne__` are special methods that define the behavior of equality and inequality comparisons for objects.

### `__eq__` (Equal):

- **Purpose:**
  - Defines the behavior of the equality operator `==`.

- **Usage:**
  - Override this method to customize how instances of a class are compared for equality.

- **Example:**
  ```python
  def __eq__(self, other):
      return self.attribute == other.attribute
  ```

### `__ne__` (Not Equal):

- **Purpose:**
  - Defines the behavior of the inequality operator `!=`.

- **Usage:**
  - Override this method to customize how instances of a class are compared for inequality.

- **Example:**
  ```python
  def __ne__(self, other):
      return self.attribute != other.attribute
  ```

## `__slots__`

### Introduction:

In Python, `__slots__` is a class variable that restricts the attributes a class can have, providing memory efficiency.

### `__slots__`:

- **Purpose:**
  - Defines a tuple of attribute names that are allowed for instances of a class.

- **Usage:**
  - Limits the attributes a class instance can have to those specified in `__slots__`.
  - Improves memory usage compared to dynamically adding attributes.

- **Example:**
  ```python
  class MyClass:
      __slots__ = ('attribute1', 'attribute2')
  ```

## **Inheritance:**

  ```python
  class Person:
      # ...

  class Employee(Person):
      # ...
  ```

- **Polymorphism:**
  ```python
  class Bird:
      def flight(self):
          print("Most birds can fly.")

  class Sparrow(Bird):
      def flight(self):
          print("Sparrows can fly.")

  class Ostrich(Bird):
      def flight(self):
          print("Ostriches cannot fly.")
  ```

- **Encapsulation:**
  ```python
  class Base:
      def __init__(self):
          self.a = "GeeksforGeeks"
          self.__c = "GeeksforGeeks"

  class Derived(Base):
      def __init__(self):
          Base.__init__(self)
          print(self.__c)  # Raises AttributeError
  ```

- **Data Abstraction:**
  ```python
  from abc import ABC, abstractmethod

  class AbstractClass(ABC):
      @abstractmethod
      def abstract_method(self):
          pass
  ```
