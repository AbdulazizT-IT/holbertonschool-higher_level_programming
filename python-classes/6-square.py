#!/usr/bin/python3
"""Defines an class Square."""


class Square:
    """Represents a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Creates a square of a given size

        Size of the square is hidden

        Args:
            size (int): length of the sides
            position (tuple): the position of the square

        Raises:
            TypeError: size is not an integer
            ValueError: size is negative

        """

        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the size of square

        Returns:
            size squared for area

        """

        return self.__size ** 2

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if(
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
            ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints out a grid of #'s representing the sqaure

        prints a blank line if size is 0

        also moves the sqaure to match position

        """

        if self.__size == 0:
            print()

        for y in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(' ', end='')
            for j in range(self.__size):
                print('#', end='')
            print()
