#Ejercicio 1. Contador de Vocales (1.0)
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0
total_vocales = 0

while True:
    entrada = input('Ingrese una vocal o ingrese "finalizar" para terminar el programa: ')
    if entrada == 'finalizar':
        break

    if entrada in 'aeiou':
        if entrada == 'a':
            contador_a += 1
        elif entrada == 'e':
            contador_e += 1
        elif entrada == 'i':
            contador_i += 1
        elif entrada == 'o':
            contador_o += 1
        elif entrada == 'u':
            contador_u += 1
        total_vocales += 1

print('\nCantidad total de vocales:', total_vocales)
print('\n\nCantidad de vocales:')
print(f'- a: {contador_a}')
print(f'- e: {contador_e}')
print(f'- i: {contador_i}')
print(f'- o: {contador_o}')
print(f'- u: {contador_u}')


