import mysql.connector

#conexion = mysql.connector.connect(
#    host = "localhost",
#    port = 3306,
#    user = "root",
#    password = "PcGc$121315!",
#)

#cursor = conexion.cursor()

#cursor.execute("SHOW DATABASES")
#for bd in cursor:
#    print(bd)

conexion = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'PcGc$121315!',
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