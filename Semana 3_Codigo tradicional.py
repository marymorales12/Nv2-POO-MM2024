# Función para ingresar la temperatura para un día específico
def ingresar_temperatura(dia):
    while True:
        try:
            temperatura = float(input(f"Ingrese la temperatura para {dia}: "))
            return temperatura
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

# Función para calcular el promedio semanal de temperaturas
def calcular_promedio_semanal(temperaturas):
    if not temperaturas:
        return 0.0
    total_temperatura = sum(temperaturas)
    return total_temperatura / len(temperaturas)

# Función principal del programa
def main():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas_semana = []

    # Solicitar temperaturas para cada día de la semana
    for dia in dias:
        temperatura = ingresar_temperatura(dia)
        temperaturas_semana.append(temperatura)

    # Calcular el promedio semanal
    promedio_semanal = calcular_promedio_semanal(temperaturas_semana)

    # Mostrar el resultado
    print(f"El promedio semanal de la temperatura es: {promedio_semanal:.2f}°C")

# Ejecutar el programa principal
if __name__ == "_main_":
    main()