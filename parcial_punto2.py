#Ejercicio 2: Tabla de Multiplicar (2.0)

'''Crea un programa que solicite al usuario ingresar un número entero positivo (N). El programa debe mostrar la tabla de
multiplicar del número, teniendo en cuenta que se debe generar la tabla con los primeros 10 valores de dicha tabla.'''


Numero = int(input("Por favor, ingrese un número entero positivo  "))

if Numero > 0:
    for i in range(1, 11):
        print(f"{Numero} x {i} = {Numero * i}")
else:
    
    print("Debes ingresar un número entero positivo.")