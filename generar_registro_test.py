
from conexion import generate_engine,connect_or_create_database, remove_database

remove_database('testNew')
connect_or_create_database()

engine = generate_engine("testNew")

from crear_tablas import usuario, administrador, productor, cliente, evento, ciudad, show, zona, asiento, lugar

# ingresa datos a todas las tablas
with engine.connect() as conn:
    conn.execute("commit")
    conn.execute(usuario.insert(), [
        {'usuario': '1205', 'correo': 'rabad@hotmail.com', 'telefono': '0929032490', 'password': 'm#886N', 'direccion': 'WHYMPER E7-98 Y PASAJE DONOSO'},
        {'usuario': '9364', 'correo': 'eacosta@gmail.com', 'telefono': '0925523190', 'password': '52$T3l', 'direccion': 'ALPALLANA E6-114 Y FRANCISCO FLOR'},
        {'usuario': '1301', 'correo': 'iacosta@outloook.com', 'telefono': '0925698980', 'password': '3d#7Z0', 'direccion': '9 DE OCTUBRE N22-48 Y JERÓNIMO CARRIÓN'},
        {'usuario': '5819', 'correo': 'vacosta@hotmail.com', 'telefono': '0956989890', 'password': 'j2A03@', 'direccion': '9 DE OCTUBRE N22-49 Y JERÓNIMO CARRIÓN'},
        {'usuario': '1633', 'correo': 'jacosta@outloook.com', 'telefono': '0925056609', 'password': 'oG462^', 'direccion': 'WHYMPER E7-39 Y ALPALLANA'},
        {'usuario': '8760', 'correo': 'wacurio@gmail.com', 'telefono': '0925698980', 'password': '8X$k22', 'direccion': '9 DE OCTUBRE N22-50 Y JERÓNIMO CARRIÓN'},
        {'usuario': '9476', 'correo': 'bagila@hotmail.com', 'telefono': '0925698988', 'password': '1G^44x', 'direccion': '9 DE OCTUBRE N22-51 Y JERÓNIMO CARRIÓN'},
        {'usuario': '6300', 'correo': 'maguinaga@outloook.com', 'telefono': '0925056666', 'password': 'Q920m!', 'direccion': 'WHYMPER E7-38 Y ALPALLANA'},
        {'usuario': '5977', 'correo': 'taguirre@hotmail.com', 'telefono': '0925056607', 'password': 'q6&G69', 'direccion': 'WHYMPER E7-37 Y ALPALLANA'},
        {'usuario': '6268', 'correo': 'raguirre@gmail.com', 'telefono': '0925698987', 'password': '8*5W7h', 'direccion': 'LA PRENSA 42-95 Y MARIANO ECHEVERRÍA SECTOR LA Y'},
        {'usuario': '2024', 'correo': 'jose_aguagallo@hotmail.com', 'telefono': '0929618999', 'password': '7#9xL8', 'direccion': 'AV. UNIDAD NACIONAL ENTRE URUGUAY Y BOLIVIA SEGUNDO PISO'},
        {'usuario': '8825', 'correo': 'maria_apolo@outlook.com', 'telefono': '0925715030', 'password': '5Ed8!0', 'direccion': 'ROCAFUERTE 1344 Y BOLIVAR PLAZA DE SANTO DOMINGO, EDIFICIO GEOMIL'},
        {'usuario': '8157', 'correo': 'rodrigo_camacho@gmail.com', 'telefono': '0925881022', 'password': '230!Hj', 'direccion': 'REPUBLICA DEL SALVADOR N. 34 -183 Y SUIZA'},
        {'usuario': '9218', 'correo': 'patricio_escobar@hotmail.com', 'telefono': '0938140123', 'password': '&133Wh', 'direccion': 'REPUBLICA DEL SALVADOR N. 34 -184 Y SUIZA'},
        {'usuario': '1608', 'correo': 'alonso_insuasti@hotmail.com', 'telefono': '0938412345', 'password': '8@v89B', 'direccion': 'AV. JUAN JOSE PAEZ 233 Y ABELARDO MORAN'},
        {'usuario': '6948', 'correo': 'ruben_gualle@outlook.com', 'telefono': '0926452530', 'password': 'u%66J5', 'direccion': 'REPUBLICA DEL SALVADOR N. 34 -186 Y SUIZA'},
        {'usuario': '1856', 'correo': 'martha_rivera@outlook.com', 'telefono': '0939474400', 'password': '4@rZ08', 'direccion': 'CLEMENTE PONCE Y PIEDRAHITA'},
        {'usuario': '5169', 'correo': 'martha_ona@gmail.com', 'telefono': '0922288166', 'password': '8%aW65', 'direccion': 'CALLE IMBABURA N7-59 Y OLMEDO - ANA MAC AULIFFE'},
        {'usuario': '7169', 'correo': 'hector_jimenez@gmail.com', 'telefono': '0932981478', 'password': 'cV695#', 'direccion': 'AV. CANDIDO RADA ENTRE MANUELA CAÑIZARES Y SALINAS FRENTE A LA FISCALIA'},
        {'usuario': '9983', 'correo': 'nely_teran@gmail.com', 'telefono': '0925881258', 'password': 'B5$y60', 'direccion': 'ROCAFUERTE 1344 Y BOLIVAR PLAZA DE SANTO DOMINGO, EDIFICIO GEOMIL'}
        
    ])

    conn.execute(administrador.insert(), [
        {'usuario': '8760', 'cedula': '1720215134'},
        {'usuario': '9476', 'cedula': '2100323860'},
        {'usuario': '6300', 'cedula': '1725887093'},
        {'usuario': '5977', 'cedula': '0603476599'},
        {'usuario': '6268', 'cedula': '1716725336'}
    ])

    conn.execute(productor.insert(), [
        {'usuario': '1205', 'RUC': '0103871307001', 'razon_social': 'razon_social01'},
        {'usuario': '9364', 'RUC': '1714672274001', 'razon_social': 'razon_social02'},
        {'usuario': '1301', 'RUC': '1713280491001', 'razon_social': 'razon_social03'},
        {'usuario': '5819', 'RUC': '1002926093001', 'razon_social': 'razon_social04'},
        {'usuario': '1633', 'RUC': '1718165622001', 'razon_social': 'razon_social05'}
        
    ])

    conn.execute(cliente.insert(), [
        {'usuario': '2024', 'cedula': '0600686166', 'nombres': 'JOSE HUMBERTO', 'apellidos': 'AGUAGALLO LASO'},
        {'usuario': '8825', 'cedula': '0700897622', 'nombres': 'MARIA JOSEFA', 'apellidos': 'APOLO ORDOÑEZ'},
        {'usuario': '8157', 'cedula': '0200400687', 'nombres': 'RODRIGO EFREN', 'apellidos': 'CAMACHO VARGAS'},
        {'usuario': '9218', 'cedula': '0501169882', 'nombres': 'NELSON PATRICIO', 'apellidos': 'ESCOBAR RIVERA'},
        {'usuario': '1608', 'cedula': '1000925089', 'nombres': 'ALONSO RODRIGO', 'apellidos': 'INSUASTI POZO'},
        {'usuario': '6948', 'cedula': '1700456518', 'nombres': 'RUBEN ADALBERTO', 'apellidos': 'GUALLE QUISAGUANO'},
        {'usuario': '1856', 'cedula': '1705779070', 'nombres': 'MARTHA DEL ROCIO', 'apellidos': 'RIVERA VELA'},
        {'usuario': '5169', 'cedula': '1704977592', 'nombres': 'MARTHA MARIA DE LOURDES', 'apellidos': 'OÑA RAMOS'},
        {'usuario': '7164', 'cedula': '1100072550', 'nombres': 'HECTOR MINOS', 'apellidos': 'JIMENEZ ROMERO'},
        {'usuario': '9983', 'cedula': '1001402484', 'nombres': 'MARIA NELY', 'apellidos': 'TERAN VILLARREAL'}
        
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
