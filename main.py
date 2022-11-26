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

def vender_tickets():
    print("Venta de tickets")
    lugar = input("Ingrese el lugar del evento: ")
    numero_tickets = input("Ingrese el número de tickets a vender: ")
    print("El evento ha sido registrado exitosamente")
    main()

def comprar_tickets():
    print("Compra de tickets")
    lugar = input("Ingrese el lugar del evento: ")
    numero_tickets = input("Ingrese el número de tickets a vender: ")
    print("El evento ha sido registrado exitosamente")
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
    elif opcion == "2":
        print("Ver eventos por fecha")
    elif opcion == "3":
        print("Ver eventos por lugar")
    elif opcion == "4":
        main()
    else:
        print("Opción inválida")


def consultar_tickets():
    print("Consultar tickets")
    print("1. Ver todos los tickets")
    print("2. Ver tickets por fecha")
    print("3. Ver tickets por lugar")
    print("4. Volver")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        print("Ver todos los tickets")
    elif opcion == "2":
        print("Ver tickets por fecha")
    elif opcion == "3":
        print("Ver tickets por lugar")
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



















