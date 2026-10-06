"""El Departamento de Informática de la Universidad de Los Lagos está monitoreando el consumo de
memoria RAM (en Gigabytes) de uno de sus servidores principales de bases de datos. Se han
registrado los consumos exactos en 4 instantes del día (Mañana, Mediodía, Tarde y Noche) dentro
de una lista de Python.

Escribe un programa en Python que realice las siguientes tareas utilizando exclusivamente lo
aprendido hasta el momento en la Unidad II:

1.Ingresar por terminal los 4 consumos del día y guardarlo en una lista con valores de tipo
decimal (float).

2.Acceder a cada valor individualmente utilizando la indexación de listas para guardarlos en
variables independientes.

3.Calcule y muestre el consumo promedio de RAM del servidor durante el día.

4.Calcule y muestre el 'Rango de Operación' (la diferencia entre el consumo máximo y el mínimo
detectado) haciendo uso de las funciones integradas de Python vistas en clases.

Mañana
Medio dia
Tarde
Noche

"""

consumos = []
tiempo = ["Mañana", "Medio dia", "Tarde", "Noche"]
bucle = 0
i = 1

consumos.append(float(input(f"Ingrese el uso de ram acorde al tiempo, {tiempo[bucle]} ")))
consumos.append(float(input(f"Ingrese el uso de ram acorde al tiempo, {tiempo[bucle]} ")))
consumos.append(float(input(f"Ingrese el uso de ram acorde al tiempo, {tiempo[bucle]} ")))
consumos.append(float(input(f"Ingrese el uso de ram acorde al tiempo, {tiempo[bucle]} ")))

ram_manana = consumos[0]
ram_medio_dia = consumos[1]
ram_tarde = consumos[2]
ram_noche = consumos[3]

print(f"El promedio de la semana es:{sum(consumos) / len(consumos)}")
print(f"El rango de deferencia de uso con el maximo y minimo es 12 {max(consumos) - min(consumos):.3}")
