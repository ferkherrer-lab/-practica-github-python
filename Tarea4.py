import email
import logging
from abc import ABC, abstractmethod
from datetime import datetime

logging.basicConfig(
    filename='logs_sistema_software_fj.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def registrar_log(mensaje, nivel="info"):
  if nivel == "info":
        logging.info(mensaje)
  elif nivel == "error":
        logging.error(mensaje)
  elif nivel == "warning":
        logging.warning(mensaje)

  class tareaexception(Exception):
      pass
  class datosinvalidosexception(tareaexception):
      pass
  class servicionodisponibleexception(tareaexception):
      pass
  class reservainvalidaexception(tareaexception):
      pass
  
  class servicio(ABC):
    def __init__(self, nombre, tarifa, email):
        self.nombre = nombre
        self.tarifa = tarifa
        self.email = email

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, valor):
        if "@" not in valor or "." not in valor:
            raise datosinvalidosexception(f" el correo "{valor}"  no es valido ( falta @ )")
        self._email = valor
    
    class servicio(ABC):
        def __init__(self, nombre, costo_base):
             self.nombre = nombre
             self.costo_base = costo_base
          
    @abstractmethod
    def calcular_costo(self):
          pass

class reservasala(servicio):
    def calcular_costo(self, horas):
        if horas <= 0:
            raise ReservaError(" las hora de la reserva debe ser mayor a 0")
        return self.costo_base * horas
        
    def ejecutar_simulacion():
      print("=" * 75)
      print("SIMULACION DE SIMULACION SOFTWARE FJ")
      print("=" * 75 + "\n")
      
    cliente = {}
    servicios = []
    reservas = []
    reservasala = {}
    alquilerdeequpios =[]
    AsesoriaEspecializada = []
      
    print(" servicio 1: registrar cliente")
    try:
          c1 = cliente("Dario Gonzales", "Dario@gmail.com")
          cliente.append(c1)
          print(f"op 1 [OK] cliente registrado -> {c1.nombre}")
    except Exception as e:
        print(f"-> Error: {e}")
    else:
        print(f"-> [Else]: operacion completa sin errrores")
    finally:
        print("-> [finally] fin de operacion 1.\n")
        
    print(" servicio 2: registrar cliente")
    try:
          c2 = cliente("Duver arias", "Duver@gmail.com")
          cliente.append(c2)
    except Exception as e:
        print(f"-> [capturado]: Error -> {e}")
        logging.error (f"of 2 fallo: {e}")
    else:
        print("-> [Else]: ocurrio un error")
    finally:
        print("-> [finally]: fin de la operacion 2.\n")
        
    print(" servicio 3: crear un servicio de sala")
    try:
          r1 = reservasala("sala vip", 400.0)
          servicios.append(r1)
          print(f"-> ¡exito! servicio creado:{r1.nombre} a ${r1.costo_base}/hora")
    except Exception as e:
        print(f"-> Error: {e}")
    else:
        print(f"-> [Else]: servicio registrado correctamente")
    finally:
        print("-> [finally] fin de operacion 3.\n")
        
          
    print(" operacion 4: calcular el costo por horas en la sala")
    try:
        total = r1.calcular_costo (5)
        print(f"-> ¡Exito! costo por 5 horas: ${total}")
    except Exception as e:
            print(f"-> Error: {e}")
    else:
            print(f"-> [Else]: calculo realizado con exito")
    finally:
            print("-> [finally]: fin de la operacion 4.\n")

    print(" operacion 5: calcular costo de horas negativas")
    try:
        r1.calcular_costo(-2)
    except ReservaError as e:
        print(f"-> [capturado]: error  controlado -> {e}")
        logging.error(f"op 5 fallo: {e}")
    else:
        print("-> [Else]: no se ejecuta")
    finally:
        print("-> [finally]: fin de la operacion 5.\n")

    print(" operacion 6: registrar segundo cliente")
    try:
        c3 = cliente("maria torres", "maria@gmail.com")
        cliente.append(c3)
        print(f"-> ¡Exito! cliente creado: {c3.nombre}")
    except Exception as e:
        print(f"-> Error: {e}")
    else:
        print("-> [Else]: Estupendo")
    finally:
        print("-> [finally]: fin de la operacion 6.\n")
        
        
    print(" operacion 7: validar correo del cliente")
    try:
        c3.gmail = "correo incorrecto o faltan caracteres"
    except clienteerror as e:
        print(f"-> [capturado]: se detecto correo invalido ->{e}")
        logging.error(f"op 7 fallo: {e}")
    else:
        print("-> [Else]: modificacion")
    finally:
        print(f"-> [finally]: fin de la operacion 7.\n")
    
    print(" operacion 8: servicio de asesoria tecnica")
    try:
        r2 = reservasala("asesoria", 100.0)
        servicio.append(r2)
        print(f"-> ¡Exito! servicio {r2.nombre} creado")
    except Exception as e:
        print(f"-> Error: {e}")
    else:
        print("-> [Else]: operacion exitosa")
    finally:
        print("-> [finally]: fin de la opracion 8.\n")

    print(" operacion 9: calcular costo de asesoria")
    try:
        costo_asesoria = r2.calcular_costo(8)
        print(f"-> ¡Exito! costo total: ${costo_asesoria}")
    except Exception as e:
        print(f"-> Error: {e}")
    else:
        print("-> [Else]: Estupendo")
    finally:
        print("-> [finally]: fin de la opracion 9.\n")

    print(" operacion 10: simular errores del sistema")
    try:
        raise errorsoftwarefj("falla de simulacion")
    except errorsoftwarefj as e:
            print(f"-> [capturado]: error de sistema encontrado -> {e}")
            logging.critical(f"op 10 error critico: {e}")
    else:
        print("-> [Else]: no se encontraron errores")
    finally:
        print("-> [finally]: fin de la operacion 10 y cierre de simulacion.\n")

    print("\n" + "=" * 65)
    print(" Resumen: clientes guardados: {len(cliente)} | servicios: {len(servicio)}")
    print(" registro_errores.log")
    print(" SIMULACIÓN FINALIZADA CON ÉXITO ")
    print("=" * 65)

if __name__ == "__main__":  
    ejecutar_simulacion()
