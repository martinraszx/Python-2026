#creando una tupla tipo string
estudiantes = ("Germán", "Benjamín", "Felipe", "Martín")
print(type(estudiantes))
print(estudiantes)
print(f"Tupla: {[estudiantes]}")
#creando una tupla coompleja con datos estructurados
datos = ([1, 2, 3, 4, 5], ("Queilen", "Castro"), ("Universidad de Los Lagos", "AIEP"))

#tambien se puede consultar la posición de un elemento al igual que la lista
print(datos[0])
print(datos)

#con las listas se puede eliminar elementos
lista_asignaturas = ["Programación", "Química", "Introducción a la Matemáticas"]
print(f"LISTA: {[lista_asignaturas]}")

lista_asignaturas.pop()
print(f"Lista con ultimo elemento eliminado: {[lista_asignaturas]}")

print(estudiantes.index("Martín"))

print(sorted(estudiantes)) 