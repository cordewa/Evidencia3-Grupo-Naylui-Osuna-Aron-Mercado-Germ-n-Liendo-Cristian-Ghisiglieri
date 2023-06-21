import mysql.connector

#conexion = mysql.connector.connect(
#    host = "BigBread",
#    port = 3306,
#    user = "root",
#    password = "Root123",
#)

#cursor = conexion.cursor()

#cursor.execute("SHOW DATABASES")
#for bd in cursor:
#    print(bd)

conexion = mysql.connector.connect(
    host = 'BigBread',
    port = 3306,
    user = 'root',
    password = 'Root123',
    db = 'db_big_bread'
    )

try:
    if conexion.is_connected():
        print("La conexion fue exitosa")

except:
    print("No se pudo conectar a la base de datos")

finally:
    if conexion.is_connected():
        conexion.close()
        print("La conexion fue cerrada")

class Conectar():

    def Insertar_Producto(self,idproducto,idcategoria,nombre,stock,precio,unid_medida,):
        conection = conexion.Conectar()
        try:
            cursor = conexion.Conectar.cursor()
            sentenciaSQL = "INSERT INTO Productos values(%s,%s,%s,%s,%s,%s)"
            data = (idproducto, idcategoria, nombre, stock, precio, unid_medida)
            cursor.execute(sentenciaSQL,data)
            cursor.conexion.commit()
            cursor.conexion.close()

        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conectar a la Base de Datos!", descripcionDelError)

    def Insertar_Insumos(self,idinsumo,nombre,stock,precio,):
        conection = conexion.Conectar()
        try:
            cursor = conexion.Conectar.cursor()
            sentenciaSQL = "INSERT INTO insumos values(%s,%s,%s,%s)"
            data = (idinsumo, nombre, stock, precio,)
            cursor.execute(sentenciaSQL,data)
            cursor.conexion.commit()
            cursor.conexion.close()

        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conectar a la Base de Datos!", descripcionDelError)

    def Insertar_Recetas(self,idreceta,nombre,idproducto,cant_producto,):
        conection = conexion.Conectar()
        try:
            cursor = conexion.Conectar.cursor()
            sentenciaSQL = "INSERT INTO recetas values(%s,%s,%s,%s)"
            data = (idreceta,nombre,idproducto,cant_producto,)
            cursor.execute(sentenciaSQL,data)
            cursor.conexion.commit()
            cursor.conexion.close()

        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conectar a la Base de Datos!", descripcionDelError)            

    def Insertar_Categorias(self,idcategoria,nombre,):
        conection = conexion.Conectar()
        try:
            cursor = conexion.Conectar.cursor()
            sentenciaSQL = "INSERT INTO categorias values(%s,%s)"
            data = (idcategoria,nombre,)
            cursor.execute(sentenciaSQL,data)
            cursor.conexion.commit()
            cursor.conexion.close()

        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conectar a la Base de Datos!", descripcionDelError)       
    
    def Insertar_Producciondiaria(self,idproduccion,idproducto,cantidad,fecha,):
        conection = conexion.Conectar()
        try:
            cursor = conexion.Conectar.cursor()
            sentenciaSQL = "INSERT INTO Produccion_diaria values(%s,%s,%s,%s)"
            data = (idproduccion,idproducto,cantidad,fecha)
            cursor.execute(sentenciaSQL,data)
            cursor.conexion.commit()
            cursor.conexion.close()

        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conectar a la Base de Datos!", descripcionDelError)    

    def Listado_Productos(self):
        conection = conexion.Conectar.cursor()
        try:
            cursor = conexion.Conectar.cursor()
            sentenciaSQL = "SELECT * FROM Productos"
            cursor.execute(sentenciaSQL)
            resultados = cursor.fetchall()
            cursor.conexion.close()
            return resultados
        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conectar a la Base de Datos!", descripcionDelError)

    def Listado_insumos(self):
        conection = conexion.Conectar.cursor()
        try:
            cursor = conexion.Conectar.cursor()
            sentenciaSQL = "SELECT * FROM Insumos"
            cursor.execute(sentenciaSQL)
            resultados = cursor.fetchall()
            cursor.conexion.close()
            return resultados        
        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conectar a la Base de Datos!", descripcionDelError)

    def Listado_Recetas(self):
        conection = conexion.Conectar.cursor()
        try:
            cursor = conexion.Conectar.cursor()
            sentenciaSQL = "SELECT * FROM Recetas"
            cursor.execute(sentenciaSQL)
            resultados = cursor.fetchall()
            cursor.conexion.close()
            return resultados       
        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conectar a la Base de Datos!", descripcionDelError)

    def Listado_Categorias(self):
        conection = conexion.Conectar.cursor()
        try:
            cursor = conexion.Conectar.cursor()
            sentenciaSQL = "SELECT * FROM Categorias"
            cursor.execute(sentenciaSQL)
            resultados = cursor.fetchall()
            cursor.conexion.close()
            return resultados               
        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conectar a la Base de Datos!", descripcionDelError)

    def Listado_Producciondiaria(self):
        conection = conexion.Conectar.cursor()
        try:
            cursor = conexion.Conectar.cursor()
            sentenciaSQL = "SELECT * FROM Produccion_diaria"
            cursor.execute(sentenciaSQL)
            resultados = cursor.fetchall()
            cursor.conexion.close()
            return resultados               
        except mysql.connector.Error as descripcionDelError:
            print("¡Hubo un error al intentar conectar a la Base de Datos!", descripcionDelError)

            