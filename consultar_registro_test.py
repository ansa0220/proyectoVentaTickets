

from conexion import generate_engine

engine = generate_engine("testNew")

from pprint import pprint
import os

import json
# funcion para limpiar la pantalla para cualquier sistema
def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')
clear()
with engine.connect() as conn:
    print("# Consultar registros de la tabla ticket con el id del punto de venta 3")
    result = conn.execute("SELECT * FROM ticket WHERE id_pdv = 3").mappings().all()
    
    pprint(result)

    print("# Obtener el total de las ventas en tickets")

    result = conn.execute("SELECT SUM(precio_unitario) FROM ticket").mappings().all()
    pprint(result)

    print("# Nombre de los shows del 2022")

    result = conn.execute("select nombre from evento join testnew.show on evento.id_evento = show.id_evento where year(fecha) = 2022 ").mappings().all()
    pprint(result)
    
    ###Views
    print('evento_show_lugar')
    result = conn.execute("select * from evento_show_lugar;").mappings().all()
    pprint(result)
    

    print('cliente_ticket_factura')
    result = conn.execute("select * from cliente_ticket_factura;").mappings().all()
    pprint(result)


    print('cliente_ticket_show')
    result = conn.execute("select * from cliente_ticket_show;").mappings().all()
    pprint(result)


    print('show_lugar_ciudad')
    result = conn.execute("select * from show_lugar_ciudad;").mappings().all()

    pprint(result)
                         
# -- 2 triggers
# delimiter |
# create trigger tr2_cliente before insert on cliente
# 	for each statement
#     begin
# 		if new.nombres is null then
# 			set new.nombres = new.'desconocido';
# 		elseif new.nombres not is null then
# 			set new.nombres = new.nombres;
# 	end |
# delimiter ;

# ###VISTAS
# create view evento_show_lugar as
# select evento.nombre as Nombre_evento, id_show as Identidad_show, lugar.nombre as Lugar_evento
# from testnew.show
# inner join evento on show.id_evento = evento.id_evento
# inner join lugar on show.id_lugar = lugar.id_lugar;

# create view cliente_ticket_factura as 
# select cedula as Cedula, codigo_barra as Codigo_ticket, id_factura as Factura
# from cliente
# inner join ticket on cliente.usuario = ticket.usuario
# inner join factura on cliente.usuario = factura.usuario;

# create view cliente_ticket_show as
# select nombres as Nombres, codigo_barra as Codigo_ticket, nombre as Evento
# from cliente
# inner join ticket on cliente.usuario = ticket.usuario
# inner join testnew.show on show.id_show = ticket.id_show
# inner join evento on show.id_evento = evento.id_evento;

# create view show_lugar_ciudad as
# select id_show as sshow, nombre as Lugar, ciudad as Ciudad
# from testnew.show
# inner join lugar on show.id_lugar = lugar.id_lugar
# inner join ciudad on lugar.id_ciudad = ciudad.id_ciudad;


# ###SP
# delimiter $$
# create procedure eventoinsert(id_eventoEvento integer(10), nombre varchar(100), descripcion varchar(100), imagen varchar(100), usuarioAdam varchar(100), usuarioPro varchar(100), fecha_registro date)
# begin
# 	set @var = (select id_evento from evento where id_evento = id_eventoEvento);
#     if @var != nombreEvento then
# 		insert into evento values (id_eventoEvento, nombre, descripcion, imagen, usuarioAdam, usuarioPro, fecha_registro);
# 	else
# 		signal sqlstate '02000' set message_text = 'evento ya existe';
# 	end if;
# end $$
# delimiter ;
