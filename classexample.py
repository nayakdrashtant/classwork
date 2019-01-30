# class objects and constructor
class Point():
    print("This is a line")
    a = 5
    def __init__(self):
        self.y = 0
        self.x = 0

mypoint = Point()
mypoint.a
mypoint1 = Point()
mypoint1.x = 5
print(mypoint1.x)
