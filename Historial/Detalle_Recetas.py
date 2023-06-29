import Conexion

class Detalle_Recetas():
    IdDet_Receta = 0,
    IdReceta = 0,
    IdInsumo = 0,
    Cant_Insumo = 0,
    Unid_Medida = ""

    #METODO CONSTRUCTOR
    def __init__(self, id_det_receta, id_receta, id_insumo, cantidad_insumo, unidad_medida):
        self.IdDet_Receta = id_det_receta
        self.IdReceta = id_receta
        self.IdInsumo = id_insumo
        self.Cant_Insumo = cantidad_insumo
        self.Unid_Medida = unidad_medida
