import math
class circle:
    def __init__(self, radius):
        self.__radius = radius
    @property
    def getRadius(self): return self.__radius
    @getRadius.setter
    def getRadius(self, r): self.__radius = r
    def calcArea(self, r): self.__radius = (r**2)*math.pi
    def calcCirum(self, r): self.__radius = r*2*math.pi

C = circle(10)
print('반지름은 ', C.getRadius)
C.calcArea(10)
print('원의 넓이는 ', C.getRadius)
print()
C = circle(10)
print('반지름은 ', C.getRadius)
C.calcCirum(10)
print('원의 둘레는 ', C.getRadius)

