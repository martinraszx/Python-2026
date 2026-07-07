salida="--->>> "
while True:
    print("Seleccione un de los 3 ejrcicios")
    opcion=input(salida)
    match opcion:
        case "1":
            print("Porfavor a continuacion ingrese su Nombre")
            nombre=str(input(salida))
            print("Porfavor a continuacion ingrese su Apellido")
            apellido=str(input(salida))
            print("Ingrese su Edad")
            edad= int(input(salida))
            print("Ingrese su carrera")
            carrera=str(input(salida))
            print("Ingrese su altura en CM")
            altura=float(input(salida))
            print(f"El nombre es; {nombre} y el Apellido es; {apellido}")
            print(f"La edad es; {edad}")
            print(f"La carrera cursada actualmente es; {carrera}")
            print(f"Y la estatura es: {altura}cm")
        case "2":
            utiles_escolares=[]
            print("Ingrese a continuacion los utiles escolares")
            utiles=input(salida)
            utiles_escolares.append(utiles)
            utiles=input(salida)
            utiles_escolares.append(utiles)
            utiles=input(salida)
            utiles_escolares.append(utiles) 
            print(f"Primer útil escolar:{utiles_escolares[0]}")
            print(f"Segundo útil escolar: {utiles_escolares[1]}")
            print(f"Tercer Útil escolar: {utiles_escolares[2]}")
        case "3":
            print("Ingrese 5 notas a continuacion")
            i = 0
            mis_notas = []
            while True:
                notas=float(input(salida))
                mis_notas.append(notas)
                i += 1
                if i == 5 :
                    break
            print(f"La nota minima es {min(mis_notas)} y la nota maxima es {max(mis_notas)}")
            print(f"El promedio general es {sum(mis_notas)/len(mis_notas):.2}")
            print(f"La primera nota es: {mis_notas[0]}")
            print(f"La segunda nota es: {mis_notas[1]}")
            print(f"La tercera nota es:{mis_notas[2]}")
            print(f"La cuarta nota es: {mis_notas[3]}")
            print(f"La quinta nota es: {mis_notas[4]}")
        case "0" | "salir":
            print("Bai bai")
            break
        case _:
            print("error we")