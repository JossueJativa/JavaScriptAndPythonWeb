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
    
##Creacion de una funcion el cual va a aununciar algo
def announce(f):
    def wrapper():
        print ("A punto de ejecutar la funcion...")
        f()
        print ("Se ejecuto la funcion")
    return wrapper

##La funcion utiliza que cuando se llame a la funcion se va a ejecutar la funcion announce
@announce ##Aqui se llama a la funcion announce
#cuando llega a la parte de f() se va a ejecutar la funcion hello
def hello():
    print ("Hola mundo")

#Imprimir la funcion hello
hello()

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
