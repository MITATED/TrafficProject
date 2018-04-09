```python
class Rectangle(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def square(self):
		return self.width * self.height

	def perimeter(self):
		return (self.width + self.height) * 2

class Sqaure(Rectangle):
	def __init__(self, side):
		self.width = self.height = side

one = Rectangle(15, 2)
two = Sqaure(5)


print(one.square())
#>>> 30
print(one.perimeter())
#>>> 34
print(two.square())
#>>> 25
print(two.perimeter())
#>>> 20

````
