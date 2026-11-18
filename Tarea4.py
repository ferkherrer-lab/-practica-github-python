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

class ReservaSala(Servicio):
    def calcular_costo(self, horas):
        if horas <= 0:
            raise ReservaError("Las horas de la reserva deben ser mayor a 0")
        return self.costo_base * horas

def ejecutar_operaciones():
    print("=" * 75)
    print("SIMULACION DE SIMULACION SOFTWARE FJ")
    print("=" * 75 + "\n")
    
    clientes = []
    servicios = []
    reservas = []

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

    print("servicio 3: crear un servicio de sala")
    try:
        r1 = ReservaSala("sala vip", 400.0)
        servicios.append(r1)
        print(f"-> ¡Éxito! servicio creado: {r1.nombre} a ${r1.costo_base}/hora")
    except Exception as e:
        print(f"-> Error: {e}")
    else:
        print("-> [Else]: servicio registrado correctamente")
    finally:
        print("-> [Finally] fin de operacion 3.\n")

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
        print("-> [Else]: Estupendo")
    finally:
        print("-> [Finally]: fin de la operacion 6.\n")

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

    print("operacion 8: servicio de asesoria tecnica")
    try:
        r2 = ReservaSala("asesoria", 100.0)
        servicios.append(r2)
        print(f"-> ¡Éxito! servicio {r2.nombre} creado")
    except Exception as e:
        print(f"-> Error: {e}")
    else:
        print("-> [Else]: operacion exitosa")
    finally:
        print("-> [Finally]: fin de la opracion 8.\n")

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
