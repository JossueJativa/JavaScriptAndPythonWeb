#self representa al mismo objeto al cual tenemos la clase y se le va a llamar
class Point():
    def __init__(self, x, y):
        #Como se le asigna un valor a x
        self.x = x
        #Como se le asigna un valor a y
        self.y = y

p = Point(3, 5)

print (p.x)
print (p.y)