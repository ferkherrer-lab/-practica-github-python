import logging
from abc import ABC, abstractmethod
from datetime import datetime

logging.basicConfig(
  filename='logs_tarea.log',
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

  class tareaexception(exception):
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
        self.correo = correo
          
    @abstractmethod
    def calcular_costo(self):
          pass

  class reservasala(servicio):
    def __init__(self, nombre, tarifa, horas):
        super().__init__(nombre, tarifa, correo)
        self.horas = horas

    def calcular_costo(self):
      return self.tarifa * self.horas

  class alquilerequipo(servicio):
    def __init__(self, nombre, tarifa, correo, dias):
        super().__init__(nombre, tarifa, correo)
        self.dias = dias

    def calcular_costo(self):
      return (self.tarifa * self.dias) * 1.15

  def ejecutar_simulacion():
      print("=" * 75)
      print("SIMULACION DE TAREA")
      print("=" * 75 + "\n")

      try:
          c1 = cliente("Dario Gonzales", "Dario@gmail.com")
          print(f"op 1 [OK] cliente registrado -> {c1.nombre}")
          logging.info(f"cliente registrado: {c1.nombre}")
      except logging.exception as e:
        print(e)
      try:
          c2 = cliente("Duver Arias", "correo_sin_arroba")
      except errortarea as e:
          print(f"op 2 [controlado]: {e}")
          logging.warning(str(e))
  
