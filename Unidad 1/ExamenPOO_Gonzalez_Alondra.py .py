class Libro:
    disponoble = True or False 
    def __init__(self,  título, autor, año, código, disponible):
        self.título = título
        self.autor = autor
        self.año = año
        self.código = código
        self.disponible = disponible
    
    def marcar_como_disponible(self):
          print(f"El libro {self.disponible}, esta disponoble ")

    def marcar_como_prestado(self):
          print(f"El libro {self.título}, no esta disponoble debido a que se presto a un estudiante o profesor")

class Usuario: 
    def __init__(self, nombre, id_usuario, correo):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.correo = correo

    def mostrar_info(self):
          print(f"El {self.id_usuario}, esta semana a tomado dos libros como prestamo ")

    def solicitar_prestamo(self):
        print(f"El {self.id_usuario} esta solicitando el siguiente libro {self.título} ")


class Estudiante(Usuario):
    def __init__(self, nombre, id_usuario, correo, carrera, semestre):
        super().__init__(nombre, id_usuario, correo)
        self.carrera = carrera
        self.semestre = semestre

    def mostrar_info(self):
        print(f"Estudiante: {self.nombre}, ID: {self.id_usuario}, Correo: {self.correo}, Carrera: {self.carrera}, Semestre: {self.semestre}")


class Profesor(Usuario):
    def __init__(self, nombre, id_usuario, correo, departamento, tipo_contrato):
        super().__init__(nombre, id_usuario, correo)
        self.departamento = departamento
        self.tipo_contrato = tipo_contrato

    def mostrar_info(self):
        print(f"Profesor: {self.nombre}, ID: {self.id_usuario}, Correo: {self.correo}, Departamento: {self.departamento}, Tipo de contrato: {self.tipo_contrato}")

class Prestamo: 
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def registro_devolver(self):
          print(f"El {self.id_usuario}, a devuelto el libro {self.fecha_devolucion}")

    def registro_prestamo(self):
          print(f"El {self.id_usuario} esta solicitando el siguiente libro {self.título}, la fecha de prestamo fue {self.fecha_prestamo} ")

if __name__ == "__main__":
  libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, "L001", True)
  libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943, "L002", True)


  usuario1 = Usuario("Ana Pérez", "U001", "ana@example.com")
  usuario2 = Usuario("Luis Gómez", "U002", "luis@example.com")


  estudiante1 = Estudiante("Carlos Ruiz", "E001", "carlos@example.com", "Ingeniería", 3)
  estudiante2 = Estudiante("María López", "E002", "maria@example.com", "Medicina", 5)

  profesor1 = Profesor("Dr. Juan Torres", "P001", "juan@example.com", "Matemáticas", "Tiempo completo")
  profesor2 = Profesor("Dra. Elena Díaz", "P002", "elena@example.com", "Biología", "Medio tiempo")

  print("\nInformación de libros:")
  libro1.mostrar_info()
  libro2.mostrar_info()

  print("\nInformación de usuarios:")
  usuario1.mostrar_info()
  usuario2.mostrar_info()

  print("\nInformación de estudiantes y profesores (polimorfismo):")
  for persona in [usuario1, estudiante1, profesor1]:
        persona.mostrar_info()


  print("\nSimulación de préstamo por estudiante:")
  prestamo1 = estudiante1.solicitar_prestamo(libro1, "2025-10-07", "2025-10-14")
  if prestamo1:
        print(f"Estado del libro tras préstamo: {libro1.disponible}")

  print("\nSimulación de préstamo por profesor:")
  prestamo2 = profesor1.solicitar_prestamo(libro2, "2025-10-07", "2025-10-14")
  if prestamo2:
        print(f"Estado del libro tras préstamo: {libro2.disponible}")


  print("\nDevolución de libros:")
  if prestamo1:
        prestamo1.devolver_libro()
        print(f"Estado del libro tras devolución: {libro1.disponible}")
  if prestamo2:
        prestamo2.devolver_libro()
        print(f"Estado del libro tras devolución: {libro2.disponible}")


  print("\nInformación de préstamos:")
  if prestamo1:
        print(f"Libro: {prestamo1.libro.titulo}, Usuario: {prestamo1.usuario.nombre}, Fecha préstamo: {prestamo1.fecha_prestamo}, Fecha devolución: {prestamo1.fecha_devolucion}")
if prestamo2:
        print(f"Libro: {prestamo2.libro.titulo}, Usuario: {prestamo2.usuario.nombre}, Fecha préstamo: {prestamo2.fecha_prestamo}, Fecha devolución: {prestamo2.fecha_devolucion}")

