from sqlalchemy import create_engine, Table, MetaData,select
import pymysql

from sqlalchemy.exc import OperationalError


conf ={
	'db_name': 'testNew',
	'user': 'root',
	'password': 'root',
	'url': 'localhost:3306/'
}


def generate_engine(custom_db = None):
	db_name = "" if custom_db is None else custom_db
	engine = create_engine( f"mysql+pymysql://{conf['user']}:{conf['password']}@{conf['url']}{db_name}")
	return engine

def remove_database(custom_db):
	engine = generate_engine()
	with engine.connect() as conn:
		conn.execute(f"drop database {custom_db}")
	engine.dispose()


def show_databases():
	engine = generate_engine()
	with engine.connect() as conn:
		results = conn.execute(f"show databases")
		for name, in results:
			print(name)
	engine.dispose()



# ejemplo
def execute(consulta = "" ,custom_db = None):
	db_name = f"{conf[db_name]}" if custom_db is None else custom_db
	engine = generate_engine(db_name)
	with engine.connect() as conn:
		results	= conn.execute(consulta)
	engine.dispose()
	return results




def connect_or_create_database():
	db_name	 = conf['db_name']
	engine = None
	try:
		engine = generate_engine(db_name)
		with engine.connect() as conn:
			print("Conexion realizada con exito")
	except OperationalError as exc:
		if "Unknown database" in exc.__str__():
			engine = generate_engine()
			with engine.connect() as conn:
				conn.execute("commit")
				conn.execute(f"create database {db_name}")
			print(f"Database {db_name} creada con exito")
		else:
			raise exc
	engine.dispose()

show_databases()
connect_or_create_database()
show_databases()



# apellido = input('Ingrese el apellido del empleado a buscar:')
# # Build select statement for census table: stmt
# stmt = "select first_name, last_name from employees where last_name = '"+ apellido + "'"

# # Execute the statement on connection and fetch 10 records: result
# results = connection.execute(stmt).fetchmany(size=10)

# # Execute the statement and print the results
# print(results)

# for emp_name,emp_lastname in results:
#     print(emp_name,emp_lastname)

# connection.close()
