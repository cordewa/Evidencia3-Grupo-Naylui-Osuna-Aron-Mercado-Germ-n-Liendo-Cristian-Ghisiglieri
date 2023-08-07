import ConexionMenu
con = ConexionMenu.Conectar()

#LISTAR
def listarInsumos():
    listado = con.selectInsumo()
    print("\n|   ID   |     NOMBRE INSUMO     |   STOCK   |   PRECIO   |  UNIDAD DE MEDIDA  |")
    for insumo in listado:
        print("   ",insumo[0],"\t|",str(insumo[1]),"\t|\t",insumo[2],"\t|\t $ ",insumo[3],"\t|\t",str(insumo[4]))
    input("\nPresione ENTER para continuar.")
    return listado

def listarCategorias():
    listado = con.selectCategoria()
    print("\n|   ID   |     NOMBRE CATEGORIA     |")
    for categoria in listado:
        print("   ",categoria[0],"\t",str(categoria[1]))
    input("\nPresione ENTER para continuar.")
    return listado

def listarProductos():
    listado = con.selectProducto()
    print("\n| ID PROD. |   CATEGORIA   |     NOMBRE PRODUCTO     |   STOCK   |   PRECIO   |  UNIDAD DE MEDIDA  |")
    for producto in listado:
        print("   ",producto[0],"\t\t",producto[1],"\t",str(producto[2]),"\t\t",producto[3],"\t\t $",producto[4],"\t\t",str(producto[5]))
    input("\nPresione ENTER para continuar.")
    return listado

def listarRecetas():
    listado = con.selectReceta()
    print("\n| ID RECETA |     NOMBRE RECETA     |   PRODUCTO   |   CANT. PROD.   | UNIDAD DE MEDIDA |")
    for receta in listado:
        print("   ",receta[0],"\t",str(receta[1]),"\t\t",receta[2],"\t",receta[3],"\t\t",str(receta[4]))
    input("\nPresione ENTER para continuar.")
    return listado

def listarProd_Diarias():
    listado = con.selectProd_Diaria()
    print("\n| ID PRODUCCION | ID PRODUCTO |   CANTIDAD   |   FECHA   |")
    for produccion in listado:
        print("   ",produccion[0],"\t",produccion[1],"\t",produccion[2],"\t",str(produccion[3]))
    input("\nPresione ENTER para continuar.")
    return listado

#CREAR / INSERTAR
def crearInsumos():
    nombre_insumo = input("\nIngrese el nombre del Insumo: ")
    stock_insumo = int(input("\nIngrese el stock del Insumo: "))
    precio_insumo = int(input("\nIngrese el precio del Insumo: $"))
    unidad_medida = input("\nIngrese la Unidad de Medida del Insumo: ")

    insumo = ConexionMenu.Insumo("",nombre_insumo,stock_insumo,precio_insumo,unidad_medida) #ver si va 0 ó "" al comienzo!!

    con.insertInsumo(insumo)
    input("\nPresione ENTER para continuar.")

def crearCategorias():
    nombre_categoria = input("\nIngrese el nombre de la Categoria: ")

    categoria = ConexionMenu.Categoria("",nombre_categoria) #ver si va 0 ó "" al comienzo!!

    con.insertCategoria(categoria)
    input("\nPresione ENTER para continuar.")

def crearProductos():
    nombre_producto = input("\nIngrese el nombre del Producto: ")
    listado = listarCategorias()
    existe = False
    id_categoria = int(input("Ingrese el ID CATEGORIA que desea asignar al Producto: "))
    for id_cat in listado:
        if id_cat[0] == id_categoria:
            existe = True
            break
    if not existe:
        return None

    stock_producto = int(input("\nIngrese el stock del Producto: "))
    precio_producto = int(input("\nIngrese el precio del Producto: $"))
    unidad_medida = input("\nIngrese la Unidad de Medida del Producto: ")

    producto = ConexionMenu.Producto("",id_categoria,nombre_producto,stock_producto,precio_producto,unidad_medida) #ver si va 0 ó "" al comienzo!!

    con.insertProducto(producto)
    input("\nPresione ENTER para continuar.")

def crearRecetas():
    nombre_receta = input("\nIngrese el nombre de la Receta: ")
    listado = listarProductos()
    existe = False
    id_producto = int(input("Ingrese el ID PRODUCTO que desea agregar: "))
    for id_cat in listado:
        if id_cat[0] == id_producto:
            existe = True
            break
    if not existe:
        return None
    cant_producto = int(input("\nIngrese la cantidad del Producto: "))
    unidad_medida = input("\nIngrese la Unidad de Medida del Producto: ")

    receta = ConexionMenu.Receta("",nombre_receta,id_producto,cant_producto,unidad_medida) #ver si va 0 ó "" al comienzo!!

    con.insertReceta(receta)
    input("\nPresione ENTER para continuar.")

def crearProd_Diarias():
    listado = listarProductos()
    existe = False
    id_producto = int(input("Ingrese el ID PRODUCTO que desea generar: "))
    for id_cat in listado:
        if id_cat[0] == id_producto:
            existe = True
            break
    if not existe:
        return None
    cantidad = int(input("\nIngrese la cantidad de la Producción: "))
    fecha = input("\nIngrese la Fecha de la Producción: ")

    prod_diaria = ConexionMenu.Prod_Diaria("",id_producto,cantidad,fecha) #ver si va 0 ó "" al comienzo!!

    con.insertProd_Diaria(prod_diaria)
    input("\nPresione ENTER para continuar.")

#EDITAR
def getInsumoUpdateInput():
    listado = listarInsumos()
    existe = False
    id_insumo = int(input("Ingrese el ID de INSUMO a editar: "))
    for id_ins in listado:
        if id_ins[0] == id_insumo:
            existe = True
            break

    if not existe:
        return None
    
    nombre_insumo = input("\nIngrese el nombre del Insumo a actualizar: ")
    stock_insumo = int(input("\nIngrese el stock del Insumo a actualizar: "))
    precio_insumo = int(input("\nIngrese el precio del Insumo a actualizar: "))
    unidad_medida = input("\nIngrese la Unidad de Medida del Insumo: ")

    insumoInput = ConexionMenu.Insumo(id_insumo, nombre_insumo, stock_insumo, precio_insumo, unidad_medida)
    #input("\nPresione ENTER para continuar.")
    return insumoInput

def getCategoriaUpdateInput():
    listado = listarCategorias()
    existe = False
    id_categoria = int(input("Ingrese el ID CATEGORIA a editar: "))
    for id_cat in listado:
        if id_cat[0] == id_categoria:
            existe = True
            break
    
    if not existe:
        return None

    nombre_categoria = input("\nIngrese el nombre de la Categoria a actualizar: ")

    categoriaInput = ConexionMenu.Categoria(id_categoria,nombre_categoria)
    #input("\nPresione ENTER para continuar.")
    return categoriaInput

def getProductoUpdateInput():
    listado = listarProductos()
    existe = False
    id_producto = int(input("Ingrese el ID PRODUCTO a editar: "))
    for id_prod in listado:
        if id_prod[0] == id_producto:
            existe = True
            break

    if not existe:
        return None

    nombre_producto = input("\nIngrese el nombre del Producto a actualizar: ")
    categoria_producto = input("\nIngrese el nombre de la Categoría del Producto a actualizar: ")
    stock_producto = int(input("\nIngrese el stock del Producto a actualizar: "))
    precio_producto = int(input("\nIngrese el precio del Producto a actualizar: "))
    unidad_medida = input("\nIngrese la Unidad de Medida del Producto: ")

    productoInput = ConexionMenu.Producto(id_producto,categoria_producto,nombre_producto,stock_producto,precio_producto,unidad_medida)
    #input("\nPresione ENTER para continuar.")
    return productoInput

def getRecetaUpdateInput():
    listado = listarRecetas()
    existe = False
    id_receta = int(input("Ingrese el ID RECETA a editar: "))
    for id_rec in listado:
        if id_rec[0] == id_receta:
            existe = True
            break

    if not existe:
        return None

    nombre_receta = input("\nIngrese el nombre de la Receta a actualizar: ")
    listado = listarProductos()
    existe = False
    id_producto = int(input("Ingrese el ID PRODUCTO a editar: "))
    for id_prod in listado:
        if id_prod[0] == id_producto:
            existe = True
            break

    if not existe:
        return None

    cant_producto = int(input("\nIngrese la cantidad de Producto a actualizar: "))
    unidad_medida = input("\nIngrese la Unidad de Medida del Producto: ")

    recetaInput = ConexionMenu.Receta(id_receta,nombre_receta,id_producto,cant_producto,unidad_medida) #falta definir el IdProducto marcado con 0 (cero). Ver si no trae problemas!!
    #input("\nPresione ENTER para continuar.")
    return recetaInput

#ELIMINAR
def getInsumoDeleteInput():
    listado = listarInsumos()
    existe = False
    id_insumo = int(input("Ingrese el ID de INSUMO a eliminar: "))
    for id_ins in listado:
        if id_ins[0] == id_insumo:
            existe = True
            break

    if existe:
        return id_insumo
    
    return

def getCategoriaDeleteInput():
    listado = listarCategorias()
    existe = False
    id_categoria = int(input("Ingrese el ID de la Categoría a eliminar: "))
    for id_cat in listado:
        if id_cat[0] == id_categoria:
            existe = True
            break

    if existe:
        return id_categoria
    
    return

def getProductoDeleteInput():
    listado = listarProductos()
    existe = False
    id_producto = int(input("Ingrese el ID PRODUCTO a eliminar: "))
    for id_prod in listado:
        if id_prod[0] == id_producto:
            existe = True
            break

    if existe:
        return id_producto
    
    return

def getRecetaDeleteInput():
    listado = listarRecetas()
    existe = False
    id_receta = int(input("Ingrese el ID RECETA a eliminar: "))
    for id_rec in listado:
        if id_rec[0] == id_receta:
            existe = True
            break

    if existe:
        return id_receta
    
    return
