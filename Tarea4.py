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
    def __init__(self, nombre, tarifa):
        self.nombre = nombre
        self.tarifa = tarifa
          
    @abstractmethod
    def calcular_costo(self):
          pass

  class reservasala(servicio):
    def __init__(self, nombre, tarifa, horas):
        super().__init__(nombre, tarifa)
        self.horas = horas

    def calcular_costo(self):
      return self.tarifa * self.horas

  class alquilerequipo(servicio):
    def __init__(self, nombre, tarifa, dias):
        super().__init__(nombre, tarifa)
        self.dias = dias

    def calcular_costo(self):
      return (self.tarifa * self.dias) * 1.15
    
    def ejecutar_simulacion():
      print("=" * 75)
      print("SIMULACION DE TAREA")
      print("=" * 75 + "\n")
      
      clientes = {}
      servicios = {}
      reservas = []
      reservasalas = []
      alquilerdeequpios =[]
      AsesoriaEspecializada = []
      try:
          c1 = clientes("Dario Gonzales", "Dario@gmail.com")
          print(f"op 1 [OK] cliente registrado -> {c1.nombre}")
          logging.info(f"cliente registrado: {c1.nombre}")
      except logging.exception as e:
        print(e)
        
      try:
           c2 = clientes("Duver Arias", "correo_sin_arroba")
      except tareaexception as e:
          print(f"op 2 [controlado]: {e}")
          logging.warning(str(e))
          
      try:
          r1 = reservasalas(101, "sala vip", tarifa_base=500.0, capacidad_personas=12)
          servicios[r1.id_entidad] = r1
          print(f"op 3 [OK]: {r1.obtener_resumen()}")
          registrar_log(f"servicio creado: {r1.nombre_servicio}")
      except logging.exceptionxception as e:
          print(f"op 3 [error]; {e}")
          
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
