#!/usr/bin/python3
""" define class Rectangle """


from models.base import Base


class Rectangle(Base):
    """ class Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Init class """
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width """
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """ getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height """
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """ getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for x """
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """ getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter for y """
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ returns the area of the rectangle """
        return self.__height * self.__width

    def display(self):
        """ prints the rectangle using # """
        for a in range(self.__y):
            print()
        for i in range(self.__height):
            for b in range (self.__x):
                print(" ", end='')
            for j in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        return (f"[Rectangle] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}")
