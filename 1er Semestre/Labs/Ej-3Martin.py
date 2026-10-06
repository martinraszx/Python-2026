comunas_1 = []
comunas_2 = []
censo_2017 = {
    12 : dict(
        nombre_region = "Magallanes",
        superficie = 1382291,
        habitantes = 166533,
    ),
    14 : dict(
        nombre_region =  "Los rios",
        superficie = 18429,
        habitantes = 404432,
    ),
}
print("Id 12")
print(censo_2017[12])
print("Id 14")
print(censo_2017[14])
print("presione enter para continuar")
input("... ")

censo_2017[12]['densidad'] = (censo_2017[12]['superficie']/censo_2017[12]['habitantes'])
censo_2017[14]['densidad'] = (censo_2017[14]['superficie']/censo_2017[14]['habitantes'])

censo_2017[12]['capital'] = "Punta Arenas"
censo_2017[14]['capital'] = "Valdivia"

censo_2017[12]['comunas'] = comunas_1
comunas_1.append("Cabo de Hornos")
comunas_1.append("Puerto Williams")
comunas_1.append("Porvenir")

censo_2017[14]['comunas'] = comunas_2
comunas_2.append("Rio Bueno")
comunas_2.append("La Union")
comunas_2.append("Paillaco")

censo_2017[12]['coordenadas_simuladas'] = -39.8, -73.2
censo_2017[14]['coordenadas_simuladas'] = 39.8, 73.2

censo_2017[12]['zonas_exclusivas'] = set.__str__("Urbana "+"Rural "+"Fronterisa")
censo_2017[14]['zonas_exclusivas'] = set.__str__("Poco Acceso "+"camprestre "+"nieve")

censo_2017[12]['nombre_region'] = "Magallanes y Antartica Chilena"

while True:
    print("===========================================================")
    print("Escriba el id de la region que quiere revisar")
    print("Escriba el numero 0 o la palabra para salir para salir")
    opcion = str(input("Ingrese un id valido para esta oprecaion... "))
    match opcion:
        case "12":
            print(censo_2017[12]['comunas'])
        case "14":
            print(censo_2017[14]['comunas'])
        case "112":     #para testeo de que no se rompa
            print(censo_2017[12])
        case "114":     #para testeo de que no se rompa
            print(censo_2017[14])
        case "0" | "salir":

            print("Cerrando")
            break
        case _:
            print("opcion no valida o id desconocido")

print(f" para la id 12{censo_2017[12].keys,censo_2017[12].values}")
print(f" para la id 14{censo_2017[14].keys,censo_2017[14].values}")\







#codigo que no quise borrar por que me ayudo a terminar otras cosas y que me dio pereza borrar 

#densidad = censo_2017[12]['superficie']/censo_2017[12]['habitantes']
#print(f"La densidad de habitantes de la region de {censo_2017[12]['nombre_region']} {densidad:.2} Km2 por habiante")
#densidad = censo_2017[14]['superficie']/censo_2017[14]['habitantes']
#print(f"La densidad de habitantes de la region de {censo_2017[14]['nombre_region']} {densidad:.2} Km2 por habiante")

#censo_2017[12]['comunas'] = comunas_1.append["Cabo de Hornos","Puerto Williams","Porvenir"]
#censo_2017[14]['comunas'] = comunas_2.append["Rio Bueno","La Union","Paillaco"]

#censo_2017[12]['zonas_exclusivas'] = set("Urbana"+"Rural"+"Fronterisa")
#censo_2017[14]['zonas_exclusivas'] = set("Poco Acceso"+"camprestre"+"nieve"