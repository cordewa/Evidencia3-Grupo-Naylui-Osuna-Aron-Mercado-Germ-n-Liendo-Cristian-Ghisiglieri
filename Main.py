import Conexion as conexionDB

print("*** BIENVENIDO A LA CALCULADORA BIG BREAD S.A.***")
print("¿Quiere ingresar un producto?")
print("Para ingresar un producto, ingrese 1")
ingresaProducto = int(input())
if ingresaProducto == 1:
    print("Ingrese el nombre del producto")
    nombreProducto = input()

    conexionDB.Conectar.Insertar_Producto()
