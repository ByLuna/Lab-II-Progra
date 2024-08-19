class Veterinaria:
    def __init__(self, peso=0, nombre="", clase="", color="", edad=0, genero=""):
        self.Estado = "NO ATENDIDO"
        self.peso = peso
        self.tamano = self.determinar_tamano()
        self.Nombre = nombre
        self.Clase = clase  
        self.Color = color
        self.Edad = edad
        self.Genero = genero

    def determinar_tamano(self):
        if self.peso <= 10:
            return "Perro Pequeño"
        else:
            return "Perro Grande"

    def cambiar_estado(self):
        self.Estado = "ATENDIDO"
        return self.Estado

    def entrada_datos(self):
        self.Nombre = input("Nombre del Perro: ")
        self.Clase = input("Ingrese qué raza es su mascota: ")
        self.Color = input("Ingrese el color de su mascota: ")
        self.Edad = int(input("Ingrese la edad de su mascota: "))
        self.peso = int(input("Ingrese el peso de su mascota en kg: "))
        self.Genero = input("Ingrese el género de su mascota: ")
        self.tamano = self.determinar_tamano()  
    def muestra_datos(self):
        print(f"Nombre: {self.Nombre}")
        print(f"Raza: {self.Clase}")
        print(f"Color: {self.Color}")
        print(f"Edad: {self.Edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Tamaño: {self.tamano}")
        print(f"Género: {self.Genero}")
        print(f"Estado: {self.Estado}")

perro = Veterinaria()  # Se puede crear la instancia sin valores iniciales
perro.entrada_datos()  # Se piden los datos al usuario
perro.cambiar_estado()  # Cambia el estado a "ATENDIDO"
perro.muestra_datos()  # Muestra todos los datos del perro
