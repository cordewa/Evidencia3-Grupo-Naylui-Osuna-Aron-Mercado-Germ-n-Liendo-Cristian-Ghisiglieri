from ConexionMenu import Conectar
import Controlador

conectar = Conectar()

def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("\n+-------------------------------------------+")
            print("|               Big Bread SA                |")
            print("+-------------------------------------------+\n")
            print("MENÚ PRINCIPAL\n")
            print("1 - LISTAR")
            print("2 - CREAR")
            print("3 - EDITAR")
            print("4 - ELIMINAR")
            print("5 - SALIR")
            print("\n")
            opcion = int(input("Seleccione una opción:"))

            if opcion < 1 or opcion > 5:
                print("\nOpción incorrecta, ingrese nuevamente...")

            elif opcion == 1:
                try:
                    menuListar()
                except Exception as descripcionError:
                    print("Hubo un ERROR al seleccionar el Menú LISTAR...", descripcionError)

            elif opcion == 2:
                try:
                    menuCrear()
                except Exception as descripcionError:
                    print("Hubo un ERROR al seleccionar el Menú CREAR...", descripcionError)

            elif opcion == 3:
                try:
                    menuEditar()
                except Exception as descripcionError:
                    print("Hubo un ERROR al seleccionar el Menú EDITAR...", descripcionError)

            elif opcion == 4:
                try:
                    menuEliminar()
                except Exception as descripcionError:
                    print("Hubo un ERROR al seleccionar el Menú ELIMINAR...", descripcionError)

            elif opcion == 5:
                continuar = False
                print("Gracias por utilizar nuestro sistema.")
                #menuPrincipal()
                break

            else:
                print("Opción incorrecta!")
                #menuPrincipal()

def menuListar():
    continuar = True
    while(continuar):
        opcionCorrecta = False
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
                        Controlador.listarInsumos()
                    else:
                        print("NO se encontraron Insumos.")

                except Exception as descripcionError:
                    print("Hubo un Error al intentar LISTAR un Insumo...", descripcionError)

            elif opcion == 2:
                try:
                    producto = conectar.selectProducto()
                    if len(producto or [])>0:
                        Controlador.listarProductos()
                    else:
                        print("NO se encontraron Productos.")

                except Exception as descripcionError:
                    print("Hubo un Error al intentar LISTAR un Producto...", descripcionError)

            elif opcion == 3:
                try:
                    receta = conectar.selectReceta()
                    if len(receta or [])>0:
                        Controlador.listarRecetas()
                    else:
                        print("NO se encontraron Recetas.")

                except Exception as descripcionError:
                    print("Hubo un Error al intentar LISTAR una Receta...", descripcionError)

            elif opcion == 4:
                try:
                    categoria = conectar.selectCategoria()
                    if len(categoria or [])>0:
                        Controlador.listarCategorias()
                    else:
                        print("NO se encontraron Categorías.")

                except Exception as descripcionError:
                    print("Hubo un Error al intentar LISTAR una Categoría...", descripcionError)

            elif opcion == 5:
                try:
                    prod_diaria = conectar.selectProd_Diaria()
                    if len(prod_diaria or [])>0:
                        Controlador.listarProd_Diarias()
                    else:
                        print("NO se encontraron Producciones Diarias.")

                except Exception as descripcionError:
                    print("Hubo un Error al intentar LISTAR las Producciones Diarias...", descripcionError)

            elif opcion == 6:
                continuar = False
                #menuPrincipal()
                break   # VER SI ES NECESARIO QUE ESTE EL BREAK
            
            else:
                print("Opción incorrecta!")

def menuCrear():
    continuar = True
    while(continuar):
        opcionCorrecta = False
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
                    insumo = Controlador.crearInsumos()
                    if insumo is not None:
                        conectar.insertInsumo(insumo)

                except Exception as descripcionError:
                    print("Hubo un Error al intentar CREAR un Insumo...", descripcionError)

            elif opcion == 2:
                try:
                    producto = Controlador.crearProductos()
                    if producto is not None:
                        conectar.insertProducto(producto)

                except Exception as descripcionError:
                    print("Hubo un Error al intentar CREAR un Producto...", descripcionError)

            elif opcion == 3:
                try:
                    receta = Controlador.crearRecetas()
                    if receta is not None:
                        conectar.insertReceta(receta)

                except Exception as descripcionError:
                    print("Hubo un Error al intentar CREAR una Receta...", descripcionError)

            elif opcion == 4:
                try:
                    categoria = Controlador.crearCategorias()
                    if categoria is not None:
                        conectar.insertCategoria(categoria)

                except Exception as descripcionError:
                    print("Hubo un Error al intentar CREAR una Categoría...", descripcionError)

            elif opcion == 5:
                continuar = False
                #menuPrincipal()
                break   # VER SI ES NECESARIO QUE ESTE EL BREAK

            else:
                print("Opción incorrecta!")

def menuEditar():
    continuar = True
    while(continuar):
        opcionCorrecta = False
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
                    insumoUpdateInput = Controlador.getInsumoUpdateInput()
                    if insumoUpdateInput is not None:
                        conectar.updateInsumo(insumoUpdateInput)

                except Exception as descripcionError:
                    print("Hubo un Error al intentar EDITAR un Insumo...", descripcionError)

            elif opcion == 2:
                try:
                    productoUpdateInput = Controlador.getProductoUpdateInput()
                    if productoUpdateInput is not None:
                        conectar.updateProducto(productoUpdateInput)

                except Exception as descripcionError:
                    print("Hubo un Error al intentar EDITAR un Producto...", descripcionError)

            elif opcion == 3:
                try:
                    recetaInput = Controlador.getRecetaUpdateInput()
                    if recetaInput is not None:
                        conectar.updateReceta(recetaInput)

                except Exception as descripcionError:
                    print("Hubo un Error al intentar EDITAR una Receta...", descripcionError)

            elif opcion == 4:
                try:
                    categoriaInput = Controlador.getCategoriaUpdateInput()
                    if categoriaInput is not None:
                        conectar.updateCategoria(categoriaInput)

                except Exception as descripcionError:
                    print("Hubo un Error al intentar EDITAR una Categoría...", descripcionError)

            elif opcion == 5:
                continuar = False
                #menuPrincipal()
                break   # VER SI ES NECESARIO QUE ESTE EL BREAK

            else:
                print("Opción incorrecta!")

def menuEliminar():
    continuar = True
    while(continuar):
        opcionCorrecta = False
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
                    insumoDeleteInput = Controlador.getInsumoDeleteInput()
                    if insumoDeleteInput is not None:
                        conectar.deleteInsumo(insumoDeleteInput)
                    else:
                        print("No se encontro el insumo")

                except Exception as descripcionError:
                    print("Hubo un Error al intentar ELIMINAR un Insumo...", descripcionError)

            elif opcion == 2:
                try:
                    productoDeleteInput = Controlador.getProductoDeleteInput()
                    if productoDeleteInput is not None:
                        conectar.deleteProducto(productoDeleteInput)

                except Exception as descripcionError:
                    print("Hubo un Error al intentar ELIMINAR un Producto...", descripcionError)

            elif opcion == 3:
                try:
                    recetaDeleteInput = Controlador.getRecetaDeleteInput()
                    if recetaDeleteInput is not None:
                        conectar.deleteReceta(recetaDeleteInput)

                except Exception as descripcionError:
                    print("Hubo un Error al intentar ELIMINAR una Receta...", descripcionError)

            elif opcion == 4:
                try:
                    categoriaDeleteInput = Controlador.getCategoriaDeleteInput()
                    if categoriaDeleteInput is not None:
                        conectar.deleteCategoria(categoriaDeleteInput)

                except Exception as descripcionError:
                    print("Hubo un Error al intentar ELIMINAR una Categoría...", descripcionError)

            elif opcion == 5:
                continuar = False
                #menuPrincipal()
                break   # VER SI ES NECESARIO QUE ESTE EL BREAK

            else:
                print("Opción incorrecta!")

menuPrincipal()
