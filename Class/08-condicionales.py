from colorama import init,Fore
init() # Inicializando el paquete colorama 

print(Fore.MAGENTA + "======= utilizando IF y ELSE =======")

licencia = False
edad = 19
automovil = True

if licencia and edad >=18:
    print(Fore.YELLOW + "puede conducir un automovil ya que tine la edad y la licencia de conducir")
else:
    print(Fore.YELLOW + "no puede conducir un automovil por que no s mayor de edad y no tiene licencia")

if licencia and edad  >=18:
    print(Fore.CYAN + "puede conducir por que es mayor de edad, y tiene licencia")
elif automovil:
    print(Fore.BLUE + "tengo automovil, pero no tengo licencia ni la edad necesaria para conducir")
else:
    print(Fore.RED + "no puedo conducir, ya que no tengo la edad, ni licencia, in automovil")