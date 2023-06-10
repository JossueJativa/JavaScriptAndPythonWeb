#Crear una lista con tres diccionarios dentro
Persona = [
    {"Person": "Juan", "House": "Gryffindor"},
    {"Person": "Luis", "House": "Slytherin"},
    {"Person": "Maria", "House": "Hufflepuff"}
]

#si no se le asigna una key, para saber que ordenar del diccionario va a mandar un error de comparacion
#Para ordenar se puede hacer de dos formas, con una funcion o usando lambda
#Funcion
def ordenar(Persona):
    return Persona["Person"]
#Lambda
Persona.sort(key = lambda Persona: Persona["Person"])
#Imprimir la lista de personas
print (Persona)

Persona.sort(key = ordenar)
print (Persona)