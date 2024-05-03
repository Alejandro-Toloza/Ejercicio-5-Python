from abc import ABC, abstractmethod
    
from datetime import date

class CuentaBancaria(ABC):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0):
        self._nombre_titular = nombre_titular       # atributo privado
        self._dni_titular = dni_titular             # atributo privado
        self._fecha_nacimiento = fecha_nacimiento   # atributo privado
        self._saldo = saldo                         # atributo privado

    def obtener_saldo(self):
        return self._saldo

    @abstractmethod
    def depositar(self, monto):
        pass

    @abstractmethod
    def extraer(self, monto):
        pass

    def _calcular_edad(self):
        fecha_actual = date.today()
        edad = fecha_actual - self._fecha_nacimiento
        return edad.days // 365

    def obtener_edad(self):
        return self._calcular_edad()

class CuentaAhorro(CuentaBancaria):
    TASA_INTERES = 0.001

    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
            print(f"Se ha depositado {monto} a la cuenta de {self._nombre_titular}, su saldo es de: {self.obtener_saldo()}")
        else:
            print("El monto a depositar debe ser mayor a 0")

    def extraer(self, monto):
        if monto <= self.obtener_saldo():
            self._saldo -= monto
            print(f"Se ha extraido {monto} de la cuenta de {self._nombre_titular}, su saldo actual es de: {self.obtener_saldo()}")
        else:
            print("No posee saldo suficiente para esta operación")

    def calcular_interes(self):
        return self._saldo * CuentaAhorro.TASA_INTERES


# Ejemplo de uso
cuenta_ahorro = CuentaAhorro("Gabriel", 33333333, date(1990, 3, 2), 2000)
print(cuenta_ahorro.obtener_edad())
cuenta_ahorro.depositar(500)
cuenta_ahorro.extraer(1000)
print(f"El interés generado es: {cuenta_ahorro.calcular_interes()}")


