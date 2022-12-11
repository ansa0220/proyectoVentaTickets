
from conexion import generate_engine,connect_or_create_database, remove_database

remove_database('testNew')
connect_or_create_database()

engine = generate_engine("testNew")

from crear_tablas import usuario, administrador, productor, cliente, evento, ciudad, show, zona, asiento, lugar

# ingresa datos a todas las tablas
with engine.connect() as conn:
    conn.execute("commit")
    conn.execute(usuario.insert(), [
        {'usuario': 'admin', 'correo': 'admin@admin.com', 'telefono': '0987654320', 'password': 'admin', 'direccion': 'Quito'},
        {'usuario': 'productor', 'correo': 'productor@productor.com', 'telefono': '0927654320', 'password': 'productor', 'direccion': 'Quito'},
        # genera 8 clientes
        {'usuario': 'cliente1', 'correo': 'cliente1@gmail.com', 'telefono': '0987654321', 'password': 'cliente1', 'direccion': 'Quito'},
        {'usuario': 'cliente2', 'correo': 'cliente2@gmail.com', 'telefono': '0987654322', 'password': 'cliente2', 'direccion': 'Quito'},
        {'usuario': 'cliente3', 'correo': 'cliente3@gamil.com', 'telefono': '0987654323', 'password': 'cliente3', 'direccion': 'Quito'},
        {'usuario': 'cliente4', 'correo': 'cliente4@gmail.com', 'telefono': '0987654324', 'password': 'cliente4', 'direccion': 'Quito'},
        {'usuario': 'cliente5', 'correo': 'cliente5@gmail.com', 'telefono': '0987654325', 'password': 'cliente5', 'direccion': 'Quito'},
        {'usuario': 'cliente6', 'correo': 'cliente6@gmail.com', 'telefono': '0987654326', 'password': 'cliente6', 'direccion': 'Quito'},
        {'usuario': 'cliente7', 'correo': 'cliente7@gmail.com', 'telefono': '0987654327', 'password': 'cliente7', 'direccion': 'Quito'},
        {'usuario': 'cliente8', 'correo': 'cliente8@gmail.com', 'telefono': '0987654328', 'password': 'cliente8', 'direccion': 'Quito'},
    ])

    conn.execute(administrador.insert(), [
        {'usuario': 'admin', 'cedula': '1234567890'}
    ])

    conn.execute(productor.insert(), [
        {'RUC': '0234567890', 'nombre': 'productor', 'telefono': '0987654321', 'direccion': 'Quito', 'usuario': 'productor'}
    ])

    conn.execute(cliente.insert(), [
        {'usuario': 'cliente1', 'cedula': '1234567891'},
        {'usuario': 'cliente2', 'cedula': '1234567892'},
        {'usuario': 'cliente3', 'cedula': '1234567893'},
        {'usuario': 'cliente4', 'cedula': '1234567894'},
        {'usuario': 'cliente5', 'cedula': '1234567895'},
        {'usuario': 'cliente6', 'cedula': '1234567896'},
        {'usuario': 'cliente7', 'cedula': '1234567897'},
        {'usuario': 'cliente8', 'cedula': '1234567898'}
    ])

    conn.execute(evento.insert(), [
        {'id_evento': 1, 'nombre': 'Concierto de rock', 'descripcion': 'Concierto de rock', 'imagen': 'rock.jpg', 'usuario': 'productor', 'RUC': '0234567890', 'fecha_registro': '2019-05-01'},
        {'id_evento': 2, 'nombre': 'Concierto de salsa', 'descripcion': 'Concierto de salsa', 'imagen': 'salsa.jpg', 'usuario': 'productor', 'RUC': '0234567890', 'fecha_registro': '2019-05-01'},
        {'id_evento': 3, 'nombre': 'Concierto de reggaeton', 'descripcion': 'Concierto de reggaeton', 'imagen': 'reggaeton.jpg', 'usuario': 'productor', 'RUC': '0234567890', 'fecha_registro': '2019-05-01'},
        {'id_evento': 4, 'nombre': 'Concierto de cumbia', 'descripcion': 'Concierto de cumbia', 'imagen': 'cumbia.jpg', 'usuario': 'productor', 'RUC': '0234567890', 'fecha_registro': '2019-05-01'},
        {'id_evento': 5, 'nombre': 'Concierto de merengue', 'descripcion': 'Concierto de merengue', 'imagen': 'merengue.jpg', 'usuario': 'productor', 'RUC': '0234567890', 'fecha_registro': '2019-05-01'},
        {'id_evento': 6, 'nombre': 'Concierto de vallenato', 'descripcion': 'Concierto de vallenato', 'imagen': 'vallenato.jpg', 'usuario': 'productor', 'RUC': '0234567890', 'fecha_registro': '2019-05-01'},
        {'id_evento': 7, 'nombre': 'Concierto de pop', 'descripcion': 'Concierto de pop', 'imagen': 'pop.jpg', 'usuario': 'productor', 'RUC': '0234567890', 'fecha_registro': '2019-05-20'},
        {'id_evento': 8, 'nombre': 'Concierto de rap', 'descripcion': 'Concierto de rap', 'imagen': 'rap.jpg', 'usuario': 'productor', 'RUC': '0234567890', 'fecha_registro': '2019-05-20'},
    ])



    conn.execute(ciudad.insert(), [
        {'id_ciudad': 1, 'ciudad': 'Quito'},
        {'id_ciudad': 2, 'ciudad': 'Guayaquil'},
        {'id_ciudad': 3, 'ciudad': 'Cuenca'},
        {'id_ciudad': 4, 'ciudad': 'Manta'},
        {'id_ciudad': 5, 'ciudad': 'Ambato'},
        {'id_ciudad': 6, 'ciudad': 'Loja'},
        {'id_ciudad': 7, 'ciudad': 'Ibarra'},
        {'id_ciudad': 8, 'ciudad': 'Portoviejo'},
    ])
    conn.execute(lugar.insert(), [
        {'id_lugar': 1, 'nombre': 'Estadio Olímpico Atahualpa', 'tipo': 'Estadio', 'descripcion': 'Estadio de fútbol', 'id_ciudad': 1},
        {'id_lugar': 2, 'nombre': 'Estadio Monumental Banco Pichincha', 'tipo': 'Estadio', 'descripcion': 'Estadio de fútbol', 'id_ciudad': 1},
        {'id_lugar': 3, 'nombre': 'Estadio Monumental de Guayaquil', 'tipo': 'Estadio', 'descripcion': 'Estadio de fútbol', 'id_ciudad': 2},
        {'id_lugar': 4, 'nombre': 'Estadio Alejandro Serrano Aguilar', 'tipo': 'Estadio', 'descripcion': 'Estadio de fútbol', 'id_ciudad': 3},
        {'id_lugar': 5, 'nombre': 'Estadio Monumental de Manta', 'tipo': 'Estadio', 'descripcion': 'Estadio de fútbol', 'id_ciudad': 4},
        {'id_lugar': 6, 'nombre': 'Estadio Monumental de Ambato', 'tipo': 'Estadio', 'descripcion': 'Estadio de fútbol', 'id_ciudad': 5},
        {'id_lugar': 7, 'nombre': 'Estadio Monumental de Loja', 'tipo': 'Estadio', 'descripcion': 'Estadio de fútbol', 'id_ciudad': 6},
        {'id_lugar': 8, 'nombre': 'Estadio Monumental de Ibarra', 'tipo': 'Estadio', 'descripcion': 'Estadio de fútbol', 'id_ciudad': 7},
        {'id_lugar': 9, 'nombre': 'Estadio Monumental de Portoviejo', 'tipo': 'Estadio', 'descripcion': 'Estadio de fútbol', 'id_ciudad': 8},
    ])
    conn.execute(zona.insert(), [
        {'id_zona': 1, 'zona': 'General'},
        {'id_zona': 2, 'zona': 'Preferencial'},
        {'id_zona': 3, 'zona': 'VIP'},
    ])

    
    # show
    conn.execute(show.insert(), [
        {'id_show': 1, 'id_evento': 1, 'fecha': '2019-05-01', 'hora_inicio': '20:00:00', 'hora_fin': '22:00:00', 'id_lugar': 1},
        {'id_show': 2, 'id_evento': 2, 'fecha': '2019-05-01', 'hora_inicio': '20:00:00', 'hora_fin': '22:00:00', 'id_lugar': 1},
        {'id_show': 3, 'id_evento': 3, 'fecha': '2019-05-01', 'hora_inicio': '20:00:00', 'hora_fin': '22:00:00', 'id_lugar': 1},
        {'id_show': 4, 'id_evento': 4, 'fecha': '2019-05-01', 'hora_inicio': '20:00:00', 'hora_fin': '22:00:00', 'id_lugar': 1},
        {'id_show': 5, 'id_evento': 5, 'fecha': '2019-05-01', 'hora_inicio': '20:00:00', 'hora_fin': '22:00:00', 'id_lugar': 1},
        {'id_show': 6, 'id_evento': 6, 'fecha': '2019-05-01', 'hora_inicio': '20:00:00', 'hora_fin': '22:00:00', 'id_lugar': 1},
        {'id_show': 7, 'id_evento': 7, 'fecha': '2019-05-20', 'hora_inicio': '20:00:00', 'hora_fin': '22:00:00', 'id_lugar': 1},
        {'id_show': 8, 'id_evento': 8, 'fecha': '2019-05-20', 'hora_inicio': '20:00:00', 'hora_fin': '22:00:00', 'id_lugar': 1},
    ])
    conn.execute(asiento.insert(), [
        {'id_asiento': 1, 'fila': 1, 'numero': 1, 'id_zona': 1, 'id_lugar': 1},
        {'id_asiento': 2, 'fila': 1, 'numero': 2, 'id_zona': 1, 'id_lugar': 1},
        {'id_asiento': 3, 'fila': 1, 'numero': 3    , 'id_zona': 1, 'id_lugar': 1},
        {'id_asiento': 4, 'fila': 1, 'numero': 4, 'id_zona': 1, 'id_lugar': 1},
        {'id_asiento': 5, 'fila': 1, 'numero': 5, 'id_zona': 1, 'id_lugar': 1},
        {'id_asiento': 6, 'fila': 1, 'numero': 6, 'id_zona': 1, 'id_lugar': 1},
        {'id_asiento': 7, 'fila': 1, 'numero': 7, 'id_zona': 1, 'id_lugar': 1},
        {'id_asiento': 8, 'fila': 1, 'numero': 8, 'id_zona': 1, 'id_lugar': 1},
        {'id_asiento': 9, 'fila': 1, 'numero': 9, 'id_zona': 1, 'id_lugar': 1},
        {'id_asiento': 10, 'fila': 1, 'numero': 10, 'id_zona': 1, 'id_lugar': 1},
        {'id_asiento': 11, 'fila': 1, 'numero': 1, 'id_zona': 1, 'id_lugar': 2},
        {'id_asiento': 12, 'fila': 1, 'numero': 2, 'id_zona': 1, 'id_lugar': 2},
        {'id_asiento': 13, 'fila': 1, 'numero': 3, 'id_zona': 1, 'id_lugar': 2},
        {'id_asiento': 14, 'fila': 1, 'numero': 4, 'id_zona': 1, 'id_lugar': 2},
        {'id_asiento': 15, 'fila': 1, 'numero': 5, 'id_zona': 1, 'id_lugar': 2},
        {'id_asiento': 16, 'fila': 1, 'numero': 6, 'id_zona': 1, 'id_lugar': 2},
        {'id_asiento': 17, 'fila': 1, 'numero': 1, 'id_zona': 1, 'id_lugar': 3},
        {'id_asiento': 18, 'fila': 1, 'numero': 2, 'id_zona': 1, 'id_lugar': 3},
        {'id_asiento': 19, 'fila': 1, 'numero': 3, 'id_zona': 1, 'id_lugar': 3},
        {'id_asiento': 20, 'fila': 1, 'numero': 4, 'id_zona': 1, 'id_lugar': 3},
        {'id_asiento': 21, 'fila': 1, 'numero': 5, 'id_zona': 1, 'id_lugar': 3},
        {'id_asiento': 22, 'fila': 1, 'numero': 6, 'id_zona': 1, 'id_lugar': 3},
        {'id_asiento': 23, 'fila': 1, 'numero': 7, 'id_zona': 1, 'id_lugar': 3},
        {'id_asiento': 24, 'fila': 1, 'numero': 8, 'id_zona': 1, 'id_lugar': 3},
    ])
