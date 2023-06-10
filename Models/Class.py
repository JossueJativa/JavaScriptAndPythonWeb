#self representa al mismo objeto al cual tenemos la clase y se le va a llamar
class Point():
    def __init__(self, x, y):
        #Como se le asigna un valor a x
        self.x = x
        #Como se le asigna un valor a y
        self.y = y

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    ##agregar mefotos a las funciones
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        else:
            self.passengers.append(name)
            return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

p = Point(3, 5)

print (p.x)
print (p.y)

#Crear un vuelo con 3 asientos
flight = Flight(3)
people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    succes = flight.add_passenger(person)
    if succes:
        print (f"Se agrego a la persona {person} al vuelo con exito")
    else:
        print (f"No hay asientos disponibles para la persona {person}")
