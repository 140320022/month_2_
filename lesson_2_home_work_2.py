class Figure:
    unit = "cm"

    def __init__(self):
        pass
    def calculate_area(self):
        pass
    def info(self):
        pass

class Square(Figure):
    def __init__(self,side_lenght):
        self.__side_length = side_lenght
    def calculate_area(self):
        area = self.__side_length*self.__side_length
        return  area
    def info(self):
        return  f'Squarea side length:{self.__side_length},{self.unit},area:{self.calculate_area()}{self.unit}'

class Rectangle (Figure):
    def __init__(self,length,width):
        self.__length = length
        self.__width = width
    def calculate_area(self):
        area = self.__length*self.__width
        return  area
    def info(self):
        return  f'Rectangle length:{self.__length}{self.unit},width:{self.__width}{self.unit},area:{self.calculate_area()}'

square1 = Square(5)
square2 = Square(8)
rectangle1 = Rectangle(4,5)
rectangle2 = Rectangle(7,3)
rectangle3 = Rectangle(6,4)
figures = [square1,square2,rectangle1,rectangle2,rectangle3]
for figure in figures:
    print(figure.info())