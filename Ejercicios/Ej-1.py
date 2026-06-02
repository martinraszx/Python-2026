"""Un centro de investigación de la Región de Los Lagos registró las
temperaturas de los primeros 3 días de la semana en una lista. Crea un
programa en Python que calcule el promedio de la semana y la
diferencia entre el día más alto y el más bajo usando operaciones de
listas."""

temperaturas = [12.5, 14.2, 11.8]
print(f"El promedio de la semana es: {sum(temperaturas) / len(temperaturas):.3}")
print(f"La diferencia entre el día más alto y el más bajo es: {max(temperaturas) - min(temperaturas):.2}")