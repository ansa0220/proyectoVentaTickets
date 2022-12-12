

from conexion import generate_engine

engine = generate_engine("testNew")

from pprint import pprint
import os


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
    result = conn.execute("SELECT * FROM ticket WHERE id_pdv = 3").mappings().all()
    pprint(result)
