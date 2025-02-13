class Material:
    def __init__(self, titulo, tipo, estado="disponible"):
        self.titulo = titulo
        self.tipo = tipo
        self.estado = estado
    
    def cambiar_estado(self, estado):
        self.estado = estado
        print(f"El estado del material '{self.titulo}' ha sido cambiado a {self.estado}")

class Libro(Material):
    def __init__(self, titulo, autor, genero, estado="disponible"):
        super().__init__(titulo, "Libro", estado)
        self.autor = autor
        self.genero = genero

class Revista(Material):
    def __init__(self, titulo, edicion, periodicidad, estado="disponible"):
        super().__init__(titulo, "Revista", estado)
        self.edicion = edicion
        self.periodicidad = periodicidad

class MaterialDigital(Material):
    def __init__(self, titulo, tipo_archivo, enlace_descarga, estado="disponible"):
        super().__init__(titulo, "Material Digital", estado)
        self.tipo_archivo = tipo_archivo
        self.enlace_descarga = enlace_descarga

class Persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class Usuario(Persona):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)
        self.materiales_prestados = []

    def consultar_catalogo(self, catalogo):
        catalogo.mostrar_materiales()

    def prestar_material(self, material, biblioteca, fecha_devolucion):
        if material.estado == "disponible":
            prestamo = Prestamo(self, material, fecha_devolucion)
            self.materiales_prestados.append(prestamo)
            biblioteca.registrar_prestamo(prestamo)
            material.cambiar_estado("prestado")
            print(f"{self.nombre} ha solicitado el material '{material.titulo}'")
        else:
            print(f"El material '{material.titulo}' no está disponible.")

class Bibliotecario(Persona):
    def __init__(self, nombre, email):
        super().__init__(nombre, email)

    def agregar_material(self, material, sucursal):
        sucursal.agregar_material(material)
        print(f"El bibliotecario {self.nombre} ha agregado '{material.titulo}' a la sucursal.")
    
    def transferir_material(self, material, origen, destino):
        if material in origen.catalogo:
            origen.eliminar_material(material)
            destino.agregar_material(material)
            print(f"'{material.titulo}' ha sido transferido de {origen.nombre} a {destino.nombre}.")

class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []
        self.prestamos = []

    def agregar_material(self, material):
        self.catalogo.append(material)

    def eliminar_material(self, material):
        self.catalogo.remove(material)

    def mostrar_materiales(self):
        print(f"Catálogo de la sucursal {self.nombre}:")
        for material in self.catalogo:
            print(f"- {material.titulo} ({material.estado})")

    def registrar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)
        print(f"Se ha registrado el préstamo de '{prestamo.material.titulo}' a {prestamo.usuario.nombre}")

class Prestamo:
    def __init__(self, usuario, material, fecha_devolucion):
        self.usuario = usuario
        self.material = material
        self.fecha_prestamo = None  
        self.fecha_devolucion = fecha_devolucion  
        self.penalizacion = None

    def devolver_material(self):
        if self.es_retraso():
            self.penalizacion = Penalizacion(self)
            self.penalizacion.aplicar_penalizacion()
        self.material.cambiar_estado("disponible")
        print(f"El material '{self.material.titulo}' ha sido devuelto.")

    def es_retraso(self):
        fecha_actual = "2025-02-15"  
        return self.fecha_devolucion < fecha_actual

class Penalizacion:
    def __init__(self, prestamo):
        self.prestamo = prestamo
        self.multa = 0

    def aplicar_penalizacion(self):
        dias_retraso = self.calcular_dias_retraso(self.prestamo.fecha_devolucion, "2025-02-15")
        if dias_retraso > 0:
            self.multa = dias_retraso * 1  
            print(f"Se ha aplicado una multa de {self.multa} por el retraso en la devolución de '{self.prestamo.material.titulo}'.")

    def calcular_dias_retraso(self, fecha_devolucion, fecha_actual):
        fecha_devolucion = [int(x) for x in fecha_devolucion.split("-")]
        fecha_actual = [int(x) for x in fecha_actual.split("-")]

        dias_devolucion = fecha_devolucion[0] * 365 + fecha_devolucion[1] * 30 + fecha_devolucion[2]
        dias_actual = fecha_actual[0] * 365 + fecha_actual[1] * 30 + fecha_actual[2]
        return max(0, dias_actual - dias_devolucion)

class Catalogo:
    def __init__(self):
        self.materiales = []

    def agregar_material(self, material):
        self.materiales.append(material)

    def buscar_por_titulo(self, titulo):
        for material in self.materiales:
            if titulo.lower() in material.titulo.lower():
                print(f"Encontrado: {material.titulo} ({material.tipo})")

    def buscar_por_tipo(self, tipo):
        for material in self.materiales:
            if material.tipo.lower() == tipo.lower():
                print(f"Encontrado: {material.titulo} ({material.tipo})")

    def mostrar_materiales(self):
        print("Catálogo de materiales:")
        for material in self.materiales:
            print(f"- {material.titulo} ({material.tipo})")


sucursal_1 = Sucursal("sucursal centro")
sucursal_2 = Sucursal("Sucursal norte")


libro_1 = Libro("El alquimista", "Paulo Coelho", "Ficción")
libro_2 = Libro("Matar a un ruiseñor", "Harper Lee", "Drama")
libro_3 = Libro("La sombra del viento", "Carlos Ruiz Zafón", "Misterio")
libro_4 = Libro("Cumbres borrascosas", "Emily Brontë", "Romántico")
libro_5 = Libro("Orgullo y prejuicio", "Jane Austen", "Romántico")
libro_6 = Libro("La guerra de los mundos", "H.G. Wells", "Ciencia ficción")

revista_1 = Revista("National Geographic", "Edición de febrero", "Mensual")
revista_2 = Revista("Time", "Edición de marzo", "Semanal")
revista_3 = Revista("Vogue", "Edición de enero", "Mensual")
revista_4 = Revista("Scientific American", "Edición de abril", "Mensual")
revista_5 = Revista("Rolling Stone", "Edición de diciembre", "Quincenal")
revista_6 = Revista("Forbes", "Edición de septiembre", "Mensual")
revista_7 = Revista("The Economist", "Edición de agosto", "Semanal")

material_digital_1 = MaterialDigital("Curso de Python", "PDF", "enlace.com")
material_digital_2 = MaterialDigital("Introducción a la Inteligencia Artificial", "PDF", "ia-curso.com")
material_digital_3 = MaterialDigital("Tutorial de JavaScript", "Video", "tutorialjs.com")
material_digital_4 = MaterialDigital("Guía de Diseño Gráfico", "eBook", "disenografico.com")
material_digital_5 = MaterialDigital("Curso de Machine Learning", "PDF", "ml-curso.com")
material_digital_6 = MaterialDigital("Curso de Desarrollo Web", "Video", "desarrolloweb.com")
material_digital_7 = MaterialDigital("Introducción a la Programación en C", "PDF", "programacionenC.com")


bibliotecario_1 = Bibliotecario("Laura", "laura@biblioteca.com")

bibliotecario_1.agregar_material(libro_5, sucursal_1)
bibliotecario_1.agregar_material(revista_3, sucursal_2)
bibliotecario_1.agregar_material(material_digital_1, sucursal_1)

catalogo = Catalogo()
catalogo.agregar_material(libro_5)
catalogo.agregar_material(revista_3)
catalogo.agregar_material(material_digital_1)

usuario_1 = Usuario("Dylan", "dylan@correo.com")

usuario_1.consultar_catalogo(catalogo)

usuario_1.prestar_material(libro_3, sucursal_1, "2025-02-20")

bibliotecario_1.transferir_material(libro_3, sucursal_1, sucursal_2)

prestamo = Prestamo(usuario_1, libro_3, "2025-02-10")
prestamo.devolver_material()