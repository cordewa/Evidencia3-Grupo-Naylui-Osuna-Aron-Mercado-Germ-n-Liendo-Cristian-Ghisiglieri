import Conexion

class Productos():
    IdProducto = 0,
    IdCategoria = 0,
    Nombre = "",
    Stock = 0,
    Precio = 0,
    Unid_Medida = ""

    #METODO CONSTRUCTOR
    def __init__(self, id_producto, id_categoria, nombre, stock, precio, unidad_medida):
        self.IdProducto = id_producto
        self.IdCategoria = id_categoria
        self.Nombre = nombre
        self.Stock = stock
        self.Precio = precio
        self.Unid_Medida = unidad_medida
