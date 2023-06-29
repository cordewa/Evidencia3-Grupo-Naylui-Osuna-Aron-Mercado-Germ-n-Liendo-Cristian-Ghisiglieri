import ConexionMenu

#INSUMOS
def listarInsumos(insumo):
    print("LIstado de INSUMOS:\n")
    #con = ConexionMenu.Conectar()
    #listado = con.selectInsumo()
    #print("\n|   ID   |     NOMBRE INSUMO     |   STOCK   |   PRECIO   |  UNIDAD DE MEDIDA  |")
    for ins in insumo:
        datos = "ID: {0} | Nombre: {1} | Stock: {2} | Precio: $ {3} | Unid. de Medida: {4}"
        print(datos.format(ins[0], ins[1], ins[2],ins[3],ins[4]))
    input("\nPresione ENTER para continuar.")

"""
ORIGINAL
def listarInsumos():
    con = ConexionMenu.Conectar()
    listado = con.selectInsumo()
    print("\n|   ID   |     NOMBRE INSUMO     |   STOCK   |   PRECIO   |  UNIDAD DE MEDIDA  |")
    for insumo in listado:
        print("   ",insumo[0],"\t",str(insumo[1]),"\t\t",insumo[2],"\t\t $",insumo[3],"\t\t",str(insumo[4]))
    input("\nPresione ENTER para continuar.")
"""
def crearInsumos():
    con = ConexionMenu.Conectar()

    nombre_insumo = input("\nIngrese el nombre del Insumo: ")
    stock_insumo = int(input("\nIngrese el stock del Insumo: "))
    precio_insumo = int(input("\nIngrese el precio del Insumo: $"))
    unidad_medida = input("\nIngrese la Unidad de Medida del Insumo: ")

    insumo = ConexionMenu.Insumo(0,nombre_insumo,stock_insumo,precio_insumo,unidad_medida)

    con.insertInsumo(insumo)
    input("\nPresione ENTER para continuar.")


def editarInsumos():
    con = ConexionMenu.Conectar()
    insumo = listado
    listado = con.selectInsAco(insumo)
    print("\n|   ID   |     NOMBRE INSUMO     |")
    for insumo in listado:
        print("   ",insumo[0],"\t",str(insumo[1]))
        if insumo:
            existe = False
            editar = int(input("Ingrese el ID INSUMO a editar: "))
    for id_ins in listado:
        if id_ins == editar:
            existe = True
            break

    if existe:
        nombre_insumo = input("\nIngrese el nombre del Insumo a actualizar: ")
        stock_insumo = int(input("\nIngrese el stock del Insumo a actualizar: "))
        precio_insumo = int(input("\nIngrese el precio del Insumo a actualizar: "))
        unidad_medida = input("\nIngrese la Unidad de Medida del Insumo: ")

        insumo = ConexionMenu.Insumo(0,nombre_insumo,stock_insumo,precio_insumo,unidad_medida)

        con.updateInsumo(insumo)
        input("\nPresione ENTER para continuar.")

    else:
        insumo = None
    return insumo


"""def editarInsumos():
    con = ConexionMenu.Conectar()
    listarInsumos()
    listado = con.selectInsumo()
    existe = False
    editar = int(input("Ingrese el ID INSUMO a editar: "))
    for id_ins in listado:
        if id_ins == editar:
            existe = True
            break

    if existe:
        nombre_insumo = input("\nIngrese el nombre del Insumo a actualizar: ")
        stock_insumo = int(input("\nIngrese el stock del Insumo a actualizar: "))
        precio_insumo = int(input("\nIngrese el precio del Insumo a actualizar: "))
        unidad_medida = input("\nIngrese la Unidad de Medida del Insumo: ")

        insumo = ConexionMenu.Insumo(0,nombre_insumo,stock_insumo,precio_insumo,unidad_medida)

        con.updateInsumo(insumo)
        input("\nPresione ENTER para continuar.")

    else:
        insumo = None
    return insumo"""


def eliminarInsumos():
    con = ConexionMenu.Conectar()
    listarInsumos()
    listado = con.selectInsumo()
    existe = False
    eliminar = int(input("Ingrese el ID de INSUMO a eliminar: "))
    for id_ins in listado:
        if id_ins == eliminar:
            existe = True
            break

    if existe:
        con.deleteInsumo()
        eliminar = ""
    return eliminar
    

#CATEGORIAS
def listarCategorias():
    con = ConexionMenu.Conectar()
    listado = con.selectCategoria()
    print("\n|   ID   |     NOMBRE CATEGORIA     |")
    for categoria in listado:
        print("   ",categoria[0],"\t",str(categoria[1]))
    input("\nPresione ENTER para continuar.")


def crearCategorias():
    con = ConexionMenu.Conectar()

    nombre_categoria = input("\nIngrese el nombre de la Categoria: ")

    categoria = ConexionMenu.Categoria(0,nombre_categoria)

    con.insertCategoria(categoria)
    input("\nPresione ENTER para continuar.")


def editarCategorias():
    con = ConexionMenu.Conectar()
    listarCategorias()
    listado = con.selectCategoria()
    existe = False
    editar = int(input("Ingrese el ID CATEGORIA a editar: "))
    for id_cat in listado:
        if id_cat == editar:
            existe = True
            break

    if existe:
        nombre_categoria = input("\nIngrese el nombre de la Categoria a actualizar: ")

        categoria = ConexionMenu.Categoria(0,nombre_categoria)

        con.updateCcategoria(categoria)
        input("\nPresione ENTER para continuar.")

    else:
        categoria = None
    return categoria


def eliminarCategorias():
    con = ConexionMenu.Conectar()
    listarCategorias()
    listado = con.selectCategoria()
    existe = False
    eliminar = int(input("Ingrese el ID de la Categoría a eliminar: "))
    for id_cat in listado:
        if id_cat == eliminar:
            existe = True
            break

    if existe:
        con.deleteCategoria()
        eliminar = ""
    return eliminar


#PRODUCTOS
def listarProductos():
    con = ConexionMenu.Conectar()
    listado = con.selectProducto()
    print("\n| ID PRODCUTO | ID CATEGORIA |     NOMBRE PRODUCTO     |   STOCK   |   PRECIO   |  UNIDAD DE MEDIDA  |")
    for producto in listado:
        print("   ",producto[0],"\t",producto[1],"\t",str(producto[2]),"\t\t",producto[3],"\t\t $",producto[4],"\t\t",str(producto[5]))
    input("\nPresione ENTER para continuar.")


def crearProductos():
    con = ConexionMenu.Conectar()

    nombre_producto = input("\nIngrese el nombre del Producto: ")
    stock_producto = int(input("\nIngrese el stock del Producto: "))
    precio_producto = int(input("\nIngrese el precio del Producto: $"))
    unidad_medida = input("\nIngrese la Unidad de Medida del Producto: ")

    producto = ConexionMenu.Producto(0,0,nombre_producto,stock_producto,precio_producto,unidad_medida)

    con.insertProducto(producto)
    input("\nPresione ENTER para continuar.")


def editarProductos():
    con = ConexionMenu.Conectar()
    listarProductos()
    listado = con.selectProducto()
    existe = False
    editar = int(input("Ingrese el ID PRODUCTO a editar: "))
    for id_prod in listado:
        if id_prod == editar:
            existe = True
            break

    if existe:
        nombre_producto = input("\nIngrese el nombre del Producto a actualizar: ")
        stock_producto = int(input("\nIngrese el stock del Producto a actualizar: "))
        precio_producto = int(input("\nIngrese el precio del Producto a actualizar: "))
        unidad_medida = input("\nIngrese la Unidad de Medida del Producto: ")

        producto = ConexionMenu.Producto(0,0,nombre_producto,stock_producto,precio_producto,unidad_medida)

        con.updateProducto(producto)
        input("\nPresione ENTER para continuar.")

    else:
        producto = None
    return producto


def eliminarProductos():
    con = ConexionMenu.Conectar()
    listarProductos()
    listado = con.selectProducto()
    existe = False
    eliminar = int(input("Ingrese el ID PRODUCTO a eliminar: "))
    for id_prod in listado:
        if id_prod == eliminar:
            existe = True
            break

    if existe:
        con.deleteProducto()
        eliminar = ""
    return eliminar


#RECETAS
def listarRecetas():
    con = ConexionMenu.Conectar()
    listado = con.selectReceta()
    print("\n| ID RECETA |     NOMBRE RECETA     | ID PRODUCTO |   CANT. PROD.   | UNIDAD DE MEDIDA |")
    for receta in listado:
        print("   ",receta[0],"\t",str(receta[1]),"\t\t",receta[2],"\t",receta[3],"\t\t",str(receta[4]))
    input("\nPresione ENTER para continuar.")


def crearRecetas():
    con = ConexionMenu.Conectar()

    nombre_receta = input("\nIngrese el nombre de la Receta: ")
    cant_producto = int(input("\nIngrese la cantidad del Producto: "))
    unidad_medida = input("\nIngrese la Unidad de Medida del Producto: ")

    receta = ConexionMenu.Receta(0,nombre_receta,0,cant_producto,unidad_medida)

    con.insertReceta(receta)
    input("\nPresione ENTER para continuar.")


def editarRecetas():
    con = ConexionMenu.Conectar()
    listarRecetas()
    listado = con.selectReceta()
    existe = False
    editar = int(input("Ingrese el ID RECETA a editar: "))
    for id_rec in listado:
        if id_rec == editar:
            existe = True
            break

    if existe:
        nombre_receta = input("\nIngrese el nombre de la Receta a actualizar: ")
        cant_producto = int(input("\nIngrese la cantidad de Producto a actualizar: "))
        unidad_medida = input("\nIngrese la Unidad de Medida del Producto: ")

        receta = ConexionMenu.Receta(0,nombre_receta,0,cant_producto,unidad_medida)

        con.updateReceta(receta)
        input("\nPresione ENTER para continuar.")

    else:
        receta = None
    return receta


def eliminarRecetas():
    con = ConexionMenu.Conectar()
    listarRecetas()
    listado = con.selectReceta()
    existe = False
    eliminar = int(input("Ingrese el ID RECETA a eliminar: "))
    for id_rec in listado:
        if id_rec == eliminar:
            existe = True
            break

    if existe:
        con.deleteReceta()
        eliminar = ""
    return eliminar


#PRODUCCION DIARIA
def listarProd_Diarias():
    con = ConexionMenu.Conectar()
    listado = con.selectProd_Diaria()
    print("\n| ID PRODUCCION | ID PRODUCTO |   CANTIDAD   |   FECHA   |")
    for produccion in listado:
        print("   ",produccion[0],"\t",produccion[1],"\t",produccion[2],"\t",str(produccion[3]))
    input("\nPresione ENTER para continuar.")


def crearProd_Diarias():
    con = ConexionMenu.Conectar()

    cantidad = int(input("\nIngrese la cantidad de la Producción: "))
    fecha = input("\nIngrese la Fecha de la Producción: ")

    prod_diaria = ConexionMenu.Prod_Diaria(0,0,cantidad,fecha)

    con.insertProd_Diaria(prod_diaria)
    input("\nPresione ENTER para continuar.")