import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_circumference(self):
        return 2 * math.pi *self.__radius #프라이빗 변수 __변수이름
    def get_area(self):
        return math.pi * (self.__radius ** 2) #__를 붙이면 외부에서 사용 불가
    
circle = Circle(10)
print("원의 둘레:", circle.get_circumference())
print("원의 넓이", circle.get_area())
print(circle.__radius)