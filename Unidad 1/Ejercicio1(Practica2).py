# Ejercicio 1. Crear una clase, objeto, minimos 3 atributos y minimo 3 metodos distintos

class Mascota:
    def __init__(self, nombre, color, edad):
          self.nombre = nombre
          self.color = color
          self.edad = edad 
    
    def jugar(self):
          print(f"{self.nombre}, esta jugando con su pelota ")

    def dormir(self):
          print(f"{self.nombre}, esta tomando una ciesta ")
        
    def edad_perro(self):
          edad_convertida = self.edad * 7
          print(f"La edad de {self.nombre} en años perro es: {edad_convertida}")

perrito1 = Mascota("Canelita", "Gris", 3)

perrito1.dormir()
perrito1.jugar()
perrito1.edad_perro()