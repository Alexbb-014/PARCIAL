#Ejercicio 3: Conversor de Temperatura (2.0)
'''Escribe un programa que permita al usuario convertir una temperatura en grados centígrados a Fahrenheit o viceversa. El programa debe
solicitar al usuario ingresar la temperatura y la unidad de medida (C para Celsius, F para Fahrenheit) y luego realizar la conversión
correspondiente, el programa debe manejar un menú de opciones y solo detenerse cuando se presione la opción finalizar.
Grados centígrados = (grados Fahrenheit menos 32) por 5/9.
Grados Fahrenheit = (grados centígrados por 9/5) +32.'''


while True:
    temperatura = float(input("Ingresa la temperatura deseada: "))
    unidad = input("Ingresa la unidad de medida(C. para Celsius, F. para Fahrenheit): ")

    if unidad == "C" or unidad == 'c' :
        fahrenheit = (temperatura * 9/5) + 32
        print(f"{temperatura} grados Celsius son equivalentes a {fahrenheit} grados Fahrenheit.")
    elif unidad == "F" or unidad == 'f':
        celsius = (temperatura - 32) * 5/9
        print(f"{temperatura} grados Fahrenheit son equivalentes a {celsius} grados Celsius.")
    else:
        print("Unidad de medida inválida. Inténtalo de nuevo.")

    opcion = input("Presiona 'C' para convertir otra temperatura, o 'F' para finalizar: ")
    if opcion == "F":
        break

