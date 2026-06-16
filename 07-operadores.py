#Operadores en Python
a = 10
b = 5
c = 4
d = 10

print("=== OPERADORES ARITMETICOS ===")
print(f"La suma entre la variable a y b es: (a + b)") #operador de suma
print(f"La resta entre la variable a y b es: (a - b)") #operador de resta
print(f"La multiplicaión entre la variable a y b es: {a * b}") #operador de producto
print(f"La división entre la variable a y b es {a / b}") #operador de división
print(f"El módulo entre la variable a y b es: (a % b)") #operador de módulo
print(f"El coeficiente entre la variable b y c es: (b // c)") #operador de división entera
print(f"El resultado de b elevado a c (5^4): {b ** c}") #operador de potencia -> pow() hace lo mismo

print("Hola" * ((int(10*2) / 5)), "\n")

print(a == b) # op igualdad
print(a != b) # op desigualdad, distinto o diferente
print(a > b) # op mayor que
print(a < b) # op menor que
print(a >= b) # mayor o igual que
print(a <= b) # menor o igual que

bencina = False
encendido = True
edad = 19

#Usando el op AND
if bencina and encendido:
    print("El vehiculo puede arrancar")
else:
    print("El vehiculo no puede arrancar")

#Usando el op OR
if bencina or encendido:
    print("El vehiculo puede arrancar")
else:
    print("El vehiculo no puede arrancar")


if not bencina and encendido:
    print("El vehiculo puede arrancar")
else:
    print("El vehiculo no puede arrancar")

if (not bencina or encendido) or (encendido and edad >= 8):
    print("El vehiculo puede arrancar")
else:
    print("El vehiculo no puede arrancar")