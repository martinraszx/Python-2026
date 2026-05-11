#Datos númericos

#Numeros Enteros = int
edad = 18

#Nuemros Reales = float
estatura = 1.72


#numeros complejos
num_complejo = 4 + 2j        #primera forma de crear un numero complejo
otro_complejo = complex(4.2) #segunda forma de crear un numero complejo

print(num_complejo)
print(otro_complejo)

base = 8
altura = 12.5

area = (base * altura) / 2
print(f"El area del triangulo es de {area} cm")

#Salida de numeros en PI
PI = 3.141592653589793
print(f"El numero PI tiene un valor de {PI: .2f}")

#Formato de salida de Numeros

#Limitar a 4 decimales el valor de Pi
print(f"El valor de Pi es {Pi:.4f}") 

# El metodo de Redondeo
print(f"El area del triangulo es {round(area, 2)} cm")

#Cadena de textos (strings)

carrera= "Inginieria civil en Informatica"
institucion ="Universidad de los lagos"

print(carrera[0]) #Se muestra la primera letra de la variable carrera
print(carrera[-1]) #Se muestra la ultima letra de la variable carrera

print("hola" * 4) #Se repite la palabra hola 4 veces

print(len(institucion)) #Se muestra la cantidad de caracteres que tiene la variable institucion


#Arreglos

print(f"Arreglos (Listas)\n")
colores= ["Rojo", "Verde", "Azul", "Amarillo"]  #arreglo string
numeros= [1, 2, 3, 4, 5]                        #Arreglo numerico
lista_mixta= ["ola", 3.14159, 42, True]         #Arreglo mixto

print(colores[0])       #Se imprime el primer elemento de la lista
print(numeros[-1])      #Se imprime el ultimo elemento de la lista
print(lista_mixta)