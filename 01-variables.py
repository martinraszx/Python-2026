#Se añadieron mas opciones para mostrar en pantalla 
#Se definen las varialbes a usar
nombre = "Martin"
apellido = "Aguirre"
edad = "18"

"""
{} Llaves
() Parentesis
[] Llaves Cuadradas o Corchetes
"""

#El escribir las variables
#Forma uno de mostrar el contenido
print("Mi nombre y apellido es",nombre, apellido,"y mi edad es", edad)

#Forma dos para mostrar contenido
print(f"Mi nombre es {nombre} y mi apellido es {apellido} y mi edad es {edad}")

#Froma tres para mostrar contenido
print("Mi nombre es " + nombre + " y  mi apellido es "+ apellido + " y tengo "+ str(edad) + " edad")

carrera = str(input("¿Que carrera de estudios cursas?"))
print(f"Yo estudio {carrera}")