#diccionarios

paciente = {
    'nombre':'Martin Aguirre',
    'edad':18,
    'ciudad':'castro',
    'fechas_atencion':[5,8,10],
    'diagnostico':('resfrio comun'),
    'informacion_extra':{
        'tipo_de_sangre':'B+',
        'hemograma':False,
    },
}

#segunda forma de declarar un diccionario
medico = dict(
    nombre = 'Martin Aguirre',
    edad = 18,
    especialidad = "Tecnico en comunicaciones",
)

print(type(paciente))
print(f"=== Ficha Paciente === \n{paciente}\n")
print(f"=== Ficha Paciente === \n{medico}\n")
print("===============================================================================================================")
#Consulta de informacion a diccionario

#Consulta solo un valor del diccionario sin traerlo completo

print(f"El nombre del paciente es {paciente['nombre']}")

print("===============================================================================================================")
#A difierencia  de [], este metodo no genera error si no eniste la clave
# Metodo get() obtiene el valor de una clave, si no existe retorna None (o un valor por )
print(paciente['nombre'])
print(paciente.get('rut','N/D (No Data)'))
print("===============================================================================================================")
#Retornar las claves, los valores o ambas como pares
print(paciente.keys())    
print(paciente.values())    
print(paciente.items())     
print("===============================================================================================================")
#Cuenta la cantidad de varialbe sque estan dentro
print(len(paciente))
print(len(medico))
print("===============================================================================================================")
#Modificacion del diccionario
#Agregar una clave nueva al diccionario paciente
paciente['telefono'] = '+56959160310'

print("=== Ficha Paciente === \n")
print(paciente)
print("===============================================================================================================")
#Sobreescribir valor de una clave existente (forma n°1)
paciente['edad'] = 20

print("=== Ficha Paciente === \n")
print(paciente)
print("===============================================================================================================")
#funciona otro diccionario (o pares clave valor) en el actual
#util para actualizar varios campos a la vez (actualizar varias claves)

paciente.update({'edad' : 21, 'ciudad':'castro'})
print(paciente['edad'])
print(paciente['ciudad'])
print(paciente)
print("===============================================================================================================")
del(paciente['informacion_extra'])
print(paciente)
print("===============================================================================================================")
#Elimina una clave y retorna su valor (a diferencia del del, que no lo retorna) -> pop()
edad_eliminada = paciente.pop('edad')
print(paciente)
print("===============================================================================================================")
#Otras utilidades

#Con in se verifica si una clave existe en el diccionario (sin usar condicionales todavia)
print('nombre' in paciente)
print('rut' in paciente)
print("="*40)
#Con copy() se crea una copia indipendiente del diccionario
paciente2 = paciente.copy()
paciente2['nombre'] = 'Javiera'
print(paciente['nombre'])
print(paciente2['nombre'])
print(paciente2)

#Con clear() elimina todaos los elementos del diccionario, dejando vacio (a diferencia del)
medico2 = medico.copy()
print("\n ======= Diccionario copia (Medico) \n" )
print(medico2)
medico2.clear()
print(medico2)