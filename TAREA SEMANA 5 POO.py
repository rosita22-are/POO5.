"""
Programa: Conversor de Temperatura
Descripción: Este programa convierte una temperatura ingresada en grados Celsius
a grados Fahrenheit y muestra el resultado al usuario.
"""

# Función que convierte grados Celsius a Fahrenheit
def convertir_celsius_a_fahrenheit(temperatura_celsius):
    return (temperatura_celsius * 9 / 5) + 32


# Variable booleana para controlar la ejecución del programa
continuar_programa = True

# Bucle principal del programa
while continuar_programa:
    # Solicitar datos al usuario
    nombre_usuario = input("Ingrese su nombre: ")
    temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

    # Conversión de temperatura
    temperatura_fahrenheit = convertir_celsius_a_fahrenheit(temperatura_celsius)

    # Mostrar resultados
    print("\nHola", nombre_usuario)
    print("La temperatura en Fahrenheit es:", round(temperatura_fahrenheit, 2), "°F")

    # Preguntar si desea continuar
    respuesta = input("\n¿Desea realizar otra conversión? (si/no): ").lower()

    if respuesta != "si":
        continuar_programa = False
        print("Programa finalizado. ¡Gracias por usar el conversor!")
