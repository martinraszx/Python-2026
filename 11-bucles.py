from colorama import init,Fore
init() # Inicializando el paquete colorama 

print(Fore.YELLOW + "==== Bucles ====")

#bucles while
edad = 15
num = 0

while edad > 18:
    print("Eres menor de edad, no puedes manejar")

from colorama import init, Fore
init()

edad = 15
num = 0

#while edad > 18:
#    print("Eres menor de edad, no puedes manejar")

#while True:
#    print(num)
#    num = num + 2

while num <= 100:
    print(num)
    num = num + 2
print(Fore.GREEN + "Primer bucle terminado")

while num <= 200:
    print(num)
    num = num +2
else:
    print("Mi condición es mayor a 200")
print(Fore.CYAN + "segundo bucle terminado")

while num <= 300:
    print(num)
    num = num +2
    if num == 250:
        print("Mi  condición es igual a 250")
print(Fore.BLUE + "tercero bucle terminado")

while num <= 400:
    print(num)
    num += 2
    if num == 350:
        print(Fore.MAGENTA + "se detiene bucle")
        break
print(num)
print(Fore.MAGENTA + ("cuarto bucle terminado"))

num = 0
while num <= 50:
    num += 1 
    if num == 40:
        continue
    print(num)

'''
while True:
    parametro = input(">>> ingrese la palabra secreta: ")
    if parametro == "exit":
        break
    else:
        print(parametro)
'''

#bucle FOR
print(Fore.YELLOW + ("\n 1er buble for"))
for i in (1,2,3,4,5,6,7,8,9,10):
    print(Fore.GREEN + f"{i}")

print(Fore.RED + ("\n 2do buble for"))
listita = [1,2,3,4,5,6,7,8,9,10]
for i in (listita):
    print(i)

# iterand de una tercera forma (3 for)
print(Fore.BLUE + ("\n 3er buble for"))
for i in range(1,101):
    print(i)