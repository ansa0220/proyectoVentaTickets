from conexion import generate_engine,connect_or_create_database, remove_database

# remove_database('testNew')
connect_or_create_database()

engine = generate_engine("testNew")

# from crear_tablas import usuario, administrador, productor, cliente, evento, ciudad, show, zona, asiento, lugar, ticket, punto_venta, factura

# Implementar el CRUD (añadir/consultar/editar/eliminar registros) por cada tabla principal de su diagrama lógico.

#añadir usuario
def add_user(usuario,correo,telefono,password,direccion):
    
    with engine.connect() as con:
        rs = con.execute('INSERT INTO usuario (usuario,correo,telefono,password,direccion) VALUES (%s,%s,%s,%s,%s)', (usuario,correo,telefono,password,direccion))
        

#consultar usuario
def get_user(usuario):

    with engine.connect() as con:
        rs = con.execute('SELECT * FROM usuario WHERE usuario = %s', (usuario,))
        print(rs.mappings().all())

#editar usuario
def update_user(usuario,correo,telefono,password,direccion):
    
    with engine.connect() as con:
        rs = con.execute('UPDATE usuario SET correo = %s, telefono = %s, password = %s, direccion = %s WHERE usuario = %s', (correo,telefono,password,direccion,usuario))
        

#eliminar  usuario
def delete_user(usuario):
    
    with engine.connect() as con:
        rs = con.execute('DELETE FROM usuario WHERE usuario = %s', (usuario,))
        

#añadir administrador (usuario, cedula)
def add_admin(usuario,cedula):
    
    with engine.connect() as con:
        rs = con.execute('INSERT INTO administrador (usuario,cedula) VALUES (%s,%s)', (usuario,cedula))
        print(dir(rs))

#consultar
def get_admin(usuario):
    
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM administrador WHERE usuario = %s', (usuario,))
        print(rs.mappings().all())

#editar
def update_admin(usuario,cedula):
    
    with engine.connect() as con:
        rs = con.execute('UPDATE administrador SET cedula = %s WHERE usuario = %s', (cedula,usuario))
        

#eliminar
def delete_admin(usuario):
    
    with engine.connect() as con:
        rs = con.execute('DELETE FROM administrador WHERE usuario = %s', (usuario,))
        

#añadir cliente (usuario, cedula, nombres, apellidos)
def add_cliente(usuario,cedula,nombres,apellidos):
    
    with engine.connect() as con:
        rs = con.execute('INSERT INTO cliente (usuario,cedula,nombres,apellidos) VALUES (%s,%s,%s,%s)', (usuario,cedula,nombres,apellidos))
        


#consultar
def get_cliente(usuario):
    
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM cliente WHERE usuario = %s', (usuario,))
        print(rs.mappings().all())

#editar
def update_cliente(usuario,cedula,nombres,apellidos):
    
    with engine.connect() as con:
        rs = con.execute('UPDATE cliente SET cedula = %s, nombres = %s, apellidos = %s WHERE usuario = %s', (cedula,nombres,apellidos,usuario))
        

#eliminar
def delete_cliente(usuario):
    
    with engine.connect() as con:
        rs = con.execute('DELETE FROM cliente WHERE usuario = %s', (usuario,))
        

#añadir productor (usuario, RUC, razon_social)
def add_productor(usuario,RUC,razon_social):
    
    with engine.connect() as con:
        rs = con.execute('INSERT INTO productor (usuario,RUC,razon_social) VALUES (%s,%s,%s)', (usuario,RUC,razon_social))
        

#consultar productor
def get_productor(usuario):
    
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM productor WHERE usuario = %s', (usuario,))
        print(rs.mappings().all())

#editar productor
def update_productor(usuario,RUC,razon_social):
    
    with engine.connect() as con:
        rs = con.execute('UPDATE productor SET RUC = %s, razon_social = %s WHERE usuario = %s', (RUC,razon_social,usuario))


#eliminar productor
def delete_productor(usuario):
    
    with engine.connect() as con:
        rs = con.execute('DELETE FROM productor WHERE usuario = %s', (usuario,))
        

#añadir evento (id_evento, nombre, descripcion, imagen, usuarioAdm, usuarioPro, fecha_registro)
def add_evento(id_evento,nombre,descripcion,imagen,usuarioAdm,usuarioPro,fecha_registro):
    
    with engine.connect() as con:
        rs = con.execute('INSERT INTO evento (id_evento,nombre,descripcion,imagen,usuarioAdm,usuarioPro,fecha_registro) VALUES (%s,%s,%s,%s,%s,%s,%s)', (id_evento,nombre,descripcion,imagen,usuarioAdm,usuarioPro,fecha_registro))
        


#consultar evento
def get_evento(id_evento):
    
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM evento WHERE id_evento = %s', (id_evento,))
        print(rs.mappings().all())

#editar evento
def update_evento(id_evento,nombre,descripcion,imagen,usuarioAdm,usuarioPro,fecha_registro):
    
    with engine.connect() as con:
        rs = con.execute('UPDATE evento SET nombre = %s, descripcion = %s, imagen = %s, usuarioAdm = %s, usuarioPro = %s, fecha_registro = %s WHERE id_evento = %s', (nombre,descripcion,imagen,usuarioAdm,usuarioPro,fecha_registro,id_evento))
        

#eliminar evento
def delete_evento(id_evento):
    
    with engine.connect() as con:
        rs = con.execute('DELETE FROM evento WHERE id_evento = %s', (id_evento,))
        

#añadir ciudad (id_ciudad, nombre)
def add_ciudad(id_ciudad,nombre):
    
    with engine.connect() as con:
        rs = con.execute('INSERT INTO ciudad (id_ciudad,nombre) VALUES (%s,%s)', (id_ciudad,nombre))
        

#consultar ciudad
def get_ciudad(id_ciudad):
    
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM ciudad WHERE id_ciudad = %s', (id_ciudad,))
        print(rs.mappings().all())

#editar ciudad
def update_ciudad(id_ciudad,nombre):
    
    with engine.connect() as con:
        rs = con.execute('UPDATE ciudad SET nombre = %s WHERE id_ciudad = %s', (nombre,id_ciudad))
        

#eliminar ciudad
def delete_ciudad(id_ciudad):
    
    with engine.connect() as con:
        rs = con.execute('DELETE FROM ciudad WHERE id_ciudad = %s', (id_ciudad,))
        

#añadir lugar (id_lugar, nombre, ubicacion, id_ciudad)
def add_lugar(id_lugar,nombre,ubicacion,id_ciudad):
    
    with engine.connect() as con:
        rs = con.execute('INSERT INTO lugar (id_lugar,nombre,ubicacion,id_ciudad) VALUES (%s,%s,%s,%s)', (id_lugar,nombre,ubicacion,id_ciudad))
        

#consultar lugar
def get_lugar(id_lugar):
    
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM lugar WHERE id_lugar = %s', (id_lugar,))
        print(rs.mappings().all())

#editar lugar
def update_lugar(id_lugar,nombre,ubicacion,id_ciudad):
    
    with engine.connect() as con:
        rs = con.execute('UPDATE lugar SET nombre = %s, ubicacion = %s, id_ciudad = %s WHERE id_lugar = %s', (nombre,ubicacion,id_ciudad,id_lugar))
        

#eliminar lugar
def delete_lugar(id_lugar):
    
    with engine.connect() as con:
        rs = con.execute('DELETE FROM lugar WHERE id_lugar = %s', (id_lugar,))
        

#añadir show (id_show, fecha, hora_inicio, hora_fin, id_evento, id_lugar)
def add_show(id_show,fecha,hora_inicio,hora_fin,id_evento,id_lugar):
    
    with engine.connect() as con:
        rs = con.execute('INSERT INTO show (id_show, fecha, hora_inicio, hora_fin, id_evento, id_lugar) VALUES (%s,%s,%s,%s,%s,%s)', (id_show,fecha,hora_inicio,hora_fin,id_evento,id_lugar))
        

#consultar show
def get_show(id_show):
    
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM show WHERE id_show = %s', (id_show,))
        print(rs.mappings().all())
    
#editar show
def update_show(id_show,fecha,hora_inicio,hora_fin,id_evento,id_lugar):
    
    with engine.connect() as con:
        rs = con.execute('UPDATE show SET fecha = %s, hora_inicio = %s, hora_fin = %s, id_evento = %s, id_lugar = %s WHERE id_show = %s', (fecha,hora_inicio,hora_fin,id_evento,id_lugar,id_show))
        

#eliminar show
def delete_show(id_show):
    
    with engine.connect() as con:
        rs = con.execute('DELETE FROM show WHERE id_show = %s', (id_show,))
        

#añadir zona (id_zona, zona)
def add_zona(id_zona,zona):
    
    with engine.connect() as con:
        rs = con.execute('INSERT INTO zona (id_zona, zona) VALUES (%s,%s)', (id_zona,zona))
        

#consultar zona
def get_zona(id_zona):
    
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM zona WHERE id_zona = %s', (id_zona,))
        print(rs.mappings().all())

#editar zona
def update_zona(id_zona,zona):
    
    with engine.connect() as con:
        rs = con.execute('UPDATE zona SET zona = %s WHERE id_zona = %s', (zona,id_zona))
        

#eliminar zona
def delete_zona(id_zona):
    
    with engine.connect() as con:
        rs = con.execute('DELETE FROM zona WHERE id_zona = %s', (id_zona,))
        

#añadir asiento (id_asiento, fila, columna, id_zona, id_lugar)
def add_asiento(id_asiento,fila,columna,id_zona,id_lugar):
    
    with engine.connect() as con:
        rs = con.execute('INSERT INTO asiento (id_asiento, fila, columna, id_zona, id_lugar) VALUES (%s,%s,%s,%s,%s)', (id_asiento,fila,columna,id_zona,id_lugar))
        

#consultar asiento
def get_asiento(id_asiento):
    
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM asiento WHERE id_asiento = %s', (id_asiento,))
        print(rs.mappings().all())

#editar asiento
def update_asiento(id_asiento,fila,columna,id_zona,id_lugar):
    
    with engine.connect() as con:
        rs = con.execute('UPDATE asiento SET fila = %s, columna = %s, id_zona = %s, id_lugar = %s WHERE id_asiento = %s', (fila,columna,id_zona,id_lugar,id_asiento))
        

#eliminar asiento
def delete_asiento(id_asiento):
    
    with engine.connect() as con:
        rs = con.execute('DELETE FROM asiento WHERE id_asiento = %s', (id_asiento,))
        

#añadir punto_venta (id_pdv, nombre, direccion, tipo)
def add_pdv(id_pdv,nombre,direccion,tipo):
    
    with engine.connect() as con:
        rs = con.execute('INSERT INTO punto_venta (id_pdv, nombre, direccion, tipo) VALUES (%s,%s,%s,%s)', (id_pdv,nombre,direccion,tipo))
        

#consultar punto_venta
def get_pdv(id_pdv):
    
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM punto_venta WHERE id_pdv = %s', (id_pdv,))
        print(rs.mappings().all())

#editar punto_venta
def update_pdv(id_pdv,nombre,direccion,tipo):
    
    with engine.connect() as con:
        rs = con.execute('UPDATE punto_venta SET nombre = %s, direccion = %s, tipo = %s WHERE id_pdv = %s', (nombre,direccion,tipo,id_pdv))
        

#eliminar punto_venta
def delete_pdv(id_pdv):
    
    with engine.connect() as con:
        rs = con.execute('DELETE FROM punto_venta WHERE id_pdv = %s', (id_pdv,))
        

#añadir factura (id_factura, fecha, descripcion, total, forma_pago, id_pdv, usuario)
def add_factura(id_factura,fecha,descripcion,total,forma_pago,id_pdv,usuario):
    
    with engine.connect() as con:
        rs = con.execute('INSERT INTO factura (id_factura, fecha, descripcion, total, forma_pago, id_pdv, usuario) VALUES (%s,%s,%s,%s,%s,%s,%s)', (id_factura,fecha,descripcion,total,forma_pago,id_pdv,usuario))
        

#consultar factura
def get_factura(id_factura):
    
    with engine.connect() as con:
        rs = con.execute('SELECT * FROM factura WHERE id_factura = %s', (id_factura,))
        print(rs.mappings().all())

#editar factura
def update_factura(id_factura,fecha,descripcion,total,forma_pago,id_pdv,usuario):
    
    with engine.connect() as con:
        rs = con.execute('UPDATE factura SET fecha = %s, descripcion = %s, total = %s, forma_pago = %s, id_pdv = %s, usuario = %s WHERE id_factura = %s', (fecha,descripcion,total,forma_pago,id_pdv,usuario,id_factura))
        

#eliminar factura
def delete_factura(id_factura):
    
    with engine.connect() as con:
        rs = con.execute('DELETE FROM factura WHERE id_factura = %s', (id_factura,))
        

#añadir ticket (codigo_barra, precio_unitario, id_show, id_asiento, id_pdv, usuario, id_factura, estado)
def add_ticket(codigo_barra,precio_unitario,id_show,id_asiento,id_pdv,usuario,id_factura,estado):
    
    with engine.connect() as con:
        rs = con.execute('INSERT INTO ticket (codigo_barra, precio_unitario, id_show, id_asiento, id_pdv, usuario, id_factura, estado) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', (codigo_barra,precio_unitario,id_show,id_asiento,id_pdv,usuario,id_factura,estado))
        

#consultar ticket
def get_ticket(codigo_barra):
        
        with engine.connect() as con:
            rs = con.execute('SELECT * FROM ticket WHERE codigo_barra = %s', (codigo_barra,))
            print(rs.mappings().all())


#editar ticket
def update_ticket(codigo_barra,precio_unitario,id_show,id_asiento,id_pdv,usuario,id_factura,estado):
        
    with engine.connect() as con:
        rs = con.execute('UPDATE ticket SET precio_unitario = %s, id_show = %s, id_asiento = %s, id_pdv = %s, usuario = %s, id_factura = %s, estado = %s WHERE codigo_barra = %s', (precio_unitario,id_show,id_asiento,id_pdv,usuario,id_factura,estado,codigo_barra))
        

#eliminar ticket
def delete_ticket(codigo_barra):
    
    with engine.connect() as con:
        rs = con.execute('DELETE FROM ticket WHERE codigo_barra = %s', (codigo_barra,))
        
    
    



def insert():
    opciones = {
        '1': add_user,
        '2': add_lugar,
        '3': add_zona,
        '4': add_asiento,
        '5': add_pdv,
        '6': add_factura,
        '7': add_ticket,
        '8': add_evento,
        '9': add_show,
        '10': add_ciudad,
        '11': add_admin,
        '12': add_cliente,
        '13': add_productor

    }
    print('''## Añadir ##
    1. Usuario
    2. Lugar
    3. Zona
    4. Asiento
    5. Punto de venta
    6. Factura
    7. Ticket
    8. Evento
    9. Show
    10. Ciudad
    11. Administrador
    12. Cliente
    13. Productor
    ''')
    opcion = input('Opcion: ')
    if opcion == '1':
        id_usuario = input('id_usuario: ')
        correo = input('correo: ')
        telefono = input('telefono: ')
        password = input('password: ')
        direccion = input('direccion: ')
        opciones[opcion](id_usuario,correo,telefono,password,direccion)
    elif opcion == '2':
        id_lugar = input('id_lugar: ')
        nombre = input('nombre: ')
        ubicacion = input('ubicacion: ')
        id_ciudad = input('id_ciudad: ')
        opciones[opcion](id_lugar,nombre,ubicacion,id_ciudad)
    elif opcion == '3':
        id_zona = input('id_zona: ')
        zona = input('zona: ')
        opciones[opcion](id_zona,zona)
    elif opcion == '4':
        id_asiento = input('id_asiento: ')
        fila = input('fila: ')
        columna = input('columna: ')
        id_zona = input('id_zona: ')
        id_lugar = input('id_lugar: ')
        opciones[opcion](id_asiento,fila,columna,id_zona,id_lugar)
    elif opcion == '5':
        id_pdv = input('id_pdv: ')
        nombre = input('nombre: ')
        direccion = input('direccion: ')
        tipo = input('tipo: ')
        opciones[opcion](id_pdv,nombre,direccion,tipo)
    elif opcion == '6':
        id_factura = input('id_factura: ')
        fecha = input('fecha: ')
        descripcion = input('descripcion: ')
        total = input('total: ')
        forma_pago = input('forma_pago: ')
        id_pdv = input('id_pdv: ')
        usuario = input('usuario: ')
        opciones[opcion](id_factura,fecha,descripcion,total,forma_pago,id_pdv,usuario)
    elif opcion == '7':
        codigo_barra = input('codigo_barra: ')
        precio_unitario = input('precio_unitario: ')
        id_show = input('id_show: ')
        id_asiento = input('id_asiento: ')
        id_pdv = input('id_pdv: ')
        usuario = input('usuario: ')
        id_factura = input('id_factura: ')
        estado = input('estado: ')
        opciones[opcion](codigo_barra,precio_unitario,id_show,id_asiento,id_pdv,usuario,id_factura,estado)
    elif opcion == '8':
        id_evento = input('id_evento: ')
        nombre = input('nombre: ')
        descripcion = input('descripcion: ')
        opciones[opcion](id_evento,nombre,descripcion)
    elif opcion == '9':
        id_show = input('id_show: ')
        fecha = input('fecha: ')
        hora = input('hora: ')
        id_evento = input('id_evento: ')
        opciones[opcion](id_show,fecha,hora,id_evento)
    elif opcion == '10':
        id_ciudad = input('id_ciudad: ')
        nombre = input('nombre: ')
        opciones[opcion](id_ciudad,nombre)
    elif opcion == '11':
        usuario = input('usuario: ')
        cedula = input('cedula: ')
        opciones[opcion](usuario,cedula)
    elif opcion == '12':
        usuario = input('usuario: ')
        cedula = input('cedula: ')
        nombres = input('nombres: ')
        apellidos = input('apellidos: ')
        opciones[opcion](usuario,cedula,nombres,apellidos)
    elif opcion == '13':
        usuario = input('usuario: ')
        RUC = input('RUC: ')
        razon_social = input('razon_social: ')
        opciones[opcion](usuario,RUC,razon_social)
    else:
        print('Opcion no valida')
    


def select():
    opciones = {
        '1': get_user,
        '2': get_lugar,
        '3': get_zona,
        '4': get_asiento,
        '5': get_pdv,
        '6': get_factura,
        '7': get_ticket,
        '8': get_evento,
        '9': get_show,
        '10': get_ciudad,
        '11': get_admin,
        '12': get_cliente,
        '13': get_productor
    }
    print('''## Consultar ##
    1. Usuario
    2. Lugar
    3. Zona
    4. Asiento
    5. Punto de venta
    6. Factura
    7. Ticket
    8. Evento
    9. Show
    10. Ciudad
    11. Administrador
    12. Cliente
    13. Productor
    ''')
    opcion = input('Opcion: ')
    if opcion == '1':
        id_usuario = input('id_usuario: ')
        opciones[opcion](id_usuario)
    elif opcion == '2':
        id_lugar = input('id_lugar: ')
        opciones[opcion](id_lugar)
    elif opcion == '3':
        id_zona = input('id_zona: ')
        opciones[opcion](id_zona)
    elif opcion == '4':
        id_asiento = input('id_asiento: ')
        opciones[opcion](id_asiento)
    elif opcion == '5':
        id_pdv = input('id_pdv: ')
        opciones[opcion](id_pdv)
    elif opcion == '6':
        id_factura = input('id_factura: ')
        opciones[opcion](id_factura)
    elif opcion == '7':
        codigo_barra = input('codigo_barra: ')
        opciones[opcion](codigo_barra)
    elif opcion == '8':
        id_evento = input('id_evento: ')
        opciones[opcion](id_evento)
    elif opcion == '9':
        id_show = input('id_show: ')
        opciones[opcion](id_show)
    elif opcion == '10':
        id_ciudad = input('id_ciudad: ')
        opciones[opcion](id_ciudad)
    elif opcion == '11':
        usuario = input('usuario: ')
        opciones[opcion](usuario)
    elif opcion == '12':
        usuario = input('usuario: ')
        opciones[opcion](usuario)
    elif opcion == '13':
        usuario = input('usuario: ')
        opciones[opcion](usuario)
    else:
        print('Opcion no valida')

def delete():
    opciones = {
        '1': delete_user,
        '2': delete_lugar,
        '3': delete_zona,
        '4': delete_asiento,
        '5': delete_pdv,
        '6': delete_factura,
        '7': delete_ticket,
        '8': delete_evento,
        '9': delete_show,
        '10': delete_ciudad,
        '11': delete_admin,
        '12': delete_cliente,
        '13': delete_productor
    }
    print('''## Eliminar ##
    1. Usuario
    2. Lugar
    3. Zona
    4. Asiento
    5. Punto de venta
    6. Factura
    7. Ticket
    8. Evento
    9. Show
    10. Ciudad
    11. Administrador
    12. Cliente
    13. Productor
    ''')
    opcion = input('Opcion: ')
    if opcion == '1':
        id_usuario = input('id_usuario: ')
        opciones[opcion](id_usuario)
    elif opcion == '2':
        id_lugar = input('id_lugar: ')
        opciones[opcion](id_lugar)
    elif opcion == '3':
        id_zona = input('id_zona: ')
        opciones[opcion](id_zona)
    elif opcion == '4':
        id_asiento = input('id_asiento: ')
        opciones[opcion](id_asiento)
    elif opcion == '5':
        id_pdv = input('id_pdv: ')
        opciones[opcion](id_pdv)
    elif opcion == '6':
        id_factura = input('id_factura: ')
        opciones[opcion](id_factura)
    elif opcion == '7':
        codigo_barra = input('codigo_barra: ')
        opciones[opcion](codigo_barra)
    elif opcion == '8':
        id_evento = input('id_evento: ')
        opciones[opcion](id_evento)
    elif opcion == '9':
        id_show = input('id_show: ')
        opciones[opcion](id_show)
    elif opcion == '10':
        id_ciudad = input('id_ciudad: ')
        opciones[opcion](id_ciudad)
    elif opcion == '11':
        usuario = input('usuario: ')
        opciones[opcion](usuario)
    elif opcion == '12':
        usuario = input('usuario: ')
        opciones[opcion](usuario)
    elif opcion == '13':
        usuario = input('usuario: ')
        opciones[opcion](usuario)
    else:
        print('Opcion no valida')


def update():
    opciones = {
        '1': update_user,
        '2': update_lugar,
        '3': update_zona,
        '4': update_asiento,
        '5': update_pdv,
        '6': update_factura,
        '7': update_ticket,
        '8': update_evento,
        '9': update_show,
        '10': update_ciudad,
        '11': update_admin,
        '12': update_cliente,
        '13': update_productor
    }
    print('''## Actualizar ##
    1. Usuario
    2. Lugar
    3. Zona
    4. Asiento
    5. Punto de venta
    6. Factura
    7. Ticket
    8. Evento
    9. Show
    10. Ciudad
    11. Administrador
    12. Cliente
    13. Productor
    ''')
    opcion = input('Opcion: ')
    if opcion == '1':
        id_usuario = input('id_usuario: ')
        correo = input('correo: ')
        telefono = input('telefono: ')
        password = input('password: ')
        direccion = input('direccion: ')
        opciones[opcion](id_usuario, correo, telefono, password, direccion)
    elif opcion == '2':
        id_lugar = input('id_lugar: ')
        nombre = input('nombre: ')
        ubicacion = input('ubicacion: ')
        id_ciudad = input('id_ciudad: ')
        opciones[opcion](id_lugar, nombre, ubicacion, id_ciudad)
    elif opcion == '3':
        id_zona = input('id_zona: ')
        zona = input('zona: ')
        opciones[opcion](id_zona, zona)
    elif opcion == '4':
        id_asiento = input('id_asiento: ')
        fila = input('fila: ')
        columna = input('columna: ')
        id_zona = input('id_zona: ')
        id_lugar = input('id_lugar: ')
        opciones[opcion](id_asiento, fila, columna, id_zona, id_lugar)
    elif opcion == '5':
        id_pdv = input('id_pdv: ')
        nombre = input('nombre: ')
        direccion = input('direccion: ')
        tipo = input('tipo: ')
        opciones[opcion](id_pdv, nombre, direccion, tipo)
    elif opcion == '6':
        id_factura = input('id_factura: ')
        fecha = input('fecha: ')
        descripcion = input('descripcion: ')
        total = input('total: ')
        forma_pago = input('forma_pago: ')
        id_pdv = input('id_pdv: ')
        id_usuario = input('id_usuario: ')
        opciones[opcion](id_factura, fecha, descripcion, total, forma_pago, id_pdv, id_usuario)
    elif opcion == '7':
        codigo_barra = input('codigo_barra: ')
        precio_unitario = input('precio_unitario: ')
        id_show = input('id_show: ')
        id_asiento = input('id_asiento: ')
        id_pdv = input('id_pdv: ')
        usuario = input('usuario: ')
        id_factura = input('id_factura: ')
        estado = input('estado: ')
        opciones[opcion](codigo_barra, precio_unitario, id_show, id_asiento, id_pdv, usuario, id_factura, estado)
    elif opcion == '8':
        id_evento = input('id_evento: ')
        nombre = input('nombre: ')
        descripcion = input('descripcion: ')
        imagen = input('imagen: ')
        usuarioAdm = input('usuarioAdm: ')
        usuarioPro = input('usuarioPro: ')
        fecha_registro = input('fecha_registro: ')
        opciones[opcion](id_evento, nombre, descripcion, imagen, usuarioAdm, usuarioPro, fecha_registro)
    elif opcion == '9':
        id_show = input('id_show: ')
        fecha = input('fecha: ')
        hora_inicio = input('hora_inicio: ')
        hora_fin = input('hora_fin: ')
        id_evento = input('id_evento: ')
        id_lugar = input('id_lugar: ')
        opciones[opcion](id_show, fecha, hora_inicio, hora_fin, id_evento, id_lugar)
    elif opcion == '10':
        id_ciudad = input('id_ciudad: ')
        nombre = input('nombre: ')
        opciones[opcion](id_ciudad, nombre)
    elif opcion == '11':
        usuario = input('usuario: ')
        cedula = input('cedula: ')
        opciones[opcion](usuario, cedula)
    elif opcion == '12':
        usuario = input('usuario: ')
        cedula = input('cedula: ')
        nombres = input('nombres: ')
        apellidos = input('apellidos: ')
        opciones[opcion](usuario, cedula, nombres, apellidos)
    elif opcion == '13':
        usuario = input('usuario: ')
        RUC = input('RUC: ')
        razon_social = input('razon_social: ')
        opciones[opcion](usuario, RUC, razon_social)
    else:
        print('Opcion no valida')



import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
while True:
    print('''## Menu ##
    1. Insertar
    2. Eliminar
    3. Actualizar
    4. Consultar
    5. Salir
    ''')
    opcion = input('Opcion: ')
    if opcion == '1':
        insert()
        print("Insertado con exito")
    elif opcion == '2':
        delete()
        print("Eliminado con exito")
    elif opcion == '3':
        update()
        print("Actualizado con exito")
    elif opcion == '4':
        select()
    elif opcion == '5':
        break
    else:
        print('Opcion no valida')
