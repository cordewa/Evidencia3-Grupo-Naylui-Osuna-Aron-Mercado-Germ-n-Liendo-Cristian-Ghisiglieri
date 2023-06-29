CREATE database DB_BIG_BREAD;

USE DB_BIG_BREAD;
CREATE TABLE Insumos(
	IdInsumo int(6) PRIMARY KEY NOT NULL auto_increment,
	Nombre varchar(30) not null,
	Stock int(10) not null,
	Precio int(12) not null,
    Unidad_Medida varchar(20) not null);
    
CREATE TABLE Categorias(
	IdCategoria int(6) PRIMARY KEY not null auto_increment,
	Nombre varchar(30) not null);
    
CREATE TABLE Productos(
	IdProducto int(6) PRIMARY KEY not null auto_increment,
    IdCategoria int(6) not null,
	Nombre varchar(30) not null,
    Stock int(10) not null,
	Precio int(12) not null,
    Unidad_Medida varchar(20) not null,
    foreign key (IdCategoria) references Categorias (IdCategoria));
    
CREATE TABLE Recetas(
	IdReceta int(6) PRIMARY KEY not null auto_increment,
	Nombre varchar(30) not null,
    IdProducto int(6) not null,
	Cant_Producto int(10) not null,
    Unidad_Medida varchar(20) not null,
    foreign key (IdProducto) references Productos (IdProducto));
    
CREATE TABLE Detalle_Recetas(
	IdDet_Receta INT(6) PRIMARY KEY NOT NULL AUTO_INCREMENT,
	IdReceta INT(6) NOT NULL,
    IdInsumo INT(6) NOT NULL,
    Cant_Insumo INT (11) NOT NULL,
	Unid_Medida VARCHAR(25) NOT NULL,
    foreign key (IdReceta) references Recetas (IdReceta),
    foreign key (IdInsumo) references Insumos (IdInsumo));
    
CREATE TABLE Produccion_Diaria(
	IdProduccion INT(6) PRIMARY KEY NOT NULL AUTO_INCREMENT,
	IdProducto INT(6) NOT NULL,
    Cantidad INT (11) NOT NULL,
	Fecha DATE NOT NULL,
    foreign key (IdProducto) references Productos (IdProducto));
    
INSERT INTO DB_BIG_BREAD.Insumos(IdInsumo,Nombre,Stock,Precio,Unidad_Medida) 
VALUES(default,'Harina de Trigo',10000,250,'Kg'),
(default,'Agua',4000,100,'Lts'),
(default,'Sal',100,100,'Kg'),
(default,'Azucar',2500,500,'Kg'),
(default,'Levadura Fresca',250,600,'Kg'),
(default,'Grasa Vacuna',200,1000,'Kg'),
(default,'Manteca',300,500,'Kg'),
(default,'Huevos',400,65,'Unid'),
(default,'Leche',100,350,'Lts'),
(default,'Fécula de Maiz',100,450,'Kg'),
(default,'Dulce de Leche',50,750,'Kg'),
(default,'Dulce de Membrillo',80,600,'Kg'),
(default,'Crema Pastelera',50,700,'Kg');

INSERT INTO DB_BIG_BREAD.Categorias(IdCategoria,Nombre) 
VALUES(default,'Criollos'),
(default,'Facturas'),
(default,'Panes');

INSERT INTO DB_BIG_BREAD.Productos(IdProducto,IdCategoria,Nombre,Stock,Precio,Unidad_Medida) 
VALUES(default,1,'Criollo común',50,600,'Kg'),
(default,1,'Criollo de hojaldre',30,650,'Kg'),
(default,1,'Criollo de manteca',20,700,'Kg'),
(default,2,'Medialuna Salada',50,110,'Unid'),
(default,2,'Medialuna Dulce',80,120,'Unid'),
(default,2,'Vigilante',30,125,'Unid'),
(default,2,'Con Crema',30,125,'Unid'),
(default,2,'Cañoncito',25,125,'Unid'),
(default,2,'Sacramento',20,125,'Unid'),
(default,2,'Bola de Fraile',20,125,'Unid'),
(default,3,'Mignon',10,425,'Kg'),
(default,3,'Frances',12,400,'Kg'),
(default,3,'Flautín',8,425,'Kg'),
(default,3,'Baguette',5,450,'Kg');