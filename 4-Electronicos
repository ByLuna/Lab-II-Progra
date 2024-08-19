class DispositivoElectronico:
    def __init__(self):
        self.tipo = input("Ingrese el tipo de dispositivo (Celular/Tablet/Portátil): ")
        self.modelo = input("Ingrese el modelo del dispositivo: ")
        self.capacidad = input("Ingrese la capacidad del dispositivo (e.g., 128GB, 8GB RAM): ")
        self.color = input("Ingrese el color del dispositivo: ")
        self.pantalla = input("Ingrese el tamaño de la pantalla (e.g., 6.5 pulgadas): ")
        self.bateria = input("Ingrese la capacidad de la batería (e.g., 4000mAh): ")
        self.precio_compra = float(input("Ingrese el precio de compra del dispositivo: "))
        self.marca = "PHR"  
        self.origen = "Importado"  
        self.precio_venta = self.calcular_precio_venta()

    def calcular_precio_venta(self):
        return self.precio_compra * 1.7

    def mostrar_datos(self):
        print("\nCaracterísticas del dispositivo:")
        print(f"Tipo: {self.tipo}")
        print(f"Modelo: {self.modelo}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Color: {self.color}")
        print(f"Tamaño de Pantalla: {self.pantalla}")
        print(f"Capacidad de Batería: {self.bateria}")
        print(f"Marca: {self.marca}")
        print(f"Origen: {self.origen}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")

print("Registro del primer dispositivo:")
dispositivo1 = DispositivoElectronico()
dispositivo1.mostrar_datos()

print("\nRegistro del segundo dispositivo:")
dispositivo2 = DispositivoElectronico()
dispositivo2.mostrar_datos()
