#Esto es comentario equisde
print("Hola Mundo!")
print("Adios Mundo!")

5+1
print(4+6)
print(5-2)
print(3*4)
print(20/4)
#precedencia de operadores
print(5+8*(3+2))

#Tipos de datos

print(type(2))
print(type(8.62))
print(type("Texto"))
print(type('Texto'))
print(type("5"))

#Variables

mensaje = "Esto es un mensaje"
print(mensaje)
mensaje = "mensaje hackeado"
print(mensaje)
print(type(mensaje))
mensaje = 100
print(type(mensaje))
mensaje = 100.1
print(type(mensaje))

mis3animales = "Perico, Gallo, Chivo"
print(mis3animales)

tresAñimales = "Perico, Gallo, Chivo"
print(tresAñimales)

#concatenacoón de strings

muchoTexto = "Mucho Texto"
pocoTexto = "Poco Texto"

print(muchoTexto + " " + pocoTexto)

#str() int() float()

edad = 20
print("La edad del usuario es: " + str(edad))
print("El tipo de dato edad es: " + str(type(edad)))

import math

grados = 45.0
radianes = grados * math.pi / 180.0
seno = math.sin(radianes)
print("Seno de 45º: " + str(seno))

def saludar(nommbre): 
    print("Hola " + nommbre)
    print("¿Cómo estás?")
    print("Te saludo de lejos por eso del virus papu")

def despedir():
    print("Ya me voy papu")
    print("Ya que pase todo esto nos besamos")
def concatenar(parte1, parte2):
    return parte1 + parte2

print("Esto no es parte de la función")

saludar("Carlos")
despedir()
frase = concatenar("Hola " , "Adiós")

print(frase)