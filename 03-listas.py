#Listas

#Primera forma de Declaracion de Lista Mixta
lista1=["martin",18,True,4,"victor"]
ramos = []#nada

#Segunda forma de Declaracion de Lista Numerica
n=list([1,4,3,6,5,0,8])

#Metodo para las listas
#01- COUNT()- cuenta el numero de veces que se repite un elemento en la lista
print(lista1.count("martin"))

print(ramos)

#agregar un elemento al final de la lista
ramos.append("quimica")
print(ramos)

ramos.append("programacion")
print(ramos)

ramos.append("introduccion a la matematicas")
print(ramos)

#modificar el nombre de un elemento de una lista
ramos[1] = "progamacion basica"

print(ramos)

#otra forma
ramos.insert(1, "habilidades comunicativas")

print(ramos)

#eliminar elemento de la lista
ramos.pop(3)

print(ramos)

#ordenar la lista
ramos.sort()
print(ramos)

n.sort()
print(n)

#ordenar cor caracteres

ramos.sort(key=len)
print(ramos)

#extension
ramos_semestre = ["intro a la fisica", "algebra", "ciudadania"]
print(ramos_semestre)

ramos.extend(ramos_semestre)

print(ramos)