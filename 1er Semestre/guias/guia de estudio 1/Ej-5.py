tiempos_respuesta = []
tiempos_respuesta.append(float(input("Ingrese el valor numero 1: ")))
tiempos_respuesta.append(float(input("Ingrese el valor numero 2: ")))
tiempos_respuesta.append(float(input("Ingrese el valor numero 3: ")))
vel_1 = tiempos_respuesta[0]
vel_2 = tiempos_respuesta[1]
vel_3 = tiempos_respuesta[2]

print(f"El valor mas alto es {max(tiempos_respuesta)} y el valor mas lento es {min(tiempos_respuesta)}")
print(f"La brecha de rendimiento es {max(tiempos_respuesta) - min(tiempos_respuesta)}")
print(tiempos_respuesta)