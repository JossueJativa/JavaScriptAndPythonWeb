#libreria de expresiones regulares y salida del sistema
import sys

##Ingresar dos numeros
x = int (input("Ingrese la x: "))
y = int (input("Ingrese la y: "))

#calcular la divicion 
try:
    divicion = x / y
except ZeroDivisionError:
    print ("No se puede dividir por cero")
    sys.exit(1)
print ("La divicion es: ", divicion)