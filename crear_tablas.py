from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Date, Time
meta = MetaData()

from conexion import generate_engine,connect_or_create_database


print("Creando base de datos")
connect_or_create_database()

print("Creando tablas")
engine = generate_engine("testNew")

String = String(255)

usuario = Table(
   'usuario', meta, 
   Column('usuario', String, primary_key = True), 
   Column('correo', String, unique = True),
   Column('telefono', String), 
   Column('password', String), 
   Column('direccion', String)
)

# crear tabla Administrador con un foreing key a la tabla usuario que seria su usuario
administrador = Table(
    'administrador', meta,
    Column('usuario', String, ForeignKey("usuario.usuario"), primary_key = True),
    Column('cedula', String, unique = True)
)

productor = Table(
    'productor', meta,
    Column('usuario', String, ForeignKey("usuario.usuario"), primary_key = True),
    Column('RUC', String, unique = True),
    Column('razon_social', String)
)

cliente = Table(
    'cliente', meta,
    Column('usuario', String, ForeignKey("usuario.usuario"), primary_key = True),
    Column('cedula', String, unique = True),
    Column('nombres', String),
    Column('apellidos', String)
)


evento = Table(
    'evento', meta,
    Column('id_evento', Integer, primary_key = True),
    Column('nombre', String),
    Column('descripcion', String),
    Column('imagen', String),
    Column('usuario', String, ForeignKey("usuario.usuario")),
    Column('RUC', String, ForeignKey("productor.RUC"), primary_key = True),
    Column('fecha_registro', Date),
)


ciudad = Table(
    'ciudad', meta,
    Column('id_ciudad', Integer, primary_key = True),
    Column('ciudad', String)
)

lugar = Table(
    'lugar', meta,
    Column('id_lugar', Integer, primary_key = True),
    Column('nombre', String),
    Column('tipo', String),
    Column('descripcion', String),
    Column('id_ciudad', Integer, ForeignKey("ciudad.id_ciudad"))
)



show = Table(
    'show', meta,
    Column('id_show', Integer, primary_key = True),
    Column('fecha', Date),
    Column('hora_inicio', Time),
    Column('hora_fin', Time),
    Column('id_evento', Integer, ForeignKey("evento.id_evento"), primary_key = True),
    Column('id_lugar', Integer, ForeignKey("lugar.id_lugar"), primary_key = True)
)

zona = Table(
    'zona', meta,
    Column('id_zona', Integer, primary_key = True),
    Column('zona', String)
)

asiento = Table(
    'asiento', meta,
    Column('id_asiento', Integer, primary_key = True),
    Column('fila', Integer),
    Column('numero', Integer),
    Column('id_zona', Integer, ForeignKey("zona.id_zona"), primary_key = True),
    Column('id_lugar', Integer, ForeignKey("lugar.id_lugar"), primary_key = True)
)

punto_venta = Table(
    'punto_venta', meta,
    Column('id_pdv', Integer, primary_key = True),
    Column('nombre', String),
    Column('direccion', String),
    Column('tipo', String)
)


factura = Table(
    'factura', meta,
    Column('id_factura', Integer, primary_key = True),
    Column('fecha', Date),
    Column('descripcion', String),
    Column('total', Integer),
    Column('forma_pago', String),
    Column('id_pdv', Integer, ForeignKey("punto_venta.id_pdv")),
    Column('usuario', String, ForeignKey("cliente.usuario"))
)

ticket = Table(
    'ticket', meta,
    Column('codigo_barra', Integer, primary_key = True),
    Column('precio_unitario', Integer),
    Column('id_show', Integer, ForeignKey("show.id_show")),
    Column('id_asiento', Integer, ForeignKey("asiento.id_asiento")),
    Column('id_pdv', Integer, ForeignKey("punto_venta.id_pdv")),
    Column('usuario', String, ForeignKey("cliente.usuario")),
    Column('id_factura', Integer, ForeignKey("factura.id_factura")),
    Column('estado', String)
)



# guarda todas las tablas
meta.create_all(engine)

print("Tablas creadas")

# muestra todas las tablas
print(engine.table_names())
