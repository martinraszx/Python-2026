notas=[]
print("Ingrese las 3 notas")
print("dentro de 1 a 7")
ciclo = 0
while True:
    nota=float(input("... "))
    if nota >= 1.0 and nota <= 7.0:
        notas.append(nota)
        ciclo = ciclo + 1
        if ciclo == 3:
            break
    else:
        print("ingrese una nota valida")
promedio = notas[0]*0.4+notas[1]*0.4+notas[2]*0.2
print(f"Las notas calculadas son: {notas[0]*0.4:.2} siendo la primera, la segunda es: {notas[1]*0.4:.2} y la tercera es: {notas[2]*0.2:.2}")
print(f"El promedio ya calculado es {promedio:.2}")