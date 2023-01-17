

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
    
    ###TRIGGERS
    result = com.execute("delimiter | create trigger tr1_lugar_show before insert on ciudad for each statement begin if new.ciudad is null then set new.ciudad = new.'ciudad desconocida'; elseif new ciudad is not null then set new.ciudad = new.ciudad; end | delimiter ;").mappings().all()
     pprint(result)
                         
-- 2 triggers
delimiter |
create trigger tr2_cliente before insert on cliente
	for each statement
    begin
		if new.nombres is null then
			set new.nombres = new.'desconocido';
		elseif new.nombres not is null then
			set new.nombres = new.nombres;
	end |
delimiter ;
