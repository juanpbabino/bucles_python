# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y cuante cuantes números son negativos y cuantos números son mayor o igual a cero
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el último número de la secuencia\n'))

contador = 0  # Inicializo el contador en 0

# for ... in range(....)

secuencia = range(inicio, fin+1)


for i in secuencia:
    if (i < 0):
        contador += 1
        print("La cantidad de números negativos son", contador)
    else:
        print("La cantidad de números mayores o igual a cero son",contador)
# Imprimir el valor de la cantidad de números positivos y negativos

print("terminamos!")
