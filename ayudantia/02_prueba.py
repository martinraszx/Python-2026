#Ejercicio 1
i=0
productos = ["Pan", "Leche", "Pan","Queso", "Leche","Jugo", "Pan"]
print(f"La cantidadd productos sin descontar los repetidos {len(productos)}")
rem_prd=set(productos)
print(f"La cantidadde prductos sin repetir {len(rem_prd)}")
for i in rem_prd:
    print(i)
if "Jugo" in rem_prd:
    print("fue vendido")
else:
    print("aun esta en venta")