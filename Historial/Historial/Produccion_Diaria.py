import Conexion

class Produccion_Diaria():
    IdProduccion = 0,
    IdProducto = 0,
    Cantidad = 0,
    Fecha = ""

    #METODO CONSTRUCTOR
    def __init__(self, id_produccion, id_producto, cantidad, fecha):
        self.IdProduccion = id_produccion
        self.IdProducto = id_producto
        self.Cantidad = cantidad
        self.Fecha = fecha
