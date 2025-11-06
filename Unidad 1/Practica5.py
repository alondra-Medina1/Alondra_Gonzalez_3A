# Practica 5. Singleton
# Ejemplo de patrón de diseño Singleton - Sistema de Registro de logs.

class Logger:
    # Atributo de clase para guardar la única instancia
    _instance = None
# Método __new__ controla la creacion del objeto antes de init. Se asegura de que solo exista una unica instancia de logger.
    # Método __new__ controla la creación del objeto
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:   # Se crea solo una vez
            cls._instance = super().__new__(cls)
            # Arbimos un archivo de logs en modo "append (agregar)".
            cls._instance.archivo = open("app.log", "a")
        return cls._instance # Devuelve siempre a la misma instancia.

    def log(self, mensaje):
        self.archivo.write(mensaje + "\n")
        self.archivo.flush()   # Fuerza a guardar en disco

# Probando el Singleton
registro1 = Logger() # Se crea la unica instancia SINGLETON.
registro2 = Logger() # Devuelve la misma instancia, sin crear una nueva.

registro1.log("Inicio de sesión en la aplicación")
registro2.log("El usuario se autenticó")

print(registro1 is registro2)  # True, ambas variables apuntan a la misma instancia

