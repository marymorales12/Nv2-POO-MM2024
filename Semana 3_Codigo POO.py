class Clima:
    def _init_(self):
        self.temperaturas = {}  # Diccionario para almacenar las temperaturas diarias

    def ingresar_temperatura(self, dia, temperatura):
        self.temperaturas[dia] = temperatura  # Ingresa la temperatura para un día específico

    def calcular_promedio_semanal(self):
        if not self.temperaturas:  # Verifica si no hay temperaturas ingresadas
            return 0.0
        total_temperatura = sum(self.temperaturas.values())  # Suma todas las temperaturas
        return total_temperatura / len(self.temperaturas)  # Calcula el promedio

def main():
    print("Programa para calcular el promedio semanal de temperaturas usando POO\n")

    clima = Clima()  # Crea una instancia de la clase Clima

    # Ingreso de temperaturas diarias
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    for dia in dias_semana:
        while True:
            try:
                temperatura = float(input(f"Ingrese la temperatura para el día {dia}: "))  # Solicita la temperatura al usuario
                break  # Si se ingresa un valor válido, sale del bucle
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")  # Manejo de errores para valores no numéricos
        clima.ingresar_temperatura(dia, temperatura)  # Ingresa la temperatura en la instancia de Clima

    # Cálculo del promedio semanal
    promedio = clima.calcular_promedio_semanal()  # Calcula el promedio usando el método de la clase Clima

    print("\nEl promedio semanal de temperaturas es: {:.2f}".format(promedio))  # Muestra el promedio

if __name__ == "_main_":
    main()  # Ejecuta la función main si el script se ejecuta directamente