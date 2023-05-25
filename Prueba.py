opc = 0
opc2 = 0

carillas = 250000
implantes = 475000
ortodoncia = 800000

cantCar = 0
cantImp = 0
cantOrt = 0

desc = 0
subtotal = 0
total = 0

trab = 0



while opc!=3:
    print("\n-------- El Diente de Oro --------")
    print("[1] Cotización")
    print("[2] Renunciar")
    print("[3] Salir\n")

    while True:
        try: 
            opc = int(input("Ingresa una opción: "))
            if 1<= opc <=3:
                break
            else:
                print("Opción fuera de rango\n")
        except:
            print("Ingresa una opción válida\n")

    if opc == 1:

        while trab == 0:
            print("\n¿Qué tipo de trabajador eres?")
            print("[1] Trabajador Auxiliar")
            print("[2] Trabajador Administrativo")
            print("[3] Trabajador Docente")
            print("[4] Otro\n")
            while True:
                try: 
                    trab = int(input("Ingresa una opción: "))
                    if 1<= trab <=4:
                        break
                    else:
                        print("Opción fuera de rango\n")
                except:
                    print("Ingresa una opción válida\n")
            if trab == 1:
                desc = 0.15
                print("Tu descuento es del 15%")
            elif trab == 2:
                desc = 0.10
                print("Tu descuento es del 10%")
            elif trab == 3:
                desc = 0.05
                print("Tu descuento es del 5%")
            else:
                desc = 0
                print("No tienes descuento ):")

        while True:
            print("\n-------- Tratamientos --------")
            print("[1] Carillas Porcelana - Precio $250.000")
            print("[2] Implantes Dentales - Precio $475.000")
            print("[3] Ortodoncia Brackets - Precio $800.000")
            print("[4] Ver total")
            print("[5] Volver al Menú principal\n")
            while True:
                try: 
                    opc2 = int(input("Elige una opción: "))
                    if 1<= opc2 <=5:
                        break
                    else:
                        print("Opción fuera de rango\n")
                except:
                    print("Ingresa una opción válida\n")
            if opc2 == 1:
                print("\nCarillas Porcelana")
                while True:
                    try:
                        cant = int(input("¿Cuántos tratamientos desea cotizar?: "))
                        if cant > 0:
                            cantCar += cant
                            break
                        else:
                            print("Ingresa un valor mayor a 0")
                    except:
                        print("Ingresa un valor numérico")

            elif opc2 == 2:
                print("\nImplantes Dentales")
                while True:
                    try:
                        cant = int(input("¿Cuántos tratamientos desea cotizar?: "))
                        if cant > 0:
                            cantImp += cant
                            break
                        else:
                            print("Ingresa un valor mayor a 0")
                    except:
                        print("Ingresa un valor numérico")
                
            elif opc2 == 3:
                print("\nOrtodoncia Brackets")
                while True:
                    try:
                        cant = int(input("¿Cuántos tratamientos desea cotizar?: "))
                        if cant > 0:
                            cantOrt += cant
                            break
                        else:
                            print("Ingresa un valor mayor a 0")
                    except:
                        print("Ingresa un valor numérico")
                
            elif opc2 == 4:
                subtotal = ((cantCar * carillas) + (cantImp * implantes) + (cantOrt * ortodoncia)) 
                total = (subtotal - (subtotal * desc)) 
                print("-"*30)
                print(" "* 9, "Cotización")
                print("-"*30)
                if cantCar == 0 and cantImp == 0 and cantOrt == 0:
                    print("No has cotizado tratamientos")
                if cantCar > 0:
                    print(f"--> {cantCar} tratamiento(s) Carillas Porcelana   ${cantCar * carillas}")
                if cantImp > 0:
                    print(f"--> {cantImp} tratamiento(s) Implantes Dentales   ${cantImp * implantes}")
                if cantOrt > 0:
                    print(f"--> {cantOrt} tratamiento(s) Ortodoncia Brackets  ${cantOrt * ortodoncia}")
                print("-"*30)
                print(f"Subtotal                  ${subtotal}")
                print(f"Descuento {round(100*desc)}%            ${round(subtotal * desc)}")
                print("-"*30)
                print(f"Total                     ${round(total)}")
                print("-"*30)
                print(f"Son 12 cuotas de:     ${round(total/12)}")
                print("")
                print("Sonría Bonito!!!")
            else:
                break

    elif opc == 2:
        trab = 0
        cantCar = 0
        cantImp = 0
        cantOrt = 0
        print("\nCotización Eliminada\n")

            


    


