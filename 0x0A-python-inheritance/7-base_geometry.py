 #!/usr/bin/python3

"""

Empty class

"""
import doctest


class BaseGeometry:
    """Empty class"""

    def area(self):
        """Raise an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check the value type"""

        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")


if __name__ == "__main__":
    doctest.testfile("./tests/7-base_geometry.txt")
