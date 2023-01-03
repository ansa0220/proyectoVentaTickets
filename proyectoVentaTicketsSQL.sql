drop database proyectoVentaTickets;
create database proyectoVentaTickets;
use proyectoVentaTickets;

create table usuario(
	usuario varchar(50),
	correo varchar(50),
	telefono varchar(10),
	password varchar(50),
	direccion varchar(50),
	Primary Key(usuario),
	Unique(correo)
);

create table administrador(
	usuario varchar(50),
	cedula varchar(10),
	Primary Key(usuario),
	Unique(cedula),
	Foreign key(usuario) references usuario(usuario)
);

create table productor(
	usuario varchar(50),
	RUC varchar(50),
	RazonSocial varchar(50),
	Primary Key(usuario),
	Unique(RUC),
	Foreign key(usuario) references usuario(usuario)
);

create table cliente(
	usuario varchar(50),
	cedula varchar(10),
	nombres varchar(50),
	apellidos varchar(50),
	Primary Key(usuario),
	Unique(cedula),
	Foreign key(usuario) references usuario(usuario)
);

create table evento(
	id_evento int auto_increment,
	nombre varchar(50),
	descripcion varchar(100),
	imagen varchar(50),
	usuarioAdm varchar(50),
	usuarioPro varchar(50),
	fecha_registro date,
	Primary key(id_evento, usuarioPro),
	Foreign key(usuarioAdm) references administrador(usuario),
	Foreign key(usuarioPro) references productor(usuario)
);

Create table ciudad (
	Id_ciudad int auto_increment primary key,
	Ciudad varchar(10)
);

Create table lugar (
	id_lugar int auto_increment primary key,
	Nombre varchar(50) not null,
	Tipo varchar(50) not null,
	Descripcion varchar(50) not null,
	Constraint conLugar foreign key (id_lugar) references ciudad (id_ciudad)
);

Create table show_evento(
	id_show int auto_increment,
	fecha date,
	hora_inicio time,
	hora_fin time,
	id_evento int,
	id_lugar int,
	Primary key(id_show),
	Foreign key(id_evento) references evento(id_evento),
	Foreign key(id_lugar) references lugar(id_lugar)
);

Create table zona(
	id_zona int auto_increment primary key,
	Zona varchar(50) not null
);

Create table asiento (
	Id_asiento int auto_increment primary key,
	Fila int not null,
	Numero int not null,
	Id_zona int not null,
	Id_lugar int not null,
	Constraint conasientozona foreign key (id_zona) references zona(id_zona),
	Constraint conasientolugar foreign key (id_lugar) references lugar(id_lugar)
);

Create table punto_de_venta (
	Id_pdv int auto_increment primary key,
	Nombre varchar(50) not null,
	Direccion varchar(50) not null,
	Tipo varchar(50) not null
);

Create table factura (
	Num_factura int auto_increment primary key,
	Fecha date,
	Descripcion varchar(50) not null,
	Total float not null,
	Forma_pago varchar(50) not null,
	Id_pdv int not null,
	Usuario varchar(50) not null,
	Constraint confacturapdv foreign key (id_pdv) references punto_de_venta (id_pdv),
	Constraint confacturausuario foreign key (usuario) references cliente(usuario)
);

Create table ticket (
	Codigo_barra int primary key,
	Precio_unitario float not null,
	id_show int not null,
	usuario varchar(50) not null,
	id_asiento int not null,
	Num_factura int not null,
	id_pdv int not null,
	estado varchar(50) not null,
	constraint conticketshow foreign key (id_show) references show_evento(id_show),
	constraint conticketusuario foreign key (usuario) references cliente(usuario),
	constraint conticketasiento foreign key (id_asiento) references asiento (id_asiento),
	constraint conticketfactura foreign key (num_factura) references factura (num_factura),
	constraint conticketpdv foreign key (id_pdv) references punto_de_venta (id_pdv)
);