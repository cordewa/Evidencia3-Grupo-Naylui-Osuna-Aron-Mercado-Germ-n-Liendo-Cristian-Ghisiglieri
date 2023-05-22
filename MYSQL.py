import mysql.connector

class Conectar_Base_de_Datos():
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = "localhost",
                port = "3306",
                user = "root",
                password = "36773827",
                db = "BD_EJEMPLO_INNOVA"
                
            )
        except mysql.connector.Error as descripcionError: 
            print("No se conecto la base de datos", descripcionError)
          
                
            
    





