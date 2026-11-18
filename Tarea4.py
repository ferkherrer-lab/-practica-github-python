import logging
from abc import ABC, abstractmethod
from datetime import datetime

logging.basicConfig(
    filename='logs_sistema_software_fj.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

class errorsoftwarefj(Exception):
    pass

class ClienteError(errorsoftwarefj):
    pass

class ReservaError(errorsoftwarefj):
    pass

class Cliente:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if "@" not in valor or "." not in valor:
            raise ClienteError(f"El correo {valor} no es valido (falta @ .)")
        self._email = valor

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if not str(valor).isdigit() or len(str(valor)) < 7:
            raise ClienteError(f"El teléfono {valor} no es válido (debe tener al menos 7 dígitos)")
        self._telefono = str(valor)

class Servicio(ABC):
    def __init__(self, nombre, costo_base):
        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, horas):
        pass

class SalaPequena(Servicio):
    def __init__(self, costo_base=150.0):
        super().__init__("Sala Pequeña", costo_base)

    def calcular_costo(self, horas, descuento_porcentaje: float = 0.0):
        if horas <= 0:
            raise ReservaError("Las horas de la reserva deben ser mayores a 0.")
        costo = self.costo_base * horas
        if descuento_porcentaje > 0:
            costo -= costo * (descuento_porcentaje / 100.0)
        return max(0.0, costo)

class SalaMediana(Servicio):
    def __init__(self, costo_base=250.0):
        super().__init__("Sala Mediana", costo_base)

    def calcular_costo(self, horas, incluye_coffee_break: bool = False):
        if horas <= 0:
            raise ReservaError("Las horas de la reserva deben ser mayores a 0.")
        costo = self.costo_base * horas
        if incluye_coffee_break:
            costo += 50.0 
        return costo

class SalaVIP(Servicio):
    def __init__(self, costo_base=400.0):
        super().__init__("Sala VIP", costo_base)

    def calcular_costo(self, horas, incluye_proyector_avanzado: bool = True):
        if horas <= 0:
            raise ReservaError("Las horas de la reserva deben ser mayores a 0.")
        costo = self.costo_base * horas
        if incluye_proyector_avanzado:
            costo += 80.0  
        return costo

def ejecutar_operaciones():
    print("=" * 75)
    print("SIMULACION DE SIMULACION SOFTWARE FJ")
    print("=" * 75 + "\n")
    
    clientes = []
    servicios = []
    reservas = []

    # operacion 1: registrar cliente
    print("servicio 1: registrar cliente")
    try:
        c1 = Cliente("Dario Gonzales", "Dario@gmail.com", "3101234567")
        clientes.append(c1)
        print(f"-> ¡Éxito! cliente creado: {c1.nombre}")
        print(f"   Gmail: {c1.email}")
        print(f"   Teléfono: {c1.telefono}")
    except Exception as e:
        print(f"-> Error: {e}")
    else:
        print("-> [Else]: operacion completa sin errores")
    finally:
        print("-> [Finally] fin de operacion 1.\n")
        
    # operacion 2: registrar cliente con correo invalido
    print("servicio 2: registrar cliente")
    try:
        c2 = Cliente("Duver arias", "Duver-email.com", "3209876543")
        clientes.append(c2)
    except Exception as e:
        print(f"-> [capturado]: Error -> {e}")
        logging.error(f"op 2 fallo: {e}")
    else:
        print("-> [Else]: ocurrio un error")
    finally:
        print("-> [finally]: fin de la operacion 2.\n")
        
    # operacion 3: crear un servicio de sala
    print("servicio 3: crear un servicio de sala")
    try:
        r1 = SalaVIP(400.0)
        servicios.append(r1)
        print(f"-> ¡Éxito! servicio creado: {r1.nombre} a ${r1.costo_base}/hora")
    except Exception as e:
        print(f"-> Error: {e}")
    else:
        print("-> [Else]: servicio registrado correctamente")
    finally:
        print("-> [Finally] fin de operacion 3.\n")

    # operacion 4: calcular el costo por horas en la sala
    print("operacion 4: calcular el costo por horas en la sala")
    try:
        total = r1.calcular_costo(5)
        print(f"-> ¡Éxito! costo por 5 horas: ${total}")
    except Exception as e:
        print(f"-> Error: {e}")
    else:
        print("-> [Else]: calculo realizado con exito")
    finally:
        print("-> [Finally] fin de operacion 4.\n")

    # operacion 5: calcular costo de horas negativas
    print("operacion 5: calcular costo de horas negativas")
    try:
        r1.calcular_costo(-2)
    except ReservaError as e:
        print(f"-> [capturado]: error controlado -> {e}")
        logging.error(f"op 5 fallo: {e}")
    else:
        print("-> [Else]: no se ejecuta")
    finally:
        print("-> [Finally]: fin de la operacion 5.\n")

    # operacion 6: registrar segundo cliente
    print("operacion 6: registrar segundo cliente")
    try:
        c3 = Cliente("maria torres", "maria@gmail.com", "3207654321")
        clientes.append(c3)
        print(f"-> ¡Éxito! cliente creado: {c3.nombre}")
        print(f"   Gmail: {c3.email}")
        print(f"   Teléfono: {c3.telefono}")
    except Exception as e:
        print(f"-> Error: {e}")
    else:
        print("-> [Else]: GENIAL")
    finally:
        print("-> [Finally]: fin de la operacion 6.\n")

    # operacion 7: validar correo del cliente
    print("operacion 7: validar correo del cliente")
    try:
        c3.email = "correo-malo"
    except ClienteError as e:
        print(f"-> [capturado]: se detecto correo invalido -> {e}")
        logging.error(f"op 7 fallo: {e}")
    else:
        print("-> [Else]: modificacion")
    finally:
        print("-> [Finally]: fin de la operacion 7.\n")

    # operacion 8: servicio de asesoria tecnica
    print("operacion 8: servicio de asesoria tecnica")
    try:
        r2 = SalaPequena(100.0)
        servicios.append(r2)
        print(f"-> ¡Éxito! servicio {r2.nombre} creado")
    except Exception as e:
        print(f"-> Error: {e}")
    else:
        print("-> [Else]: operacion exitosa")
    finally:
        print("-> [Finally]: fin de la opracion 8.\n")

    # operacion 9: calcular costo de asesoria
    print("operacion 9: calcular costo de asesoria")
    try:
        costo_asesoria = r2.calcular_costo(8)
        print(f"-> ¡Éxito! costo total: ${costo_asesoria}")
    except Exception as e:
        print(f"-> Error: {e}")
    else:
        print("-> [Else]: Estupendo")
    finally:
        print("-> [Finally]: fin de la operacion 9.\n")

    # operacion 10: simular errores del sistema
    print("operacion 10: simular errores del sistema")
    try:
        raise errorsoftwarefj("falla de simulacion")
    except errorsoftwarefj as e:
        print(f"-> [capturado]: error de sistema encontrado -> {e}")
        logging.critical(f"op 10 error critico: {e}")
    else:
        print("-> [Else]: no se encontraron errores")
    finally:
        print("-> [Finally]: fin de la operacion 10 y cierre de simulacion.\n")

    print("\n" + "=" * 65)
    print(f"Resumen: clientes guardados: {len(clientes)} | servicios: {len(servicios)}")
    print("Se ha generado el archivo de registro: logs_sistema_software_fj.log")
    print("SIMULACIÓN FINALIZADA CON ÉXITO")
    print("=" * 65)

if __name__ == "__main__":
    ejecutar_operaciones()
