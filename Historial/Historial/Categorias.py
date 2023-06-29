import Conexion

class Categorias():
    IdCategoria = 0,
    Nombre = ""

    #METODO CONSTRUCTOR
    def __init__(self, id_categoria, nombre):
        self.IdCategoria = id_categoria
        self.Nombre = nombre
