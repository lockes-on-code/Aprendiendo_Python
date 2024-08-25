### Listas ###

my_list = list() # Un array no es lo mismo, una lista nos proporciona operaciones propias de una lista.
my_other_list = [] # Aparentemente otra forma de hacer una lista, al imprimir el tipo de ambos es 'list'.
# Tanto las listas como los arrays nos permiten almacenar datos.

print(len(my_list))

my_list = [17, 31, 30, 18, 23, 28, 30] # El uso principal uso de las listas es el de almacenamiento de datos.
# Podemos, si te fijas, guardar valores idénticos en una misma lista.

print(my_list)
print(len(my_list))

my_other_list = [17, 1.79, "Iván", "Fernández"] # Vemos que podemos almacenar distintos tipos de datos en una misma lista.
# Dentro del corchete los elementos se colocan como 0, 1, 2, etc. respectivamente en cualquier lenguaje de programación.

print(type(my_list)) # Clase / tipo 'list'.
print(type(my_other_list)) # También clase / tipo 'list'.

print(my_other_list[0]) # Imprimimos el primer elemento de la lista.
print(type(my_other_list[0])) # Y podemos ver que su clase es 'int'

print(my_other_list[-1]) # Imprime el último elemento de la lista, es decir, "Fernández".
# Al parecer el "-1" que he decidido incluir daría un error en muchísimos otros lenguajes de programación.

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-2])

"""
print(my_other_list[-5]) / Daría un indexerror al pasarnos del rango permitido cuyo máximo, en negativos, es "-4".
print(my_other_list[4]) / Otro indexerror de rango al ser el maximo permitido "4" en los valores positivos.
El rango de valores permitidos en "my_other_list" es entre "-5 y 4" de acuerdo a esta lista.
"""

# print(my_other_list.count()) / Al verlo pensamos que nos va a contar elementos, pero esto no es así. Para que funcione hay que añadirle algo que contar.
print(my_other_list.count("Iván")) # Aunque ya lo vimos es para contar elementos dentro de la lista.
print(my_list.count(30)) # Otro ejemplo del mismo tipo.

age, height, name, surname = my_other_list # He asignado una variable a cada elemento de la lista, los escoge en orden. Tiene que haber el mismo número de variables como de elementos en la lista, si no da error.
print(name) # Forma de complicarse, formas más sencillas entre las lineas 21 y 30.

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)
# Se puede desordenar, esto es posiblemente un foco principal de errores.

print(my_list + my_other_list) # Concatenamos listas.