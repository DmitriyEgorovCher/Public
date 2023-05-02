from rectangle import Rectangle, Square, Circle

# Создаем 2 прямоугольника

rect1 = Rectangle(3,4)
rect2 = Rectangle(12,5)

print(rect1.getArea())
print(rect2.getArea())

square1 = Square(5)
square2 = Square(10)

print(square1.getAreaSquare())
print(square2.getAreaSquare())

circle1 = Circle(3)
circle2 = Circle(6)

print(circle1.getAreaCircle())
print(circle2.getAreaCircle())
figures = [rect1, rect2, square1, square2, circle1, circle2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.getAreaSquare())
    elif isinstance(figure, Circle):
        print(figure.getAreaCircle())
    else:
        print(figure.getArea())