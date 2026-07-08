print("Menu")
print("simplede 1 al 3")
print("9 para salir")

while True:
    opcion= str(input("Porfavor, elija una opcion de 1 al 3... "))
    match opcion:
        case "1":
            print("eleccion 1")
        case "2":
            print("eleccion 2")
        case "3":
            print("eleccion 3") 
        case "9":
            print("se rompio we")
            break
        case _:
            print("opcin no valida we")

#Match para ver el tiempo del mes
mes = int(input("Ingrese el numero de una fecha del mes... "))
match mes:
    case 12 | 1 | 2:
        print("verano")
    case 3 | 4 | 5:
        print("otono")
    case 6 | 7 | 8:
        print("invierno")
    case 9 | 10 | 11:
        print("primavera")
    case _:
        print("opcion no valida")

#Saludo segun la hora
hora = int(input("Ingrese la hora en formato 24 horas... "))
match hora:
    case h if 0 <= h < 6:
        print("ya es de madrugada we")
    case h if 6 <= h < 12:
        print("Buenos dias")
    case h if 12 <= h < 18:
        print("Buenas tardes")
    case h if 18 <= h < 24:
        print("Buenas noches")
    case _:
        print("opcion no valida")

x = [1,2,3]
match x:
    case [a, b ,c]:#deasgrupando valores de la lista x
        print(f"Elementos de la lista x: {a}, {b}, {c}")

        
datos = {
    'nombre':'martin',
    'edad': 18
}

match datos:
    case {'nombres':n, 'edad':e}:
        print(f"nombre: {n}, edad: {e}")

#saver si un numero es par o impar
valor = 6
match valor:
    case x if x % 2 == 0:
        print(f"{valor} es un numero par")
    case x if x % 2 != 0:
        print(f"{valor} es un numero impar")