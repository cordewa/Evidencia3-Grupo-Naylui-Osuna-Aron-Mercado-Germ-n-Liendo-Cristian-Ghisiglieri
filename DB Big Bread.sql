CREATE database DB_BIG_BREAD;

USE DB_BIG_BREAD;
CREATE TABLE Proveedor(
	IdProveedor int PRIMARY KEY,
	CUIT int,
	Nombre varchar(30),
    Telefono int,
    Calle varchar(30),
	Numero int,
    Ciudad varchar(30),
    Provincia varchar(30));
    
CREATE TABLE Compras(
	IdCompra int PRIMARY KEY,
	IdProveedor int,
	Fecha date);
    
CREATE TABLE Detalle_Compra(
	IdDet_Compra int PRIMARY KEY,
	IdCompra int,
    IdInsumo int,
    Cantidad int,
	Precio decimal(10, 2));
    
CREATE TABLE Insumos(
	IdInsumo int PRIMARY KEY,
	Nombre varchar(30),
    Stock int,
	Precio decimal(10, 2));
    
CREATE TABLE Recetas(
	IdReceta int PRIMARY KEY,
	Nombre varchar(30),
    IdInsumo int,
    Cant_Insumo int,
    IdProducto int,
	Cant_Producto int);
    
CREATE TABLE Productos(
	IdProducto int PRIMARY KEY,
    IdCategoria int,
	Nombre varchar(30));
    
CREATE TABLE Categorias(
	IdCategoria int PRIMARY KEY,
	Nombre varchar(30),
	Descripcion varchar(50));
    
CREATE TABLE Pedidos(
	Nro_Factura int PRIMARY KEY,
	Fecha date,
    IdCliente int,
	Monto_Total decimal(10, 2));
    
CREATE TABLE Detalle_Pedidos(
	IdDet_Pedido int PRIMARY KEY,
    Nro_Factura int,
    IdProducto int,
    Cantidad int,
	Precio decimal(10, 2));
    
CREATE TABLE Cliente(
	IdCliente int PRIMARY KEY,
	Nombre varchar(30),
    Telefono int,
	Calle varchar(30),
	Numero int,
    Ciudad varchar(30),
    Provincia varchar(30));

SET SQL_SAFE_UPDATES = 0;
DELETE from DB_BIG_BREAD.Proveedor;

ALTER TABLE `DB_BIG_BREAD`.`Proveedor`
CHANGE COLUMN `IdProveedor` `IdProveedor` INT(11) NOT NULL AUTO_INCREMENT,
CHANGE COLUMN `CUIT` `CUIT` INT(11) NOT NULL,
CHANGE COLUMN `Nombre` `Nombre` VARCHAR(30) NOT NULL,
CHANGE COLUMN `Telefono` `Telefono` INT(11) NOT NULL,
CHANGE COLUMN `Calle` `Calle` VARCHAR(30) NOT NULL,
CHANGE COLUMN `Numero` `Numero` INT(11) NOT NULL,
CHANGE COLUMN `Ciudad` `Ciudad` VARCHAR(30) NOT NULL,
CHANGE COLUMN `Provincia` `Provincia` VARCHAR(30) NOT NULL;

ALTER TABLE `DB_BIG_BREAD`.`Compras`
CHANGE COLUMN `IdCompra` `IdCompra` INT(11) NOT NULL AUTO_INCREMENT,
CHANGE COLUMN `IdProveedor` `IdProveedor` INT(11) NOT NULL,
CHANGE COLUMN `Fecha` `Fecha` date NOT NULL;

ALTER TABLE `DB_BIG_BREAD`.`Detalle_Compra`
CHANGE COLUMN `IdDet_Compra` `IdDet_Compra` INT(11) NOT NULL AUTO_INCREMENT,
CHANGE COLUMN `IdCompra` `IdCompra` INT(11) NOT NULL,
CHANGE COLUMN `IdInsumo` `IdInsumo` INT(11) NOT NULL,
CHANGE COLUMN `Cantidad` `Cantidad` INT(11) NOT NULL,
CHANGE COLUMN `Precio` `Precio` DECIMAL(10, 2) NOT NULL;
    
ALTER TABLE `DB_BIG_BREAD`.`Insumos`
CHANGE COLUMN `IdInsumo` `IdInsumo` INT(11) NOT NULL AUTO_INCREMENT,
CHANGE COLUMN `Nombre` `Nombre` VARCHAR(30) NOT NULL,
CHANGE COLUMN `Stock` `Stock` INT(11) NOT NULL,
CHANGE COLUMN `Precio` `Precio` DECIMAL(10, 2) NOT NULL;
    
ALTER TABLE `DB_BIG_BREAD`.`Recetas`
CHANGE COLUMN `IdReceta` `IdReceta` INT(11) NOT NULL AUTO_INCREMENT,
CHANGE COLUMN `Nombre` `Nombre` VARCHAR(30) NOT NULL,
CHANGE COLUMN `IdInsumo` `IdInsumo` INT(11) NOT NULL,
CHANGE COLUMN `Cant_Insumo` `Cant_Insumo` INT(11) NOT NULL,
CHANGE COLUMN `IdProducto` `IdProducto` INT(11) NOT NULL,
CHANGE COLUMN `Cant_Producto` `Cant_Producto` INT(11) NOT NULL;
    
ALTER TABLE `DB_BIG_BREAD`.`Productos`
CHANGE COLUMN `IdProducto` `IdProducto` INT(11) NOT NULL AUTO_INCREMENT,
CHANGE COLUMN `IdCategoria` `IdCategoria` INT(11) NOT NULL,
CHANGE COLUMN `Nombre` `Nombre` VARCHAR(30) NOT NULL;
    
ALTER TABLE `DB_BIG_BREAD`.`Categorias`
CHANGE COLUMN `IdCategoria` `IdCategoria` INT(11) NOT NULL AUTO_INCREMENT,
CHANGE COLUMN `Nombre` `Nombre` VARCHAR(30) NOT NULL;
    
ALTER TABLE `DB_BIG_BREAD`.`Pedidos`
CHANGE COLUMN `Nro_Factura` `Nro_Factura` INT(11) NOT NULL AUTO_INCREMENT,
CHANGE COLUMN `Fecha` `Fecha` date NOT NULL,
CHANGE COLUMN `IdCliente` `IdCliente` INT(11) NOT NULL,
CHANGE COLUMN `Monto_Total` `Monto_Total` DECIMAL(10, 2) NOT NULL;
    
ALTER TABLE `DB_BIG_BREAD`.`Detalle_Pedidos`
CHANGE COLUMN `IdDet_Pedido` `IdDet_Pedido` INT(11) NOT NULL AUTO_INCREMENT,
CHANGE COLUMN `Nro_Factura` `Nro_Factura` INT(11) NOT NULL,
CHANGE COLUMN `IdProducto` `IdProducto` INT(11) NOT NULL,
CHANGE COLUMN `Cantidad` `Cantidad` INT(11) NOT NULL,
CHANGE COLUMN `Precio` `Precio` DECIMAL(10, 2) NOT NULL;
    
ALTER TABLE `DB_BIG_BREAD`.`Cliente`
CHANGE COLUMN `IdCliente` `IdCliente` INT(11) NOT NULL AUTO_INCREMENT,
CHANGE COLUMN `Nombre` `Nombre` VARCHAR(30) NOT NULL,
CHANGE COLUMN `Telefono` `Telefono` INT(11) NOT NULL,
CHANGE COLUMN `Calle` `Calle` VARCHAR(30) NOT NULL,
CHANGE COLUMN `Numero` `Numero` INT(11) NOT NULL,
CHANGE COLUMN `Ciudad` `Ciudad` VARCHAR(30) NOT NULL,
CHANGE COLUMN `Provincia` `Provincia` VARCHAR(30) NOT NULL;

ALTER TABLE `DB_BIG_BREAD`.`Categorias` 
DROP COLUMN `Descripcion`;

ALTER TABLE `DB_BIG_BREAD`.`Proveedor`
CHANGE COLUMN `CUIT` `CUIT` VARCHAR(15) NOT NULL,
CHANGE COLUMN `Telefono` `Telefono` VARCHAR(20) NOT NULL;

INSERT INTO DB_BIG_BREAD.Proveedor(IdProveedor,CUIT,Nombre,Telefono,Calle,Numero,Ciudad,Provincia) 
VALUES(default,30-70869989-2,'Molinos MB S.A.','0351 455-5233','Almagro',1749,'Córdoba','Córdoba');

ALTER TABLE `DB_BIG_BREAD`.`Cliente`
CHANGE COLUMN `Telefono` `Telefono` VARCHAR(20) NOT NULL;

INSERT INTO DB_BIG_BREAD.Proveedor(IdProveedor,CUIT,Nombre,Telefono,Calle,Numero,Ciudad,Provincia) 
VALUES(default,30-51596921-3,'Celusal-Timbo S.A.','0381 405-9992','Ruta 305 Km.',305,'El Timbó','Tucumán');

ALTER TABLE `DB_BIG_BREAD`.`Proveedor`
CHANGE COLUMN `Calle` `Calle` VARCHAR(40) NOT NULL;

INSERT INTO DB_BIG_BREAD.Proveedor(IdProveedor,CUIT,Nombre,Telefono,Calle,Numero,Ciudad,Provincia) 
VALUES(default,30-50125030-5,'Ledesma S.A.A.I.','011 4378-1555','Av. Corrientes',415,'CABA','Buenos Aires'),
(default,30-71555393-3,'Mapricor S.R.L.','0351 425-3097','Potosí',1208,'Córdoba','Córdoba'),
(default,33-50134847-9,'Refinería Del Centro S.A.','0351 450-1600','Camino a Capilla de los Remedios',7373,'Córdoba','Córdoba'),
(default,33-71613618-9,'MDM S.R.L.','0351 423-2353','San Martín',628,'Córdoba','Córdoba'),
(default,33-71428307-9,'Avícola Ovo S.R.L.','0351 361-9769','Av. Juan B. Justo',4493,'Córdoba','Córdoba'),
(default,30-52924642-7,'La Lacteo S.A.','0351 497-6010','Camino a Capilla de los Remedios',7000,'Córdoba','Córdoba'),
(default,30-54759682-6,'DUlcor S.A.','03576 421-790','Av. Elvio Eladio Riba',1615,'Arroyito','Córdoba'),
(default,30-63844281-3,'Distribuidora Insucor S.R.L.','0351 880-6299','Padre Luis MOnti',2401,'Córdoba','Córdoba');

SELECT * from DB_BIG_BREAD.Proveedor;

USE DB_BIG_BREAD;
UPDATE Proveedor SET CUIT='30-70869989-2' WHERE IdProveedor=1;

SELECT * from DB_BIG_BREAD.Proveedor;

USE DB_BIG_BREAD;
UPDATE Proveedor SET CUIT='30-51596921-3' WHERE IdProveedor=2;
UPDATE Proveedor SET CUIT='30-50125030-5' WHERE IdProveedor=11;
UPDATE Proveedor SET CUIT='30-71555393-3' WHERE IdProveedor=12;
UPDATE Proveedor SET CUIT='33-50134847-9' WHERE IdProveedor=13;
UPDATE Proveedor SET CUIT='33-71613618-9' WHERE IdProveedor=14;
UPDATE Proveedor SET CUIT='33-71428307-9' WHERE IdProveedor=15;
UPDATE Proveedor SET CUIT='30-52924642-7' WHERE IdProveedor=16;
UPDATE Proveedor SET CUIT='30-54759682-6' WHERE IdProveedor=17;
UPDATE Proveedor SET CUIT='30-63844281-3' WHERE IdProveedor=18;

SELECT * from DB_BIG_BREAD.Proveedor;





