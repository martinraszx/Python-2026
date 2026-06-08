while True:
    print("El 1 es para una variable pre establecida que es  ´ __ICiNF-2026_ula___ ´")
    print("EL 2 es para ingresar una variable")
    seleccion = int(input("... "))
    if seleccion == 1:
        sys_viejo = " __ICiNF-2026_ula___ "
        sys_nuevo = sys_viejo.strip()
        sys_nuevo = sys_nuevo.replace("_","")
        print(f"Quedaria con los cambios ya hecho asi: {sys_nuevo.upper()} y el lagor seria de {len(sys_nuevo)}")
        break
    if seleccion == 2:
        print("Ingrese la matricula del sistema viejo")
        sys_ingresado = str(input("... "))

        sys_nuevo = sys_ingresado.strip()
        sys_nuevo = sys_nuevo.replace("_","")
        print(f"Quedaria con los cambios ya hecho asi: {sys_nuevo.upper()} y el lagor seria de {len(sys_nuevo)}")
        break