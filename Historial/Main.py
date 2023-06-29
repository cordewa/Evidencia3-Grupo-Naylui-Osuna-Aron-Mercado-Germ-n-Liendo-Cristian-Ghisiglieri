import Conexion as conexionDB


while True:
    print("*** BIENVENIDO A BIG BREAD S.A.***")
    print("1 - ¿Quiere ingresar modificar o eliminar PRODUCTOS?")
    print("2 - ¿Quiere ingresar modificar o eliminar INSUMOS?")
    print("3 - ¿Quiere ingresar modificar o eliminar RECETAS?")
    print("4 - ¿Quiere ingresar modificar o eliminar CATEGORIAS?")
    print("5 - ¿Quiere ingresar modificar o eliminar PRODUCCION DIARIA?")
    print("6 - LISTADO DE PRODUCTOS")
    print("7 - LISTADO DE INSUMOS")
    print("8 - LISTADO DE RECETAS")
    print("9 - LISTADO DE CATEGORIAS")
    print("10 - LISTADO DE PRODUCCION DIARIA")    
    print("11 - SALIR")
    print("\n")
    opcion = int(input("Ingrese su opción: "))
  
    if opcion == 1:
        conexionDB.Insertar_Productos()
    elif opcion == 2:
        conexionDB.Insertar_Insumos()
    elif opcion == 3:
        conexionDB.Insertar_Recetas()
    elif opcion == 4:
        conexionDB.Insertar_Categorias()
    elif opcion == 5:
        conexionDB.Insertar_Producciondiaria()        
    elif opcion == 6:
        conexionDB.Listado_Productos()
    elif opcion == 7:
        conexionDB.Listado_Insumos()
    elif opcion == 8:
        conexionDB.Listado_Recetas()
    elif opcion == 9:
        conexionDB.Listado_Categorias()
    elif opcion == 10:
        conexionDB.Listado_Producciondiaria() 
    elif opcion == 11:                      
        break
    else:
        print("¡Opción incorrecta!")
        
