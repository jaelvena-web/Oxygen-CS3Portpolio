class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return f"{self.__length} cm"

    @length.setter
    def length(self, new_length):
        if new_length <= 0:
            print("Length must be greater than 0.")
        else:
            self.__length = new_length
            print(f"Length updated to {self.__length} cm.")

    @length.deleter
    def length(self):
        del self.__length
        print("Length deleted.")

    @property
    def width(self):
        return f"{self.__width} cm"

    @width.setter
    def width(self, new_width):
        if new_width <= 0:
            print("Width must be greater than 0.")
        else:
            self.__width = new_width
            print(f"Width updated to {self.__width} cm.")

    @width.deleter
    def width(self):
        del self.__width
        print("Width deleted.")

rectangle = Rectangle(10, 5)
del rectangle.width
del rectangle.length
rectangle.length = 15
print(rectangle.length)