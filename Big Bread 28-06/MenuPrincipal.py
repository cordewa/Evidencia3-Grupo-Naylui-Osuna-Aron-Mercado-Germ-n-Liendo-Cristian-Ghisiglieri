from ConexionMenu import Conectar
import Controlador

def menuPrincipal():
    continuar = True  #Variable continuar
    while(continuar):
        opcionCorrecta = False  #Variable opcionCorrecta
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
                except Exception as descripcionError:
                    print("Hubo un ERROR...", descripcionError)
            elif opcion == 2:
                try:
                    menuEditar()
                except Exception as descripcionError:
                    print("Hubo un ERROR...", descripcionError)
            elif opcion == 3:
                try:
                    menuEliminar()
                except Exception as descripcionError:
                    print("Hubo un ERROR...", descripcionError)
            elif opcion == 4:
                try:
                    menuListar()
                except Exception as descripcionError:
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
                #insumo = None
                try:
                    #conectar.insertInsumo(insumo)
                    Controlador.crearInsumos()  
                except Exception as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 2:
                try:
                    Controlador.crearProductos  
                except Exception as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 3:
                try:
                    Controlador.crearRecetas()  
                except Exception as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 4:
                try:
                    Controlador.crearCategorias()  
                except Exception as descripcionError:
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
                except Exception as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 2:
                try:
                    Controlador.editarProductos()  
                except Exception as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 3:
                try:
                    Controlador.editarRecetas()  
                except Exception as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 4:
                try:
                    Controlador.editarCategorias()  
                except Exception as descripcionError:
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
                except Exception as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 2:
                try:
                    Controlador.eliminarProductos()  
                except Exception as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 3:
                try:
                    Controlador.eliminarRecetas()  
                except Exception as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 4:
                try:
                    Controlador.eliminarCategorias()  
                except Exception as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 5:
                continuar = False
                menuPrincipal()
                break   # VER SI ES NECESARIO QUE ESTE EL BREAK
            else:
                print("Opción incorrecta!")

def menuListar():
    conectar = Conectar()
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
                    insumo = conectar.selectInsumo()
                    if len(insumo)>0:
                        Controlador.listarInsumos(insumo)
                    else:
                        print("NO se encontraron Insumos.")
                except Exception as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 2:
                try:
                    Controlador.listarProductos()  
                except Exception as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 3:
                try:
                    Controlador.listarRecetas()  
                except Exception as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 4:
                try:
                    Controlador.listarCategorias()  
                except Exception as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 5:
                try:
                    Controlador.listarProd_Diaria()  
                except Exception as descripcionError:
                    print("Hubo un Error...", descripcionError)
            elif opcion == 6:
                continuar = False
                menuPrincipal()
                break   # VER SI ES NECESARIO QUE ESTE EL BREAK
            else:
                print("Opción incorrecta!")

menuPrincipal()