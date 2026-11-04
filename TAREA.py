import logging
from abc import ABC, abstractmethod
from datetime import datetime

# ==========================================
# 1. CONFIGURACIÓN DEL SISTEMA DE LOGS
# ==========================================
logging.basicConfig(
    filename='sistema_software_fj.log',
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

# ==========================================
# 2. EXCEPCIONES PERSONALIZADAS
# ==========================================
class SoftwareFJException(Exception):
    """Clase base para excepciones del sistema."""
    pass

class DatosInvalidosException(SoftwareFJException):
    """Excepción para datos de entrada no válidos."""
    pass

class ServicioNoDisponibleException(SoftwareFJException):
    """Excepción cuando un servicio no está disponible o activo."""
    pass

class ReservaInvalidaException(SoftwareFJException):
    """Excepción para errores en el proceso o parámetros de reserva."""
    pass


# ==========================================
# 3. CLASES BASE Y ENTIDADES
# ==========================================
class EntidadBase(ABC):
    """Clase abstracta base para entidades generales del sistema."""
    def __init__(self, id_entidad):
        self._id_entidad = id_entidad

    @property
    def id_entidad(self):
        return self._id_entidad

    @abstractmethod
    def obtener_resumen(self):
        pass


class Cliente(EntidadBase):
    """Clase Cliente con encapsulación y validaciones estrictas."""
    def __init__(self, id_cliente, nombre, correo):
        super().__init__(id_cliente)
        self.nombre = nombre
        self.correo = correo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not isinstance(valor, str) or len(valor.strip()) < 3:
            raise DatosInvalidosException("El nombre del cliente debe tener al menos 3 caracteres.")
        self._nombre = valor.strip()

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if not valor or "@" not in valor or "." not in valor:
            raise DatosInvalidosException(f"Correo electrónico inválido: '{valor}'")
        self._correo = valor.strip()

    def obtener_resumen(self):
        return f"Cliente ID: {self.id_entidad} | Nombre: {self.nombre} | Email: {self.correo}"


# ==========================================
# 4. JERARQUÍA DE SERVICIOS (POLIMORFISMO)
# ==========================================
class Servicio(EntidadBase):
    """Clase abstracta Servicio."""
    def __init__(self, id_servicio, nombre_servicio, tarifa_base, disponible=True):
        super().__init__(id_servicio)
        self.nombre_servicio = nombre_servicio
        if tarifa_base <= 0:
            raise DatosInvalidosException("La tarifa base debe ser un valor positivo mayor a 0.")
        self.tarifa_base = tarifa_base
        self.disponible = disponible

    @abstractmethod
    def calcular_costo(self, *args, **kwargs):
        """Método abstracto para calcular costos con polimorfismo."""
        pass

    def obtener_resumen(self):
        estado = "Disponible" if self.disponible else "No Disponible"
        return f"Servicio: {self.nombre_servicio} (ID: {self.id_entidad}) - Base: ${self.tarifa_base:.2f} [{estado}]"


class ReservaSalas(Servicio):
    """Servicio 1: Reserva de Salas."""
    def __init__(self, id_servicio, nombre_servicio, tarifa_base, capacidad_personas, disponible=True):
        super().__init__(id_servicio, nombre_servicio, tarifa_base, disponible)
        self.capacidad_personas = capacidad_personas

    def calcular_costo(self, horas, tasa_impuesto=0.19, descuento=0.0):
        """Calcula el costo total considerando horas, impuestos y opcionalmente descuento."""
        if horas <= 0:
            raise DatosInvalidosException("Las horas de reserva de sala deben ser mayores a 0.")
        subtotal = (self.tarifa_base * horas) * (1 - descuento)
        return subtotal * (1 + tasa_impuesto)


class AlquilerEquipos(Servicio):
    """Servicio 2: Alquiler de Equipos."""
    def __init__(self, id_servicio, nombre_servicio, tarifa_base, seguro_incluido=True, disponible=True):
        super().__init__(id_servicio, nombre_servicio, tarifa_base, disponible)
        self.seguro_incluido = seguro_incluido

    def calcular_costo(self, dias, deposito_garantia=50.0, tasa_impuesto=0.19):
        """Calcula costo según días, agregando seguro/depósito e impuestos."""
        if dias <= 0:
            raise DatosInvalidosException("Los días de alquiler deben ser mayores a 0.")
        costo_base = self.tarifa_base * dias
        costo_seguro = 20.0 if self.seguro_incluido else 0.0
        subtotal = costo_base + costo_seguro + deposito_garantia
        return subtotal * (1 + tasa_impuesto)


class AsesoriaEspecializada(Servicio):
    """Servicio 3: Asesorías Especializadas."""
    def __init__(self, id_servicio, nombre_servicio, tarifa_base, especialista, disponible=True):
        super().__init__(id_servicio, nombre_servicio, tarifa_base, disponible)
        self.especialista = especialista

    def calcular_costo(self, horas, nivel_urgencia="Normal", tasa_impuesto=0.19):
        """Calcula costo según urgencia."""
        if horas <= 0:
            raise DatosInvalidosException("Las horas de asesoría deben ser mayores a 0.")
        multiplicador = 1.5 if nivel_urgencia.lower() == "alta" else 1.0
        subtotal = (self.tarifa_base * horas) * multiplicador
        return subtotal * (1 + tasa_impuesto)


# ==========================================
# 5. CLASE RESERVA
# ==========================================
class Reserva:
    """Clase Reserva que integra Cliente, Servicio, Duración y Estado."""
    def __init__(self, id_reserva, cliente, servicio, duracion_unidades):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion_unidades = duracion_unidades
        self.estado = "Pendiente"
        self.costo_total = 0.0

    def procesar_reserva(self, **kwargs):
        """Procesa y confirma la reserva aplicando bloques try/except/else/finally."""
        try:
            if not self.servicio.disponible:
                raise ServicioNoDisponibleException(f"El servicio '{self.servicio.nombre_servicio}' no se encuentra disponible.")

            # Cálculo de costo dinámico según el servicio
            self.costo_total = self.servicio.calcular_costo(self.duracion_unidades, **kwargs)

        except (ServicioNoDisponibleException, DatosInvalidosException) as e:
            self.estado = "Fallida"
            msg = f"Error al procesar Reserva #{self.id_reserva}: {str(e)}"
            registrar_log(msg, nivel="error")
            # Encadenamiento de excepciones
            raise ReservaInvalidaException(f"No se pudo completar la reserva #{self.id_reserva}") from e

        else:
            self.estado = "Confirmada"
            msg = f"Reserva #{self.id_reserva} confirmada con éxito. Cliente: {self.cliente.nombre}. Total: ${self.costo_total:.2f}"
            print(f"[ÉXITO] {msg}")
            registrar_log(msg, nivel="info")

        finally:
            registrar_log(f"Finalizado intento de procesamiento para la Reserva #{self.id_reserva}.", nivel="info")

    def cancelar_reserva(self):
        self.estado = "Cancelada"
        msg = f"Reserva #{self.id_reserva} ha sido cancelada."
        print(f"[INFO] {msg}")
        registrar_log(msg, nivel="info")


# ==========================================
# 6. SIMULACIÓN DE 10 OPERACIONES COMPLETAS
# ==========================================
def ejecutar_simulacion():
    print("=" * 65)
    print("  INICIANDO SISTEMA INTEGRAL DE GESTIÓN DE SOFTWARE FJ")
    print("=" * 65 + "\n")

    clientes = {}
    servicios = {}
    reservas = []

    # ----------------------------------------------------
    # OPERACIÓN 1: Registro correcto de Cliente (VÁLIDO)
    # ----------------------------------------------------
    try:
        c1 = Cliente(1, "Carlos Mendoza", "carlos@mail.com")
        clientes[c1.id_entidad] = c1
        print(f"Op 1 [OK]: {c1.obtener_resumen()}")
        registrar_log(f"Cliente registrado: {c1.nombre}")
    except Exception as e:
        print(f"Op 1 [ERROR]: {e}")

    # ----------------------------------------------------
    # OPERACIÓN 2: Intento de Registro de Cliente con Email Inválido (FALLIDO)
    # ----------------------------------------------------
    try:
        c2 = Cliente(2, "Ana Gómez", "correo_invalido_sin_arroba")
        clientes[c2.id_entidad] = c2
    except DatosInvalidosException as e:
        msg = f"Op 2 [CONTROLADO]: Fallo esperado al registrar cliente -> {e}"
        print(msg)
        registrar_log(msg, nivel="warning")

    # ----------------------------------------------------
    # OPERACIÓN 3: Creación del Servicio 1 - Sala de Juntas (VÁLIDO)
    # ----------------------------------------------------
    try:
        s1 = ReservaSalas(101, "Sala VIP Ejecutiva", tarifa_base=50.0, capacidad_personas=12)
        servicios[s1.id_entidad] = s1
        print(f"Op 3 [OK]: {s1.obtener_resumen()}")
        registrar_log(f"Servicio creado: {s1.nombre_servicio}")
    except Exception as e:
        print(f"Op 3 [ERROR]: {e}")

    # ----------------------------------------------------
    # OPERACIÓN 4: Creación del Servicio 2 - Alquiler de Equipo (VÁLIDO)
    # ----------------------------------------------------
    try:
        s2 = AlquilerEquipos(102, "Proyector 4K + Sonido", tarifa_base=30.0, seguro_incluido=True)
        servicios[s2.id_entidad] = s2
        print(f"Op 4 [OK]: {s2.obtener_resumen()}")
        registrar_log(f"Servicio creado: {s2.nombre_servicio}")
    except Exception as e:
        print(f"Op 4 [ERROR]: {e}")

    # ----------------------------------------------------
    # OPERACIÓN 5: Creación del Servicio 3 - Asesoría No Disponible (VÁLIDO REGISTRO, NO DISPONIBLE)
    # ----------------------------------------------------
    try:
        s3 = AsesoriaEspecializada(103, "Consultoría Arquitectura Cloud", tarifa_base=100.0, especialista="Ing. Silva", disponible=False)
        servicios[s3.id_entidad] = s3
        print(f"Op 5 [OK]: {s3.obtener_resumen()}")
        registrar_log(f"Servicio creado: {s3.nombre_servicio}")
    except Exception as e:
        print(f"Op 5 [ERROR]: {e}")

    # ----------------------------------------------------
    # OPERACIÓN 6: Intento de Creación de Servicio con Tarifa Inválida (FALLIDO)
    # ----------------------------------------------------
    try:
        s_error = ReservaSalas(104, "Sala Económica", tarifa_base=-10.0, capacidad_personas=4)
    except DatosInvalidosException as e:
        msg = f"Op 6 [CONTROLADO]: Fallo esperado al crear servicio con costo negativo -> {e}"
        print(msg)
        registrar_log(msg, nivel="warning")

    # ----------------------------------------------------
    # OPERACIÓN 7: Procesamiento de Reserva Exitosa de Sala (VÁLIDO)
    # ----------------------------------------------------
    try:
        r1 = Reserva(501, clientes[1], servicios[101], duracion_unidades=4)
        # Uso de argumentos sobrecargados opcionales
        r1.procesar_reserva(tasa_impuesto=0.19, descuento=0.10)
        reservas.append(r1)
        print("Op 7 [OK]: Reserva procesada correctamente.")
    except Exception as e:
        print(f"Op 7 [ERROR]: {e}")

    # ----------------------------------------------------
    # OPERACIÓN 8: Intento de Reserva con Servicio NO Disponible (FALLIDO)
    # ----------------------------------------------------
    try:
        r2 = Reserva(502, clientes[1], servicios[103], duracion_unidades=2)
        r2.procesar_reserva()
        reservas.append(r2)
    except ReservaInvalidaException as e:
        msg = f"Op 8 [CONTROLADO]: Fallo esperado en reserva -> {e}"
        print(msg)

    # ----------------------------------------------------
    # OPERACIÓN 9: Intento de Reserva con Parámetros Inválidos (Horas Cero/Negativas) (FALLIDO)
    # ----------------------------------------------------
    try:
        r3 = Reserva(503, clientes[1], servicios[102], duracion_unidades=-3)
        r3.procesar_reserva()
        reservas.append(r3)
    except ReservaInvalidaException as e:
        msg = f"Op 9 [CONTROLADO]: Fallo esperado por duración inválida -> {e}"
        print(msg)

    # ----------------------------------------------------
    # OPERACIÓN 10: Procesamiento de Reserva de Asesoría y Cancelación (VÁLIDO)
    # ----------------------------------------------------
    try:
        # Reactivamos un servicio o usamos uno válido para procesar y luego cancelar
        s4 = AsesoriaEspecializada(104, "Asesoría Ciberseguridad", tarifa_base=80.0, especialista="Dra. López", disponible=True)
        r4 = Reserva(504, clientes[1], s4, duracion_unidades=3)
        r4.procesar_reserva(nivel_urgencia="alta")
        reservas.append(r4)
        # Cancelación
        r4.cancelar_reserva()
        print("Op 10 [OK]: Reserva creada, procesada y cancelada correctamente.")
    except Exception as e:
        print(f"Op 10 [ERROR]: {e}")

    print("\n" + "=" * 65)
    print("  SIMULACIÓN FINALIZADA CON ÉXITO Y SISTEMA ESTABLE")
    print("=" * 65)

if _name_ == "_main_":
    ejecutar_simulacion()
