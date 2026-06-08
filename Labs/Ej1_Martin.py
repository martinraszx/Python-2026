registro_lluvia = []
print("A continuacion ingrese la medicion de las muestras ")
registro_lluvia.append(float(input("Muestra numero 1: ")))
registro_lluvia.append(float(input("Muestra numero 2: ")))
registro_lluvia.append(float(input("Muestra nuemro 3: ")))
registro_lluvia.append(float(input("Muestra nuemro 4: ")))
registro_lluvia.append(float(input("MUestra numero 5: ")))

mm1 = registro_lluvia[0]
mm2 = registro_lluvia[1]
mm3 = registro_lluvia[2]
mm4 = registro_lluvia[3]
mm5 = registro_lluvia[4]

print(f"El registro de la lluvia durante el dia fueron estos: {registro_lluvia}")
print(f"El minimo que a llovido a sido de {min(registro_lluvia)}mm y el maximo que a llovido a sido de {max(registro_lluvia)}mm")
print(f"El promedio fue de: {sum(registro_lluvia) / len(registro_lluvia)}mm")
print(f"La brecha de la lluvia entre la medicion mas grande y pequeña a sido de {max(registro_lluvia)- min(registro_lluvia)}mm")