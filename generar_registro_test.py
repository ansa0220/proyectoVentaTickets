
from conexion import generate_engine,connect_or_create_database, remove_database

remove_database('testNew')
connect_or_create_database()

engine = generate_engine("testNew")

from crear_tablas import usuario, administrador, productor, cliente, evento, ciudad, show, zona, asiento, lugar, ticket, punto_venta, factura

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
        {'usuario': '7169', 'cedula': '1100072550', 'nombres': 'HECTOR MINOS', 'apellidos': 'JIMENEZ ROMERO'},
        {'usuario': '9983', 'cedula': '1001402484', 'nombres': 'MARIA NELY', 'apellidos': 'TERAN VILLARREAL'}
        
    ])

    conn.execute(evento.insert(), [
        {'id_evento': 34961, 'nombre': 'Bye Bye Tour-Guayaquil', 'descripcion': 'Kimberly Loaiza y Juan de Dios Pantoja anuncia su última gira juntos', 'imagen': 'imagen1.jpg', 'usuarioAdm': '8760', 'usuarioPro': '1205', 'fecha_registro': '2022-01-09'},
        {'id_evento': 61475, 'nombre': 'Ecuador Padel Fest - Copa Kia', 'descripcion': 'El evento más importante de pádel en el Ecuador junto a Juan Lebrón, Charlie Moon y más', 'imagen': 'imagen2.jpg', 'usuarioAdm': '9476', 'usuarioPro': '9364', 'fecha_registro': '202-02-08'},
        {'id_evento': 84091, 'nombre': 'Dinos Gye', 'descripcion': 'Viven Dinosaurios en Guayaquil', 'imagen': 'imagen3.jpg', 'usuarioAdm': '6300', 'usuarioPro': '1301', 'fecha_registro': '2022-03-07'},
        {'id_evento': 62808, 'nombre': 'Camilo De Adentro Pa Afuera Tour', 'descripcion': 'Concierto de Camilo', 'imagen': 'imagen4.jpg', 'usuarioAdm': '5977', 'usuarioPro': '5819', 'fecha_registro': '2022-04-06'},
        {'id_evento': 75010, 'nombre': 'Navidad de Cristal', 'descripcion': 'Celebración Fiesta de Navidad', 'imagen': 'imagen5.jpg', 'usuarioAdm': '6268', 'usuarioPro': '1633', 'fecha_registro': '2022-05-05'},
        {'id_evento': 82160, 'nombre': 'La Última Vuelta World Tour Daddy Yankee Legendaddy', 'descripcion': 'Concierto de Daddy Yankee', 'imagen': 'imagen6.jpg', 'usuarioAdm': '8760', 'usuarioPro': '1205', 'fecha_registro': '2022-06-04'},
        {'id_evento': 27820, 'nombre': 'Cristian Castro & Karina', 'descripcion': 'Concierto de Cristian Castro & Karina', 'imagen': 'imagen7.jpg', 'usuarioAdm': '9476', 'usuarioPro': '9364', 'fecha_registro': '2022-07-03'},
        {'id_evento': 68878, 'nombre': 'Armeniazo Fest', 'descripcion': 'Festival de Armeniazo Fest', 'imagen': 'imagen8.jpg', 'usuarioAdm': '6300', 'usuarioPro': '1301', 'fecha_registro': '2022-08-02'},
        {'id_evento': 13737, 'nombre': 'Covachazo', 'descripcion': 'Covachazo', 'imagen': 'imagen9.jpg', 'usuarioAdm': '5977', 'usuarioPro': '5819', 'fecha_registro': '2022-09-01'},
        {'id_evento': 88750, 'nombre': 'Concierto de rap', 'descripcion': 'Concierto de rap', 'imagen': 'imagen10.jpg', 'usuarioAdm': '6268', 'usuarioPro': '1633', 'fecha_registro': '2022-09-30'}
    ])



    conn.execute(ciudad.insert(), [
        {'id_ciudad': 353, 'ciudad': 'Guayaquil'},
        {'id_ciudad': 146, 'ciudad': 'Quito'},
        {'id_ciudad': 207, 'ciudad': 'Manta'}
       
    ])
    conn.execute(lugar.insert(), [
        {'id_lugar': 790, 'nombre': 'Coliseo Voltaire Paladin Polo', 'tipo': 'Estadio', 'descripcion': 'Estadio de fútbol', 'id_ciudad': 353},
        {'id_lugar': 837, 'nombre': 'Rancho San Francisco - Quito', 'tipo': 'Rancho', 'descripcion': 'Rancho', 'id_ciudad': 146},
        {'id_lugar': 772, 'nombre': 'Malecon 2000 - Guayaquil', 'tipo': 'Malecon 2000', 'descripcion': 'Malecon 2000', 'id_ciudad': 353},
        {'id_lugar': 358, 'nombre': 'Coliseo General Rumiñahu', 'tipo': 'Estadio', 'descripcion': 'Estadio de fútbol', 'id_ciudad': 146},
        {'id_lugar': 501, 'nombre': 'Teatro Principal Centro de Arte', 'tipo': 'Teatro', 'descripcion': 'Teatro Principal Centro de Arte', 'id_ciudad': 353},
        {'id_lugar': 869, 'nombre': 'Estadio Modelo', 'tipo': 'Estadio', 'descripcion': 'Estadio de fútbol', 'id_ciudad': 353},
        {'id_lugar': 839, 'nombre': 'Estadio Olimpico Atahualpa', 'tipo': 'Estadio', 'descripcion': 'Estadio de fútbol', 'id_ciudad': 146},
        {'id_lugar': 419, 'nombre': 'Centro de Convenciones', 'tipo': 'Salon', 'descripcion': 'Centro de Convenciones', 'id_ciudad': 353},
        {'id_lugar': 740, 'nombre': 'Complejo Deportivo Offside', 'tipo': 'Complejo', 'descripcion': 'Complejo Deportivo', 'id_ciudad': 146},
        {'id_lugar': 469, 'nombre': 'Centro de Convenciones Miami - El Labrador', 'tipo': 'Salon', 'descripcion': 'Centro de Convenciones Miami', 'id_ciudad': 146},
        {'id_lugar': 156, 'nombre': 'Mall del Pacifico', 'tipo': 'Centro comercial', 'descripcion': 'Mall del Pacifico', 'id_ciudad': 207},
    ])
    conn.execute(zona.insert(), [
        {'id_zona': 1, 'zona': 'General'},
        {'id_zona': 2, 'zona': 'Preferencial'},
        {'id_zona': 3, 'zona': 'Tu tu Box'},
        {'id_zona': 4, 'zona': 'Butaca Tela'},
        {'id_zona': 5, 'zona': 'Butaca Aluminio'},
        {'id_zona': 6, 'zona': 'Tribuna'},
        {'id_zona': 7, 'zona': 'Platea Central'},
        {'id_zona': 8, 'zona': 'Palco Legendaddy'},
        {'id_zona': 9, 'zona': 'Palco que tire pa lante'},
        {'id_zona': 10, 'zona': 'Palco dura'},
        {'id_zona': 11, 'zona': 'Palco rompe'},
        {'id_zona': 12, 'zona': 'Sillas limbo'},
        {'id_zona': 13, 'zona': 'Llamado de emergencia'},
        {'id_zona': 14, 'zona': 'Gasolina'},
        {'id_zona': 15, 'zona': 'Somos de calle'},
        {'id_zona': 16, 'zona': 'Legendaddy Box'},
        {'id_zona': 17, 'zona': 'Big Boss Platinum'},
        {'id_zona': 18, 'zona': 'Gasolina Golden'},
        {'id_zona': 19, 'zona': 'Daddys Fan Zone'},
        {'id_zona': 20, 'zona': 'Bronce box'},
        {'id_zona': 21, 'zona': 'Plata box'},
        {'id_zona': 22, 'zona': 'Coldstar bloque'},
        {'id_zona': 23, 'zona': 'Coldatar bloque'},
        {'id_zona': 24, 'zona': 'Fans box'},
        {'id_zona': 25, 'zona': 'Palco'},
        {'id_zona': 26, 'zona': 'VIP'},
        {'id_zona': 27, 'zona': 'Platea'},
        {'id_zona': 28, 'zona': 'Boxes'},
        {'id_zona': 29, 'zona': 'Unica'}
    ])

    
    # show
    conn.execute(show.insert(), [
        {'id_show': 39277, 'id_evento': 34961, 'fecha': '2023-06-16', 'hora_inicio': '20:00:00', 'hora_fin': '12:00:00', 'id_lugar': 790},
        {'id_show': 65748, 'id_evento': 61475, 'fecha': '2022-12-19', 'hora_inicio': '19:00:00', 'hora_fin': '23:00:00', 'id_lugar': 837},
        {'id_show': 75639, 'id_evento': 84091, 'fecha': '2022-10-06', 'hora_inicio': '11:00:00', 'hora_fin': '21:00:00', 'id_lugar': 772},
        {'id_show': 29769, 'id_evento': 62808, 'fecha': '2023-03-18', 'hora_inicio': '20:00:00', 'hora_fin': '01:00:00', 'id_lugar': 358},
        {'id_show': 76784, 'id_evento': 62808, 'fecha': '2023-03-19', 'hora_inicio': '20:00:00', 'hora_fin': '01:00:00', 'id_lugar': 790},
        {'id_show': 66079, 'id_evento': 75010, 'fecha': '2022-12-17', 'hora_inicio': '17:00:00', 'hora_fin': '22:00:00', 'id_lugar': 501},
        {'id_show': 42475, 'id_evento': 82160, 'fecha': '2022-10-04', 'hora_inicio': '20:00:00', 'hora_fin': '00:00:00', 'id_lugar': 869},
        {'id_show': 41810, 'id_evento': 82160, 'fecha': '2022-10-05', 'hora_inicio': '20:00:00', 'hora_fin': '00:00:00', 'id_lugar': 839},
        {'id_show': 26092, 'id_evento': 27820, 'fecha': '2022-12-16', 'hora_inicio': '20:00:00', 'hora_fin': '00:00:00', 'id_lugar': 419},
        {'id_show': 68046, 'id_evento': 68878, 'fecha': '2022-12-02', 'hora_inicio': '20:00:00', 'hora_fin': '01:00:00', 'id_lugar': 740},
        {'id_show': 40708, 'id_evento': 13737, 'fecha': '2022-12-03', 'hora_inicio': '18:00:00', 'hora_fin': '00:00:00', 'id_lugar': 469},
        {'id_show': 95990, 'id_evento': 88750, 'fecha': '2022-05-20', 'hora_inicio': '20:00:00', 'hora_fin': '00:00:00', 'id_lugar': 156}
    ])
    conn.execute(asiento.insert(), [
        {'id_asiento': 1, 'fila': 1, 'numero': 40, 'id_zona': 24, 'id_lugar': 790},
        {'id_asiento': 2, 'fila': 1, 'numero': 59, 'id_zona': 24, 'id_lugar': 790},
        {'id_asiento': 3, 'fila': 1, 'numero': 89, 'id_zona': 25, 'id_lugar': 790},
        {'id_asiento': 4, 'fila': 1, 'numero': 41, 'id_zona': 25, 'id_lugar': 790},
        {'id_asiento': 5, 'fila': 1, 'numero': 3, 'id_zona': 26, 'id_lugar': 790},
        {'id_asiento': 6, 'fila': 1, 'numero': 11, 'id_zona': 26, 'id_lugar': 790},
        {'id_asiento': 7, 'fila': 1, 'numero': 24, 'id_zona': 6, 'id_lugar': 790},
        {'id_asiento': 8, 'fila': 1, 'numero': 56, 'id_zona': 6, 'id_lugar': 790},
        {'id_asiento': 9, 'fila': 1, 'numero': 28, 'id_zona': 2, 'id_lugar': 837},
        {'id_asiento': 10, 'fila': 1, 'numero': 19, 'id_zona': 2, 'id_lugar': 837},
        {'id_asiento': 11, 'fila': 1, 'numero': 16, 'id_zona': 27, 'id_lugar': 837},
        {'id_asiento': 12, 'fila': 1, 'numero': 75, 'id_zona': 27, 'id_lugar': 837},
        {'id_asiento': 13, 'fila': 1, 'numero': 98, 'id_zona': 28, 'id_lugar': 837},
        {'id_asiento': 14, 'fila': 1, 'numero': 20, 'id_zona': 28, 'id_lugar': 837},
        {'id_asiento': 15, 'fila': 1, 'numero': 56, 'id_zona': 1, 'id_lugar': 772},
        {'id_asiento': 16, 'fila': 1, 'numero': 37, 'id_zona': 1, 'id_lugar': 772},
        {'id_asiento': 17, 'fila': 1, 'numero': 13, 'id_zona': 1, 'id_lugar': 772},
        {'id_asiento': 18, 'fila': 1, 'numero': 30, 'id_zona': 3, 'id_lugar': 358},
        {'id_asiento': 19, 'fila': 1, 'numero': 53, 'id_zona': 3, 'id_lugar': 358},
        {'id_asiento': 20, 'fila': 1, 'numero': 13, 'id_zona': 4, 'id_lugar': 358},
        {'id_asiento': 21, 'fila': 1, 'numero': 15, 'id_zona': 4, 'id_lugar': 358},
        {'id_asiento': 22, 'fila': 1, 'numero': 32, 'id_zona': 5, 'id_lugar': 358},
        {'id_asiento': 23, 'fila': 1, 'numero': 8, 'id_zona': 1, 'id_lugar': 358},
        {'id_asiento': 24, 'fila': 1, 'numero': 52, 'id_zona': 2, 'id_lugar': 358},
        {'id_asiento': 25, 'fila': 1, 'numero': 83, 'id_zona': 2, 'id_lugar': 358},
        {'id_asiento': 26, 'fila': 1, 'numero': 62, 'id_zona': 3, 'id_lugar': 790},
        {'id_asiento': 27, 'fila': 1, 'numero': 64, 'id_zona': 3, 'id_lugar': 790},
        {'id_asiento': 28, 'fila': 1, 'numero': 34, 'id_zona': 6, 'id_lugar': 790},
        {'id_asiento': 29, 'fila': 1, 'numero': 6, 'id_zona': 6, 'id_lugar': 790},
        {'id_asiento': 30, 'fila': 1, 'numero': 17, 'id_zona': 7, 'id_lugar': 790},
        {'id_asiento': 31, 'fila': 1, 'numero': 37, 'id_zona': 1, 'id_lugar': 790},
        {'id_asiento': 32, 'fila': 1, 'numero': 66, 'id_zona': 29, 'id_lugar': 501},
        {'id_asiento': 33, 'fila': 1, 'numero': 82, 'id_zona': 29, 'id_lugar': 501},
        {'id_asiento': 34, 'fila': 1, 'numero': 3, 'id_zona': 8, 'id_lugar': 869},
        {'id_asiento': 35, 'fila': 2, 'numero': 88, 'id_zona': 9, 'id_lugar': 869},
        {'id_asiento': 36, 'fila': 3, 'numero': 14, 'id_zona': 10, 'id_lugar': 869},
        {'id_asiento': 37, 'fila': 4, 'numero': 99, 'id_zona': 11, 'id_lugar': 869},
        {'id_asiento': 38, 'fila': 5, 'numero': 42, 'id_zona': 12, 'id_lugar': 869},
        {'id_asiento': 39, 'fila': 6, 'numero': 4, 'id_zona': 13, 'id_lugar': 869},
        {'id_asiento': 40, 'fila': 7, 'numero': 33, 'id_zona': 14, 'id_lugar': 869},
        {'id_asiento': 41, 'fila': 8, 'numero': 18, 'id_zona': 15, 'id_lugar': 869},
        {'id_asiento': 42, 'fila': 1, 'numero': 11, 'id_zona': 16, 'id_lugar': 839},
        {'id_asiento': 43, 'fila': 2, 'numero': 64, 'id_zona': 6, 'id_lugar': 839},
        {'id_asiento': 44, 'fila': 3, 'numero': 78, 'id_zona': 1, 'id_lugar': 839},
        {'id_asiento': 45, 'fila': 4, 'numero': 64, 'id_zona': 2, 'id_lugar': 839},
        {'id_asiento': 46, 'fila': 5, 'numero': 78, 'id_zona': 17, 'id_lugar': 839},
        {'id_asiento': 47, 'fila': 6, 'numero': 64, 'id_zona': 25, 'id_lugar': 839},
        {'id_asiento': 48, 'fila': 7, 'numero': 12, 'id_zona': 18, 'id_lugar': 839},
        {'id_asiento': 49, 'fila': 8, 'numero': 46, 'id_zona': 19, 'id_lugar': 839},
        {'id_asiento': 50, 'fila': 1, 'numero': 83, 'id_zona': 26, 'id_lugar': 740},
        {'id_asiento': 51, 'fila': 1, 'numero': 14, 'id_zona': 21, 'id_lugar': 419},
        {'id_asiento': 52, 'fila': 1, 'numero': 28, 'id_zona': 22, 'id_lugar': 419},
        {'id_asiento': 53, 'fila': 1, 'numero': 86, 'id_zona': 23, 'id_lugar': 419},
        {'id_asiento': 54, 'fila': 1, 'numero': 92, 'id_zona': 20, 'id_lugar': 419},
        {'id_asiento': 55, 'fila': 1, 'numero': 39, 'id_zona': 29, 'id_lugar': 469},
        {'id_asiento': 56, 'fila': 1, 'numero': 86, 'id_zona': 29, 'id_lugar': 156}
        
    ])

    conn.execute(punto_venta.insert(), [
       {'id_pdv': 1, 'nombre': 'TicketShow', 'direccion': 'web', 'tipo': 'virtual'},
       {'id_pdv': 2, 'nombre': 'BuenPlan', 'direccion': 'web', 'tipo': 'virtual'},
       {'id_pdv': 3, 'nombre': 'Ticketfacil', 'direccion': 'web', 'tipo': 'virtual'},
       {'id_pdv': 4, 'nombre': 'Smartticket', 'direccion': 'web', 'tipo': 'virtual'},
       {'id_pdv': 5, 'nombre': 'Instaticket', 'direccion': 'web', 'tipo': 'virtual'},
       {'id_pdv': 6, 'nombre': 'Centralticket', 'direccion': 'web', 'tipo': 'virtual'},
       {'id_pdv': 7, 'nombre': 'Feelthetickets', 'direccion': 'web', 'tipo': 'virtual'}
        
    ])

    conn.execute(ticket.insert(), [
       {'codigo_barra': 117958, 'precio_unitario': 10, 'id_show': 39277, 'usuario': '2024', 'id_asiento': 1, 'num_factura': 5100, 'id_pdv': 1, 'estado': 'disponible'},
       {'codigo_barra': 224235, 'precio_unitario': 20, 'id_show': 39277, 'usuario': '8825', 'id_asiento': 2, 'num_factura': 1006, 'id_pdv': 2, 'estado': 'disponible'},
       {'codigo_barra': 523602, 'precio_unitario': 30, 'id_show': 65748, 'usuario': '8157', 'id_asiento': 11, 'num_factura': 5430, 'id_pdv': 3, 'estado': 'disponible'},
       {'codigo_barra': 313666, 'precio_unitario': 40, 'id_show': 65748, 'usuario': '9218', 'id_asiento': 12, 'num_factura': 6581, 'id_pdv': 7, 'estado': 'disponible'},
       {'codigo_barra': 607292, 'precio_unitario': 50, 'id_show': 29769, 'usuario': '1608', 'id_asiento': 19, 'num_factura': 8768, 'id_pdv': 6, 'estado': 'disponible'},
       {'codigo_barra': 223329, 'precio_unitario': 60, 'id_show': 29769, 'usuario': '6948', 'id_asiento': 20, 'num_factura': 6231, 'id_pdv': 5, 'estado': 'disponible'},
       {'codigo_barra': 620265, 'precio_unitario': 70, 'id_show': 41810, 'usuario': '1856', 'id_asiento': 43, 'num_factura': 6222, 'id_pdv': 4, 'estado': 'disponible'},
       {'codigo_barra': 222585, 'precio_unitario': 80, 'id_show': 41810, 'usuario': '5169', 'id_asiento': 44, 'num_factura': 5323, 'id_pdv': 3, 'estado': 'disponible'},
       {'codigo_barra': 752740, 'precio_unitario': 90, 'id_show': 26092, 'usuario': '7169', 'id_asiento': 52, 'num_factura': 9758, 'id_pdv': 2, 'estado': 'disponible'},
       {'codigo_barra': 860628, 'precio_unitario': 100, 'id_show': 26092, 'usuario': '9983', 'id_asiento': 53, 'num_factura': 8822, 'id_pdv': 1, 'estado': 'disponible'}
 
    ])

    conn.execute(factura.insert(), [
       {'num_factura': 5100, 'fecha': '2022-05-20', 'descripcion': 'venta de ticket para x evento', 'total': 100, 'forma_pago': 'debito', 'id_pdv': 1, 'usuario': '2024'},
       {'num_factura': 1006, 'fecha': '2022-04-19', 'descripcion': 'venta de ticket para x evento', 'total': 100, 'forma_pago': 'debito', 'id_pdv': 2, 'usuario': '8825'},
       {'num_factura': 5430, 'fecha': '2022-05-18', 'descripcion': 'venta de ticket para x evento', 'total': 100, 'forma_pago': 'debito', 'id_pdv': 3, 'usuario': '8157'},
       {'num_factura': 6581, 'fecha': '2022-06-17', 'descripcion': 'venta de ticket para x evento', 'total': 30, 'forma_pago': 'debito', 'id_pdv': 7, 'usuario': '9218'},
       {'num_factura': 8768, 'fecha': '2022-07-16', 'descripcion': 'venta de ticket para x evento', 'total': 30, 'forma_pago': 'debito', 'id_pdv': 6, 'usuario': '1608'},
       {'num_factura': 6231, 'fecha': '2022-08-15', 'descripcion': 'venta de ticket para x evento', 'total': 90, 'forma_pago': 'debito', 'id_pdv': 5, 'usuario': '6948'},
       {'num_factura': 6222, 'fecha': '2022-05-14', 'descripcion': 'venta de ticket para x evento', 'total': 100, 'forma_pago': 'debito', 'id_pdv': 4, 'usuario': '1856'},
       {'num_factura': 5323, 'fecha': '2022-04-13', 'descripcion': 'venta de ticket para x evento', 'total': 1000, 'forma_pago': 'debito', 'id_pdv': 3, 'usuario': '5169'},
       {'num_factura': 9758, 'fecha': '2022-06-12', 'descripcion': 'venta de ticket para x evento', 'total': 500, 'forma_pago': 'debito', 'id_pdv': 2, 'usuario': '7169'},
       {'num_factura': 8822, 'fecha': '2022-07-11', 'descripcion': 'venta de ticket para x evento', 'total': 600, 'forma_pago': 'debito', 'id_pdv': 1, 'usuario': '9983'}
       
    ])
     
