salida = "--> "
total = 0
notas = {
    "Ana": 6.2,
    "Luis": 4.8,
    "Pedro": 3.9,
    "Sofía": 5.5
}
for i in notas:
    if notas[i] >= 4.0:
        total  =total +1
        print(f"{i} {notas[i]} {salida}aprobado")
    else:
        print(f"{i} {notas[i]} {salida}reprobado")
print(f"El total de aprobados es: {total}")