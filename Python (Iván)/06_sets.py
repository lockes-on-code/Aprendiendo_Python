### Sets ###
# De base tiene un array al igual que las listas, pero, en Python, no existen los arrays.

my_set = set() # La forma de llamar a un set.
my_other_set = {} # Al parecer la forma simple de llamar a un set.

print(type(my_set))
print(type(my_other_set)) # Al imprimir el tipo vemos que pone 'dict' de diccionario, pero, al parecer, los sets se llaman de la misma forma que los diccionarios.

# Ahora vamos a entender a los sets como una lista con una peculiaridad que veremos después.
my_other_set = {"Iván", "Fernández", 17}
print(type(my_other_set)) # Y ahora al imprimir el tipo vemos que pone 'set', es decir, que las llaves al estar vacias van a ser un diccionario.

# A parte de listas, tuplas y sets tenemos una estructura más que es la de diccionario, los diccionarios los veremos más adelante así que no hace falta saber que son ahora.

print(len(my_other_set)) # Cuenta el número de elementos.

"""
print(my_other_set[0]) / Error al intentar imprimir elementos como en las listas.
Antes de acceder a elementos podemos hacer diferentes operaciones.
Ahora vamos a interpretar esto como un listado.
"""

my_other_set.add("lockes") # Función para añadir elementos nuevos.
print(my_other_set) # Nos lo coloca todo desordenado, por lo que esto ya no es como un listado y una tupla. Y, además, ya no tenemos control absoluto de los elementos como en las listas y, por lo tanto, no podemos acceder a ellos mediante índices, algo que pasa también con las tuplas.

my_other_set.add("lockes") # Un set no admite repetidos, algo diferente tanto en las tuplas como en las listas.
print(my_other_set) # Un nuevo orden.

# La sintaxis para comprobar si un elemento se encuentra presente dentro de un set.
print("Fernández" in my_other_set) # Fernández existe en my_other_set, True.
print("Hernández" in my_other_set) # Hernández existe en my_other_set, False.

my_other_set.remove("Fernández") # Función para eliminar valores de un set, función presente dentro de las listas.
print(my_other_set)

my_other_set.pop() # En los sets la función pop elimina el primer elemento que salga en el set.
print(my_other_set)

my_other_set.clear() # Función que elimina todos los elementos de un set.
print(my_other_set) 
print(len(my_other_set)) # Como podemos ver la longitud del set es 0, es decir, contiene 0 elemenrtos.
print(type(my_other_set)) # Pero al imprimir el tipo vemos que aun sigue poninendo que es un set.

del my_other_set # Eliminamos el set.
# print(my_other_set) / El set ya no existe.

my_set = {"Iván", "Fernández", 17}
my_list = list(my_set)
print(my_list)
print(my_list[0]) # Podemos acceder a los elementos, pero esto es muy arriesgado debido a que no conocemos el orden de la lista.

my_other_set = {"HTML", "Pyhton", "JavaScript"}

my_new_set = my_set.union(my_other_set) # Función para sumar sets.
print(my_new_set) 
print(my_new_set.union(my_new_set).union(my_set)) # Y si hacemos una nueva unión consigo mismo, con my_set o con my_other_set podemos ver que no pasa nada debido a que los valores no se pueden repetir.
print(my_new_set.union({"C#", 1.79})) # Pero podemos añadir valores nuevos de la siguiente manera.

print(my_new_set.difference(my_set)) # Función que nos indica que valores no se encuentran dentro de, en este caso, my_set, y no se incluyen C# y 1.79 debido a que estas no pertenecen directamente a my_new_set, sino que son de una unión.

"""
VENTAJAS DE LOS SETS
No trabajar con repetidos.
Y trabajar rapidamente con elementos que no necesitan un orden en concreto.
"""
