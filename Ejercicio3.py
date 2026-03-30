# Ejercicio 3: Clase CuentaBancaria + Tupla y Ciclo
# Objetivo: Crear una tupla de cuentas y realizar depósitos y retiros.

import os
os.system("cls")

class CuentaBanco:
    def __init__ (self, titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo
    def depositar (self, cantidad):
        self.saldo += cantidad
    def retirar (self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
        else:
            print("El numero ingresado a retirar es superior al que hay en la cuenta")
            
cuenta1 = CuentaBanco("Tomás", 1000000)
cuenta2 = CuentaBanco("Ramiro", 200000)
cuenta3 = CuentaBanco("Juan", 100000)
    
cuentas = (cuenta1, cuenta2, cuenta3)
    
for cuenta in cuentas:
        cuenta.depositar(300)
        cuenta.retirar(100)
        print(f"El titular es: {cuenta.titular} | Saldo de la cuenta: {cuenta.saldo}")