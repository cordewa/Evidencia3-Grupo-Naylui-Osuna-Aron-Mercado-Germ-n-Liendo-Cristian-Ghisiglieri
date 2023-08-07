import mysql.connector

class Conectar():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = 'PcGc$121315!',
                db = 'db_big_bread'
            )
        except mysql.connector.Error as descripcionError:
            print("Error durante la conexión.", descripcionError)

#LISTAR
    def selectInsumo(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM Insumos"
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                cursor.close()
                return resultados
            
            except Exception as descripcionError:
                print("Error SQL al LISTAR los Insumos.",descripcionError)


    def selectCategoria(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM Categorias"
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                cursor.close()
                return resultados
            
            except Exception as descripcionError:
                print("Error SQL al LISTAR las Categorías.",descripcionError)


    def selectProducto(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT p.idproducto, c.nombre, p.nombre, p.stock, p.precio, p.unidad_medida FROM Productos p JOIN Categorias c ON (p.idcategoria = c.idcategoria)"
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                cursor.close()
                return resultados
            
            except Exception as descripcionError:
                print("Error SQL al LISTAR los Productos.",descripcionError)


    def selectReceta(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT r.idreceta, r.nombre, p.nombre, r.cant_producto, p.unidad_medida FROM Recetas r JOIN Productos p ON (r.idproducto = p.idproducto)" #"SELECT * FROM Recetas"
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                cursor.close()
                return resultados
            
            except Exception as descripcionError:
                print("Error SQL al LISTAR las Recetas.",descripcionError)


    def selectDet_Receta(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM Detalle_Recetas"
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                cursor.close()
                return resultados
            
            except Exception as descripcionError:
                print("Error SQL al LISTAR los Detalles de Recetas.",descripcionError)


    def selectProd_Diaria(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * FROM Produccion_Diaria"
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                cursor.close()
                return resultados
            
            except Exception as descripcionError:
                print("Error SQL al LISTAR la Producción Diaria.",descripcionError)

# INSERTAR / CREAR
    def insertInsumo(self,insumo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT INTO Insumos (IdInsumo, Nombre, Stock, Precio, Unidad_Medida) VALUES (null,%s,%s,%s,%s)"

                data = (insumo.getnombre_insumo(),
                        insumo.getstock_insumo(),
                        insumo.getprecio_insumo(),
                        insumo.getunidad_medida())
                
                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                cursor.close()
                print("Insumo creado correctamente.")

            except Exception as descripcionError:
                print("Error SQL al CREAR un Insumo.",descripcionError)


    def insertCategoria(self,categoria):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT INTO Categorias (IdCategoria, Nombre) VALUES (null,%s)"

                data = (categoria.getnombre_categoria(),)

                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                cursor.close()
                print("Categoria creada correctamente.")

            except Exception as descripcionError:
                print("Error SQL al CREAR una Categoría.",descripcionError)


    def insertProducto(self,producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT INTO Productos (IdProducto, IdCategoria, Nombre, Stock, Precio, Unidad_Medida) VALUES (null,%s,%s,%s,%s,%s)"

                data = (producto.getid_categoria(),
                        producto.getnombre_producto(),
                        producto.getstock_producto(),
                        producto.getprecio_producto(),
                        producto.getunidad_medida(),)
                
                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                cursor.close()
                print("Producto creado correctamente.")

            except Exception as descripcionError:
                print("Error SQL al CREAR un Producto.",descripcionError)

# Acá hay que rehacer "insertReceta"! Estamos solicitando los productos, en vez de los INSUMOS para generar un PRODUCTO.
# Además, hay que permitir ingresar varios INSUMOS para CREAR el Producto! Es decir, debería de hacer un bucle al finalizar
# la carga de cada INSUMO (con un mensaje: "Desea ingresar un NUEVO Insumo?")

# En realidad, hay que ver cómo se vincula con el DetalleReceta! El DetalleReceta es el que nos tendría que permitir
# ingresar varios INSUMOS
    def insertReceta(self,receta):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT INTO Recetas (IdReceta, Nombre, IdProducto, Cant_Producto, Unidad_Medida) VALUES (null,%s,%s,%s,%s)"

                data = (receta.getnombre_receta(),
                        receta.getid_producto(),
                        receta.getcant_producto(),
                        receta.getunidad_medida(),)
                
                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                cursor.close()
                print("Receta creada correctamente.")

            except Exception as descripcionError:
                print("Error SQL al CREAR una Receta.",descripcionError)

# El código de "insertDet_Receta" esta MAL. Todavía falta desarrollar y vincular a RECETAS.
    def insertDet_Receta(self,det_receta):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT INTO Detalle_Recetas (IdDet_Receta, IdReceta, IdInsumo, Cant_Insumo, Unidad_Medida) VALUES (null,null,null,%s,%s)"

                data = (det_receta.getcant_insumo(),
                        det_receta.getunidad_medida())
                
                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                cursor.close()
                print("Detalle Receta creado correctamente.")

            except Exception as descripcionError:
                print("Error SQL al CREAR un Detalle de Receta.",descripcionError)


    def insertProd_Diaria(self,prod_diaria):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "INSERT INTO Produccion_Diaria (IdProduccion, IdProducto, Cantidad, Fecha) VALUES (null,%s,%s,%s)"

                data = (prod_diaria.getid_producto(),
                        prod_diaria.getcantidad(),
                        prod_diaria.getfecha(),)
                
                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                cursor.close()
                print("Produccion Diaria creada correctamente.")

            except Exception as descripcionError:
                print("Error SQL al CREAR una Producción Diaria.",descripcionError)

#EDITAR
    def updateInsumo(self, insumoInput):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "UPDATE Insumos SET Nombre = %s, Stock = %s, Precio = %s, Unidad_Medida = %s WHERE idInsumo = %s"

                data = (insumoInput.getnombre_insumo(),
                        insumoInput.getstock_insumo(),
                        insumoInput.getprecio_insumo(),
                        insumoInput.getunidad_medida(),
                        insumoInput.getid_insumo(),)
                
                cursor.execute(sentenciaSQL, data)
                self.conexion.commit()
                cursor.close()
                print("Insumo editado correctamente.")

            except Exception as descripcionError:
                print("Error SQL al EDITAR un Insumo.",descripcionError)


    def updateCategoria(self,categoria):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "UPDATE Categorias SET Nombre = %s WHERE idCategoria = %s"

                data = (categoria.getnombre_categoria(),
                        categoria.getid_categoria(),)
                
                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                cursor.close()
                print("Categoria editada correctamente.")

            except Exception as descripcionError:
                print("Error SQL al EDITAR la Categoría.",descripcionError)


    def updateProducto(self,producto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "UPDATE Productos SET Nombre = %s, Stock = %s, Precio = %s, Unidad_Medida = %s WHERE idProducto = %s"

                data = (producto.getnombre_producto(),
                        producto.getstock_producto(),
                        producto.getprecio_producto(),
                        producto.getunidad_medida(),
                        producto.getid_producto(),)
                
                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                cursor.close()
                print("Producto editado correctamente.")

            except Exception as descripcionError:
                print("Error SQL al EDITAR el Producto.",descripcionError)


    def updateReceta(self,receta):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "UPDATE Recetas SET Nombre = %s, IdProducto = %s, Cant_Producto = %s, Unidad_Medida = %s WHERE idReceta = %s"

                data = (receta.getnombre_receta(),
                        receta.getid_producto(),
                        receta.getcant_producto(),
                        receta.getunidad_medida(),
                        receta.getid_receta(),)
                
                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                cursor.close()
                print("Receta editada correctamente.")

            except Exception as descripcionError:
                print("Error SQL al EDITAR la Receta.",descripcionError)


# El código de "updateDet_Receta" esta MAL. Todavía falta desarrollar y vincular a RECETAS.
    def updateDet_Receta(self,det_receta):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "UPDATE Detalle_Recetas SET IdReceta = %s, IdInsumo = %s, Cant_Insumo = %s, Unid_Medida = %s WHERE idDet_Receta = %s"

                data = (det_receta.getid_receta(),
                        det_receta.getid_insumo(),
                        det_receta.getcant_insumo(),
                        det_receta.getunidad_medida(),
                        det_receta.getid_detreceta(),)
                
                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                cursor.close()
                print("Detalle Receta editado correctamente.")

            except Exception as descripcionError:
                print("Error SQL al EDITAR el Detalle de la Receta.",descripcionError)

#ELIMINAR / BORRAR
    def deleteInsumo(self, insumoDeleteInput):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE from Insumos WHERE IdInsumo = %s"

                data = (insumoDeleteInput, )

                cursor.execute(sentenciaSQL, data)
                self.conexion.commit()
                cursor.close()
                print("Insumo eliminado correctamente.")

            except Exception as descripcionError:
                print("Error SQL al BORRAR el Insumo.",descripcionError)


    def deleteCategoria(self,categoriaDeleteInput):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE from Categorias WHERE IdCategoria = %s"

                data = (categoriaDeleteInput, )
                
                cursor.execute(sentenciaSQL, data)
                self.conexion.commit()
                cursor.close()
                print("Categoria eliminada correctamente.")

            except Exception as descripcionError:
                print("Error SQL al BORRAR la Categoría.",descripcionError)


    def deleteProducto(self,productoDeleteInput):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE from Productos WHERE IdProducto = %s"

                data = (productoDeleteInput,)
                
                cursor.execute(sentenciaSQL, data)
                self.conexion.commit()
                cursor.close()
                print("Producto eliminado correctamente.")

            except Exception as descripcionError:
                print("Error SQL al BORRAR el Producto.",descripcionError)


    def deleteReceta(self,recetaDeleteInput):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE from Recetas WHERE IdReceta = %s"

                data = (recetaDeleteInput, )
                
                cursor.execute(sentenciaSQL, data)
                self.conexion.commit()
                cursor.close()
                print("Receta eliminada correctamente.")

            except Exception as descripcionError:
                print("Error SQL al BORRAR la Receta.",descripcionError)


# El código de "deleteDet_Receta" esta MAL. Todavía falta desarrollar y vincular a RECETAS.
    def deleteDetReceta(self,det_recetaDeleteInput):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE from Detalle_Recetas WHERE IdDet_Receta = %s"

                data = (det_recetaDeleteInput, )
                
                cursor.execute(sentenciaSQL, data)
                self.conexion.commit()
                cursor.close()
                print("Detalle Receta eliminado correctamente.")

            except Exception as descripcionError:
                print("Error SQL al BORRAR el Detalle de la Receta.",descripcionError)


class Insumo():
    IdInsumo = 0
    Nombre = ""
    Stock = 0
    Precio = 0
    Unidad_Medida = ""

    def __init__(self,id_insumo,nombre_insumo,stock_insumo,precio_insumo,unidad_medida):
        self.id_insumo = id_insumo
        self.nombre_insumo = nombre_insumo
        self.stock_insumo = stock_insumo
        self.precio_insumo = precio_insumo
        self.unidad_medida = unidad_medida
    
    def getid_insumo(self):
        return self.id_insumo
    def getnombre_insumo(self):
        return self.nombre_insumo
    def getstock_insumo(self):
        return self.stock_insumo
    def getprecio_insumo(self):
        return self.precio_insumo
    def getunidad_medida(self):
        return self.unidad_medida
    
    def setid_insumo(self,id_insumo):
        self.id_insumo = id_insumo
    def setnombre_insumo(self,nombre_insumo):
        self.nombre_insumo = nombre_insumo
    def setstock_insumo(self,stock_insumo):
        self.stock_insumo = stock_insumo
    def setprecio_insumo(self,precio_insumo):
        self.precio_insumo = precio_insumo
    def setunidad_medida(self,unidad_medida):
        self.unidad_medida = unidad_medida


class Categoria():
    IdCategoria = 0
    Nombre = ""

    def __init__(self,id_categoria,nombre_categoria):
        self.id_categoria = id_categoria
        self.nombre_categoria = nombre_categoria
    
    def getid_categoria(self):
        return self.id_categoria
    def getnombre_categoria(self):
        return self.nombre_categoria
    
    def setid_categoria(self,id_categoria):
        self.id_categoria = id_categoria
    def setnombre_categoria(self,nombre_categoria):
        self.nombre_categoria = nombre_categoria


class Producto():
    IdProducto = 0
    IdCategoria = 0
    Nombre = ""
    Stock = 0
    Precio = 0
    Unidad_Medida = ""

    def __init__(self,id_producto,id_categoria,nombre_producto,stock_producto,precio_producto,unidad_medida):
        self.id_producto = id_producto
        self.id_categoria = id_categoria
        self.nombre_producto = nombre_producto
        self.stock_producto = stock_producto
        self.precio_producto = precio_producto
        self.unidad_medida = unidad_medida
    
    def getid_producto(self):
        return self.id_producto
    def getid_categoria(self):
        return self.id_categoria
    def getnombre_producto(self):
        return self.nombre_producto
    def getstock_producto(self):
        return self.stock_producto
    def getprecio_producto(self):
        return self.precio_producto
    def getunidad_medida(self):
        return self.unidad_medida
    
    def setid_producto(self,id_producto):
        self.id_producto = id_producto
    def setid_categoria(self,id_categoria):
        self.id_categoria = id_categoria
    def setnombre_producto(self,nombre_producto):
        self.nombre_producto = nombre_producto
    def setstock_producto(self,stock_producto):
        self.stock_producto = stock_producto
    def setprecio_producto(self,precio_producto):
        self.precio_prodcuto = precio_producto
    def setunidad_medida(self,unidad_medida):
        self.unidad_medida = unidad_medida


class Receta():
    IdReceta = 0
    Nombre = ""
    IdProducto = 0
    Cant_Producto = 0
    Unidad_Medida = ""

    def __init__(self,id_receta,nombre_receta,id_producto,cant_producto,unidad_medida):
        self.id_receta = id_receta
        self.nombre_receta = nombre_receta
        self.id_producto = id_producto
        self.cant_producto = cant_producto
        self.unidad_medida = unidad_medida
    
    def getid_receta(self):
        return self.id_receta
    def getnombre_receta(self):
        return self.nombre_receta
    def getid_producto(self):
        return self.id_producto
    def getcant_producto(self):
        return self.cant_producto
    def getunidad_medida(self):
        return self.unidad_medida
    
    def setid_receta(self,id_receta):
        self.id_receta = id_receta
    def setnombre_receta(self,nombre_receta):
        self.nombre_receta = nombre_receta
    def setid_producto(self,id_producto):
        self.id_producto = id_producto
    def setcant_producto(self,cant_producto):
        self.cant_producto = cant_producto
    def setunidad_medida(self,unidad_medida):
        self.unidad_medida = unidad_medida


class Det_Receta():
    IdDet_Receta = 0
    IdReceta = 0
    IdInsumo = 0
    Cant_Insumo = 0
    Unidad_Medida = ""

    def __init__(self,id_detreceta,id_receta,id_insumo,cant_insumo,unidad_medida):
        self.id_detreceta = id_detreceta
        self.id_receta = id_receta
        self.id_insumo = id_insumo
        self.cant_insumo = cant_insumo
        self.unidad_medida = unidad_medida
    
    def getid_detreceta(self):
        return self.id_detreceta
    def getid_receta(self):
        return self.id_receta
    def getid_insumo(self):
        return self.id_insumo
    def getcant_insumo(self):
        return self.cant_insumo
    def getunidad_medida(self):
        return self.unidad_medida
    
    def setid_detreceta(self,id_detreceta):
        self.id_detreceta = id_detreceta
    def setid_receta(self,id_receta):
        self.id_receta = id_receta
    def setid_insumo(self,id_insumo):
        self.id_insumo = id_insumo
    def setcant_insumo(self,cant_insumo):
        self.cant_insumo = cant_insumo
    def setunidad_medida(self,unidad_medida):
        self.unidad_medida = unidad_medida


class Prod_Diaria():
    IdProduccion = 0
    IdProducto = 0
    Cantidad = ""
    Fecha = ""

    def __init__(self,id_produccion,id_producto,cantidad,fecha):
        self.id_produccion = id_produccion
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.fecha = fecha
    
    def getid_productocion(self):
        return self.id_produccion
    def getid_producto(self):
        return self.id_producto
    def getcantidad(self):
        return self.cantidad
    def getfecha(self):
        return self.fecha
    
    def setid_produccion(self,id_produccion):
        self.id_produccion = id_produccion
    def setid_producto(self,id_producto):
        self.id_producto = id_producto
    def setcantidad(self,cantidad):
        self.cantidad = cantidad
    def setfecha(self,fecha):
        self.fecha = fecha
