import Conexion

class Insumos():
    IdInsumo = 0,
    Nombre = "",
    Stock = 0,
    Precio = 0,2

    #METODO CONSTRUCTOR
    def __init__(self, id_insumo, nombre, stock, precio):
        self.IdInsumo = id_insumo
        self.Nombre = nombre
        self.Stock = stock
        self.Precio = precio
