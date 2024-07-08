# Clase base: Vehículo
class Vehiculo:
    def init(self, marca, modelo):
        self.marca = marca      # Atributo público
        self.modelo = modelo    # Atributo público
        self.__estado = 'apagado'  # Atributo privado (encapsulado)

    def encender(self):
        self.__estado = 'encendido'
        print(f'{self.marca} {self.modelo} ha sido encendido.')

    def apagar(self):
        self.__estado = 'apagado'
        print(f'{self.marca} {self.modelo} ha sido apagado.')

    def str(self):
        return f'Vehículo {self.marca} {self.modelo}, estado: {self.__estado}'

# Clase derivada: Coche (hereda de Vehículo)
class Coche(Vehiculo):
    def init(self, marca, modelo, color):
        super().init(marca, modelo)
        self.color = color    # Atributo específico de Coche

    def encender(self):  # Método polimórfico (sobrescribe el método de la clase base)
        self.__estado = 'encendido'
        print(f'{self.marca} {self.modelo} de color {self.color} ha sido encendido.')

# Creación de instancias y demostración del programa
if __name__ == "main":
    # Crear instancia de Vehículo
    vehiculo1 = Vehiculo('Toyota', 'Corolla')
    print(vehiculo1)
    vehiculo1.encender()

    # Crear instancia de Coche (clase derivada)
    coche1 = Coche('Ford', 'Mustang', 'rojo')
    print(coche1)
    coche1.encender()
