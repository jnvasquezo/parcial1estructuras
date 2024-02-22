from sala_cine import SalaCine, Cliente 

def obtener_datos_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    contacto_emergencia = input("Ingrese el contacto de emergencia del cliente: ")
    discapacidad = input("¿El cliente presenta alguna discapacidad? (Sí/No): ").lower() == "si"
    return Cliente(nombre, apellido, contacto_emergencia, discapacidad)

def main():
    filas = int(input("Ingrese la cantidad de filas en la sala de cine: "))
    asientos_por_lado = int(input("Ingrese la cantidad de asientos por lado en la sala de cine: "))
    num_asientos_discapacitados = int(input("Ingrese la cantidad de asientos para personas con discapacidad: "))
    asientos_discapacitados = []
    for _ in range(num_asientos_discapacitados):
        fila = int(input("Ingrese la fila del asiento para persona con discapacidad: "))
        asiento = int(input("Ingrese el número del asiento para persona con discapacidad: "))
        asientos_discapacitados.append((fila, asiento))
    sala = SalaCine(filas, asientos_por_lado, asientos_discapacitados)

    # Mostramos el estado inicial de la sala
    sala.mostrar_estado_sala()

    while True:
        opcion = input("\n¿Qué acción desea realizar? (reservar/cancelar/Emergencia/salir/mostrar/pelicula): ").lower()
        if opcion == "reservar":
            fila = int(input("Ingrese la fila del asiento a reservar: "))
            asiento = int(input("Ingrese el número del asiento a reservar: "))
            cliente = obtener_datos_cliente()
            sala.reservar_asiento(fila, asiento, cliente)
        elif opcion == "cancelar":
            fila = int(input("Ingrese la fila del asiento a cancelar: "))
            asiento = int(input("Ingrese el número del asiento a cancelar: "))
            sala.cancelar_reserva(fila, asiento)
        elif opcion == "emergencia":
            print("Información de contacto de emergencia de las personas que han reservado:")
            for nodo_asiento in sala.iterar_asientos():
                if nodo_asiento.cliente:
                    print("Nombre: {}, Apellido: {}, Contacto de Emergencia: {}".format(nodo_asiento.cliente.nombre, nodo_asiento.cliente.apellido, nodo_asiento.cliente.contacto_emergencia))
        elif opcion == "mostrar":
            sala.mostrar_estado_sala()
        elif opcion == "pelicula":
            sala.mostrar_estado_sala()
            print("todos estan disfrutando de la increible pelicula de linterna verde")
            for nodo_asiento in sala.iterar_asientos():
                if nodo_asiento.cliente:
                    print("Nombre: {}, Apellido: {},".format(nodo_asiento.cliente.nombre, nodo_asiento.cliente.apellido))
        elif opcion == "salir":
            break
        else:
            print("Opción no válida. Por favor, ingrese 'reservar', 'cancelar' o 'salir'.")

if __name__ == "__main__":
    main()
