import Controlador

def menuPrincipal():
    continuar = True  
    while(continuar):
        opcionCorrecta = False  
        while(not opcionCorrecta):
            print("\n+-------------------------------------------+")
            print("|               Big Bread SA                |")
            print("+-------------------------------------------+\n")
            print("MENÚ PRINCIPAL\n")
            print("1 - CREAR")
            print("2 - EDITAR")
            print("3 - ELIMINAR")
            print("4 - LISTAR")
            print("5 - SALIR")
            print("\n")
            opcion = int(input("Seleccione una opción:"))

            if opcion < 1 or opcion > 5:
                print("\nOpción incorrecta, ingrese nuevamente...")

            elif opcion == 1:
                try:
                    menuCrear()
                except ValueError as descripcionError:
                    print("Hubo un ERROR...", descripcionError)
            elif opcion == 2:
                try:
                    menuEditar()
                except ValueError as descripcionError:
                    print("Hubo un ERROR...", descripcionError)
            elif opcion == 3:
                try:
                    menuEliminar()
                except ValueError as descripcionError:
                    print("Hubo un ERROR...", descripcionError)
            elif opcion == 4:
                try:
                    menuListar()
                except ValueError as descripcionError:
                    print("Hubo un ERROR...", descripcionError)
            elif opcion == 5:
                continuar = False
                print("Gracias por utilizar nuestro sistema.")
                #menuPrincipal()
                break
            else:
                print("Opción incorrecta!")
                #menuPrincipal()
        
def menuCrear():
    continuar = True  #Variable continuar
    while(continuar):
        opcionCorrecta = False  #Variable opcionCorrecta
        while(not opcionCorrecta):
            print("+------------------------------+")
            print("1 - CREAR INSUMO")
            print("2 - CREAR PRODUCTO")
            print("3 - CREAR RECETA")
            print("4 - CREAR CATEGORIA")
            print("5 - VOLVER AL MENÚ")
            print("\n")
            opcion = int(input("Seleccione la opción a realizar:"))

            if opcion < 1 or opcion > 5:
                print("\nOpción incorrecta, ingrese nuevamente...")
            elif opcion == 1:
                try:
                    Controlador.crearInsumos()  
                except ValueError as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 2:
                try:
                    print("Funciona crearProductos")
                    #controlador.crearProductos()  
                except ValueError as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 3:
                try:
                    print("Funciona crearRecetas")
                    #controlador.crearRecetas()  
                except ValueError as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 4:
                try:
                    print("Funciona crearCategorias")
                    #controlador.crearCategorias()  
                except ValueError as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 5:
                continuar = False
                menuPrincipal()
                break   # VER SI ES NECESARIO QUE ESTE EL BREAK
            else:
                print("Opción incorrecta!")

def menuEditar():
    continuar = True  #Variable continuar
    while(continuar):
        opcionCorrecta = False  #Variable opcionCorrecta
        while(not opcionCorrecta):
            print("+------------------------------+")
            print("1 - EDITAR INSUMO")
            print("2 - EDITAR PRODUCTO")
            print("3 - EDITAR RECETA")
            print("4 - EDITAR CATEGORIA")
            print("5 - VOLVER AL MENÚ")
            print("\n")
            opcion = int(input("Seleccione la opción a realizar:"))

            if opcion < 1 or opcion > 5:
                print("\nOpción incorrecta, ingrese nuevamente...")
            elif opcion == 1:
                try:
                    Controlador.editarInsumos()  
                except ValueError as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 2:
                try:
                    print("Funciona editarProductos")
                    #controlador.editarProductos()  
                except ValueError as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 3:
                try:
                    print("Funciona editarRecetas")
                    #controlador.editarRecetas()  
                except ValueError as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 4:
                try:
                    print("Funciona editarCategorias")
                    #controlador.editarCategorias()  
                except ValueError as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 5:
                continuar = False
                menuPrincipal()
                break   # VER SI ES NECESARIO QUE ESTE EL BREAK
            else:
                print("Opción incorrecta!")

def menuEliminar():
    continuar = True  #Variable continuar
    while(continuar):
        opcionCorrecta = False  #Variable opcionCorrecta
        while(not opcionCorrecta):
            print("+------------------------------+")
            print("1 - ELIMINAR INSUMO")
            print("2 - ELIMINAR PRODUCTO")
            print("3 - ELIMINAR RECETA")
            print("4 - ELIMINAR CATEGORIA")
            print("5 - VOLVER AL MENÚ")
            print("\n")
            opcion = int(input("Seleccione la opción a realizar:"))

            if opcion < 1 or opcion > 5:
                print("\nOpción incorrecta, ingrese nuevamente...")
            elif opcion == 1:
                try:
                    Controlador.eliminarInsumos()  
                except ValueError as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 2:
                try:
                    print("Funciona eliminarProductos")
                    #controlador.eliminarProductos()  
                except ValueError as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 3:
                try:
                    print("Funciona eliminarRecetas")
                    #controlador.eliminarRecetas()  
                except ValueError as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 4:
                try:
                    print("Funciona eliminarCategorias")
                    #controlador.eliminarCategorias()  
                except ValueError as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 5:
                continuar = False
                menuPrincipal()
                break   # VER SI ES NECESARIO QUE ESTE EL BREAK
            else:
                print("Opción incorrecta!")

def menuListar():
    continuar = True  #Variable continuar
    while(continuar):
        opcionCorrecta = False  #Variable opcionCorrecta
        while(not opcionCorrecta):
            print("+------------------------------+")
            print("1 - LISTAR INSUMO")
            print("2 - LISTAR PRODUCTO")
            print("3 - LISTAR RECETA")
            print("4 - LISTAR CATEGORIA")
            print("5 - LISTAR PRODUCCION DIARIA")
            print("6 - VOLVER AL MENÚ")
            print("\n")
            opcion = int(input("Seleccione la opción a realizar:"))

            if opcion < 1 or opcion > 6:
                print("\nOpción incorrecta, ingrese nuevamente...")
            elif opcion == 1:
                try:
                    Controlador.listarInsumos()  
                except ValueError as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 2:
                try:
                    print("Funciona listarProductos")
                    #controlador.listarProductos()  
                except ValueError as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 3:
                try:
                    print("Funciona listarRecetas")
                    #controlador.listarRecetas()  
                except ValueError as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 4:
                try:
                    print("Funciona listarCategorias")
                    #controlador.listarCategorias()  
                except ValueError as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 5:
                try:
                    print("Funciona listarProd_Diaria")
                    #controlador.listarProd_Diaria()  
                except ValueError as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 6:
                continuar = False
                menuPrincipal()
                break   # VER SI ES NECESARIO QUE ESTE EL BREAK
            else:
                print("Opción incorrecta!")

menuPrincipal()
