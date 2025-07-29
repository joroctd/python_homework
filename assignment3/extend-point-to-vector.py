def check_other_type(method):
    def wrapper(self, other):
        if isinstance(other, self.__class__):
            return method(self, other)
        else:
            print('Provided object is not of the same type.')
            return None
    return wrapper

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @check_other_type
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
    def __str__(self):
        return f'''Point<x={self.x}, y={self.y}>'''

    @check_other_type
    def __sub__(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

class Vector(Point):
    def __str__(self):
        return f'''Vector<x={self.x}, y={self.y}>'''

    @check_other_type
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

pointA = Point(1, 1)
pointB = Point(2, 2)
pointC = Point(1, 1)
print('pointA:', pointA)
print('pointB:', pointB)
print('pointC:', pointC)
print('pointA == pointB:', pointA == pointB)
print('pointA == pointC:', pointA == pointC)
print('pointB - pointA:', pointB - pointA)
print('pointC - pointA:', pointC - pointA)
print()
vectorA = Vector(1, 2)
vectorB = Vector(2, 3)
print('vectorA:', vectorA)
print('vectorB:', vectorB)
print('vectorA + vectorB:', vectorA + vectorB)
