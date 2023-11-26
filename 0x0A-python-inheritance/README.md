# Python - Inheritance
![](https://media.tenor.com/1SwdfIZZkx4AAAAd/wes-dst.gif)

## Concepts Covered:

### 1. Class:
- A blueprint or prototype for creating objects.
- Contains attributes (variables) and methods (functions).

### 2. Objects:
- Entities with state, behavior, and identity.
- Instances of a class.

### 3. Polymorphism:
- Having many forms.
- Classes can provide different implementations of methods.

### 4. Encapsulation:
- Wrapping data and methods into a single unit (class).
- Restricts direct access to variables, promoting data integrity.

### 5. Inheritance:
- Capability of a class to derive properties from another class.
- Supports code reusability and the representation of real-world relationships.

### 6. Data Abstraction:
- Hides unnecessary code details from the user.
- Achieved through abstract classes.

## Examples:

- **Class Definition:**
  ```python
  class Dog:
      pass
  ```

- **Object Creation:**
  ```python
  obj = Dog()
  ```

- **Inheritance:**
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
