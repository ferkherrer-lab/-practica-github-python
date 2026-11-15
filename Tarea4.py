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
    reservasalas = []
    alquilerdeequpios =[]
    AsesoriaEspecializada = []
      
    print(" servicio 1: registrar cliente ")
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
        
    print(" servicio 2: registrar cliente con correo inavildo")
    try:
          c2 = cliente("Duver arias", "Duver-gmail.com")
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
          r1 = reservarsala("sala vip", 400.0)
          servicios.append(r1)
          print(f"-> ¡exito! servicio creado:{r1.nombre} a $[r1.costo_base}/hora")
    except Exception as e:
        print(f"-> Error: {e}")
    else:
        print(f"-> [Else]: servicio registrado correctamente")
    finally:
        print("-> [finally] fin de operacion 3.\n")

    print(" operacion 4: calcular el costo por horas en la sala")
    try:
        total = r1.calcular_costo (5)
            print(f"-> ¡Exito! costo por 5 horas: ${total]")
    except Exception as e:
            print(f"-> Error: {e}")
    else:
            print(f"-> [Else]: calculo realizado con exito")
    finally:
            print("-> [finally]: fin de la operacion 4.\n")

    print(" operacion 5: calcular costo de horas negativas")
    try:
        r1.calcular_costo(-2)
    except reservaerror as e:
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
        print("-> Error: {e}2)
    else:
        print("-> [Else]: Estupendo")
    finally:
        print("-> [finally]: fin de la operacion 6.\n")
        
      try:
          r2 = alquilerdeequpios(102, "sonido+proyector+computador", tarifa_base=30.0, seguro_incluido=True)
          servicios[r2.id_entidad] = r2
          print(f"op 4 [OK]: {r2.obtener_resumen()}")
          registrar_log(f"servicio creado: {r2.nombre_servicio}")
      except logging.exception as e:
          print(f"op 4 [error]: {e}")
          
      try:
          r3 = reservasala(104, "sala economica", tarifa_base=300.0, capacidad_personas=6)
          servicios[r3.id_entidad] = r3
          print(f"op 5 [OK]: {r3.obtener_resumen()}")
          registrar_log(f"servicio creado: {r3.nombre_servicio}")
      except logging.exception as e:
          print(f"op 5 [error]; {e}")
          
      try:
          s1 = reservas(501, clientes[1], servicio[101], duracion_unidades=4)
          s1.procesar_reserva(tasa_inpuestos=0.19, descuento=0.10)
          reservas.append(s1)
          print("op 6 [OK]: reserva procesada correctamente")
      except logging.exception as e:
          print(f"op 6 [error]: {e}")
          
      try:
          s2 = reservas(502, clientes[1], servicio[103], duracion_unidades=2)
          s2.procesar_reserva(tasa_inpuestos=0.19, descuento=0.10)
          reservas.append(s2)
      except reservainvalidaexception as e:
          msg=f"op 7[controlado] fallo inesperado duracion invalida -> {e}"
          print(msg)
      try:
          s3 = AsesoriaEspecializada(104, "Asesoría Ciberseguridad", tarifa_base=80.0, especialista="Dra. López", disponible=True)
          r3 = reservas(504, clientes[1], s3, duracion_unidades=3)
          r3.procesar_reserva(nivel_urgencia="alta")
          reservas.append(r3)
          r3.cancelar_reserva()
          print("Op 7 [OK]: Reserva creada, procesada y cancelada correctamente.")
      except Exception as e:
          print(f"Op 7 [error]: {e}")

      print("\n" + "=" * 65)
      print(" SIMULACIÓN FINALIZADA CON ÉXITO ")
      print("=" * 65)

if __name__ == "__main__":  
    ejecutar_simulacion()
