class Cliente:
    def __init__(self, nombre, apellido, contacto_emergencia, discapacidad):
        self.nombre = nombre
        self.apellido = apellido
        self.contacto_emergencia = contacto_emergencia
        self.discapacidad = discapacidad

class NodoAsiento:
    def __init__(self, fila, asiento, cliente=None):
        self.fila = fila
        self.asiento = asiento
        self.cliente = cliente
        self.siguiente = None

class SalaCine:
    def __init__(self, filas, asientos_por_lado, asientos_discapacitados):
        self.filas = filas
        self.asientos_por_lado = asientos_por_lado
        self.asientos_discapacitados = asientos_discapacitados
        self.capacidad_total = filas * asientos_por_lado * 2
        self.primer_asiento = None

    def mostrar_estado_sala(self):
        print("Estado actual de la sala:")
        actual = self.primer_asiento
        for fila in range(1, self.filas + 1):
            fila_str = ""
            for asiento in range(1, self.asientos_por_lado * 2 + 1):
                if actual is not None and actual.fila == fila and actual.asiento == asiento:
                    if actual.cliente:
                        fila_str += "X "
                    else:
                        fila_str += "R "
                    actual = actual.siguiente
                else:
                    fila_str += "O "
            print("Fila {}: {}".format(fila, fila_str))

    def buscar_asiento(self, fila, asiento):
        actual = self.primer_asiento
        while actual is not None:
            if actual.fila == fila and actual.asiento == asiento:
                return actual
            actual = actual.siguiente
        return None

    def reservar_asiento(self, fila, asiento, cliente):
        if fila < 1 or fila > self.filas or asiento < 1 or asiento > self.asientos_por_lado * 2:
            print("Fila o asiento fuera de rango.")
            return False
        elif self.buscar_asiento(fila, asiento):
            print("Lo siento, este asiento ya está ocupado o reservado.")
            return False
        elif (fila, asiento) in self.asientos_discapacitados and not cliente.discapacidad:
            print("Lo siento, este asiento es para personas con discapacidad.")
            return False
        elif cliente.discapacidad and (fila, asiento) not in self.asientos_discapacitados:
            print("Lo siento, solo puede reservar asientos para personas con discapacidad.")
            return False
        else:
            nuevo_asiento = NodoAsiento(fila, asiento, cliente)
            if not self.primer_asiento or (fila < self.primer_asiento.fila or
                                            (fila == self.primer_asiento.fila and asiento < self.primer_asiento.asiento)):
                nuevo_asiento.siguiente = self.primer_asiento
                self.primer_asiento = nuevo_asiento
            else:
                actual = self.primer_asiento
                while actual.siguiente and (fila > actual.siguiente.fila or
                                            (fila == actual.siguiente.fila and asiento > actual.siguiente.asiento)):
                    actual = actual.siguiente
                nuevo_asiento.siguiente = actual.siguiente
                actual.siguiente = nuevo_asiento
            print("¡Reserva realizada con éxito!")
            self.mostrar_estado_sala()
        return True

    def cancelar_reserva(self, fila, asiento):
        anterior = None
        actual = self.primer_asiento
        while actual is not None:
            if actual.fila == fila and actual.asiento == asiento:
                if anterior is None:
                    self.primer_asiento = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                print("¡Reserva cancelada con éxito!")
                self.mostrar_estado_sala()
                return
            anterior = actual
            actual = actual.siguiente
        print("No se encontró ninguna reserva en este asiento.")