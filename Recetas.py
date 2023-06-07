import Conexion

class Recetas():
    IdReceta = 0,
    Nombre = "",
    IdProducto = 0,
    Cant_Producto = 0

    #METODO CONSTRUCTOR
    def __init__(self, id_receta, nombre, id_producto, cantidad_producto):
        self.IdReceta = id_receta
        self.Nombre = nombre
        self.IdProducto = id_producto
        self.Cant_Producto = cantidad_producto