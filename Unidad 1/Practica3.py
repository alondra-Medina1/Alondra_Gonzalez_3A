# Practica 3.  Introduccion al poliformismo
# Simular un sistema de cobro de al menos 4 tipos de operaciones de pago

class pago_tarjeta:
    def procesar_pago(self, cantidad):
        return f"Procesando pogo de ${cantidad} con tarjeta debidto/credito"
    
class pago_evectivo:
    def procesar_pago(self, cantidad):
        return f"Procesando pogo de ${cantidad} en efectivo"
    
class pago_paypal: # Cuando sea paypal, pedirle al usuario su nombre
    def procesar_pago(self, cantidad):
        nombre = input("Ingresa tu nombre")
        return f"Procesando pogo de ${cantidad} con paypal del usuario {nombre}"
    
class pago_trasferencia: # Actividad 2 Agregar funcionalidad dicional al metodo procesar_pago() cuando sea trasferencia: sumar 20 (comision) a cantidad
    def procesar_pago(self, cantidad):
        cantidad_total = cantidad + 20
        return f"Procesando pogo de ${cantidad} con trasferencia"

metodos_pago = [pago_tarjeta(), pago_paypal(), pago_evectivo(), pago_trasferencia()]

for m in metodos_pago:
    print(m.procesar_pago(500))

# Actividad 1
# Procesar diferentes cantidades de cada opcion de pago: 100 con tarjeta, 400 con efectivo, 600 con paypal y 500 con trasferencia 

pago1 = pago_tarjeta()
pago2 = pago_evectivo()
pago3 = pago_paypal()
pago4 = pago_trasferencia()

print(pago1.procesar_pago(100))
print(pago2.procesar_pago(600))
print(pago3.procesar_pago(400))
print(pago4.procesar_pago(500))

