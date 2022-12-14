import os


def cotizar_evento():
    print("Cotización de eventos")
    lugar = input("Ingrese el lugar del evento: ")
    numero_tickets = input("Ingrese el número de tickets a vender: ")
    print("El costo de la cotización es de: $100")
    main()
    

def registrar_evento():
    print("Registro de eventos")
    lugar = input("Ingrese el lugar del evento: ")
    numero_tickets = input("Ingrese el número de tickets a vender: ")
    print("El evento ha sido registrado exitosamente")
    main()


def comprar_tickets():
    print("Compra de tickets")
    lugar = input("Ingrese el lugar del evento: ")
    numero_tickets = input("Ingrese el número de tickets a comprar: ")
    print("El costo de la compra es de: $100")
    main()

def mostrar_eventos():
    eventos = ["Evento 1", "Evento 2", "Evento 3"]
    for evento in eventos:
        print(evento)
    main()
    
def mostrar_eventos_por_fechas():
    eventos = ["Evento 1", "Evento 2", "Evento 3"]
    fechas = ["Fecha 1", "Fecha 2", "Fecha 3"]
    
    eventos_fechas =  zip(eventos, fechas)
    for evento,fecha in eventos_fechas:
        print("El evento " + evento + " se llevará a cabo el día " + fecha)
    main()
    

def mostrar_eventos_por_lugar():
    eventos = ["Evento 1", "Evento 2", "Evento 3"]
    lugares = ["Lugar 1", "Lugar 2", "Lugar 3"]
    
    eventos_lugares =  zip(eventos, lugares)
    for evento,lugar in eventos_lugares:
        print("El evento " + evento + " se llevará a cabo en el lugar " + lugar)
    main()

def consultar_eventos():
    print("Consultar eventos")
    print("1. Ver todos los eventos")
    print("2. Ver eventos por fecha")
    print("3. Ver eventos por lugar")
    print("4. Volver")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        print("Ver todos los eventos")
        mostrar_eventos()
    elif opcion == "2":
        print("Ver eventos por fecha")
        mostrar_eventos_por_fechas()
    elif opcion == "3":
        print("Ver eventos por lugar")
        mostrar_eventos_por_lugar()
    elif opcion == "4":
        main()
    else:
        print("Opción inválida")



def mostrar_todos_los_tickets():
    print("Ver todos los tickets")
    tickets= ["Ticket 1", "Ticket 2", "Ticket 3"]
    for ticket in tickets:
        print(ticket)
    main()

def mostrar_tickets_por_fecha():
    eventos = ["Evento 1", "Evento 2", "Evento 3"]
    tickets = ["Ticket 1", "Ticket 2", "Ticket 3"]
    fechas = ["Fecha 1", "Fecha 2", "Fecha 3"]
    
    tickets_fechas =  zip(eventos, tickets, fechas)
    for evento,ticket,fecha in tickets_fechas:
        print("El ticket " + ticket + " para el evento " + evento + " se llevará a cabo el día " + fecha)
    main()


def mostrar_tickets_por_lugar():
    eventos = ["Evento 1", "Evento 2", "Evento 3"]
    tickets = ["Ticket 1", "Ticket 2", "Ticket 3"]
    lugares = ["Lugar 1", "Lugar 2", "Lugar 3"]
    
    tickets_lugares =  zip(eventos, tickets, lugares)
    for evento,ticket,lugar in tickets_lugares:
        print("El ticket " + ticket + " para el evento " + evento + " se llevará a cabo en el lugar " + lugar)
    main()

def consultar_tickets():
    print("Consultar tickets")
    print("1. Ver todos los tickets")
    print("2. Ver tickets por fecha")
    print("3. Ver tickets por lugar")
    print("4. Volver")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        mostrar_todos_los_tickets()
    elif opcion == "2":
        mostrar_tickets_por_fecha()
    elif opcion == "3":
        mostrar_tickets_por_lugar()
    elif opcion == "4":
        main()
    else:
        print("Opción inválida")



def clear():
        os.system('cls' if os.name == 'nt' else 'clear')


tipoDeUsuario = ""


def main():
    global tipoDeUsuario
    print("Bienvenido a Ventas de tickets para x evento")
    if tipoDeUsuario=="":
        tipoDeUsuario = input("¿Eres invitado, cliente, productor o administrador? ")
    if tipoDeUsuario == "invitado":
        print("Bienvenido invitado")
        print("1. Consultar eventos")
        print("2. Consultar tickets")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            consultar_eventos()
        elif opcion == "2":
            consultar_tickets()
        elif opcion == "3":
            print("Saliendo...")
            exit()
        else:
            print("Opción inválida")
            main()

    elif tipoDeUsuario == "cliente":
        print("Bienvenido cliente")
        print("1. Consultar eventos")
        print("2. Consultar tickets")
        print("3. Comprar tickets")
        print("4. Ver perfil")
        print("5. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            consultar_eventos()
        elif opcion == "2":
            consultar_tickets()
        elif opcion == "3":
            comprar_tickets()
        elif opcion == "4":
            print("Ver perfil")
        elif opcion == "5":
            print("Saliendo...")
            exit()
        else:
            print("Opción inválida")
            main()

    elif tipoDeUsuario == "administrador":
        print("Bienvenido administrador")
    elif tipoDeUsuario == "productor":
        print("Bienvenido productor")
        print("1. Cotizar evento")
        print("2. Registrar evento")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            cotizar_evento()
        elif opcion == "2":
            registrar_evento()
        elif opcion == "3":
            print("Saliendo...")
            exit()
        else:
            print("Opción inválida")
            main()
        


clear()

main()



















