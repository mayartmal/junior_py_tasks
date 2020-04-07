#Напишите функцию, которая на вход принимает список геометрических
#фигур с различными параметрами и выводит площадь каждой фигуры.
#Используйте полиморфизм.

class Figure(object):

	def __init__(self):
		super(Figure, self).__init__()
	def calculate_area():
		print("It is abstract figure with out area")

		
class Circle(Figure):
	def __init__(self, radius):
		super(Circle, self).__init__()
		self.radius = radius
	def calculate_area(self):
		area = (self.radius ** 2) * 3.1416
		return area


class Rectangle(Figure):
	def __init__(self, a_side, b_side):
		super(Rectangle, self).__init__()
		self.a_side = a_side
		self.b_side = b_side
	def calculate_area(self):
		area = self.a_side * self.b_side
		return area

			
class Square(Figure):
	def __init__(self, side):
		super(Square, self).__init__()
		self.side = side
	def calculate_area(self):
		area = self.side ** 2
		return area


testCircle = Circle(1)
testRectangle = Rectangle(2, 3)
testSquare = Square(3)

figure_list = (testCircle, testRectangle, testSquare)

def areas(figure_list):
	for figure in figure_list:
		area = figure.calculate_area()
		print("Area of the object is:", area)

areas(figure_list)
