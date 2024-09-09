### Tuplas ###

# Una tupla es un conjunto de valores / elementos.
my_tuple = tuple(()) # Forma de escribir una tupla.
my_other_tuple = () # Otra forma de definirla.

my_tuple = (17, 1.79, "Iván", "Fernández", "Iván") # Parece una lista.

print(my_tuple)
print(type(my_tuple)) # Clase 'tuple'

print(my_tuple[0]) # Por ahora parece lo mismo.
print(my_tuple[-1])
"""
print(my_tuple[4]) IndexError
print(my_tuple[-6]) IndexError
Y como ya vimos como con las listas también se nos presentan unos limites dentro de las tuplas.
"""

print(my_tuple.count("Iván")) # Función para contar el número de elementos dentro de la tupla.
print(my_tuple.index(1.79)) # Función que nos indica el indice de un elemento, esta función también esta presente para listas aunque no la hayamos visto.
# A diferencia de las listas estas son las únicas funciones presentes en las tuplas.

"""
PRINCIPAL DIFERENCIA CON LAS LISTAS

my_tuple[1] = 1.80
print(my_tuple)
Esto da error ya que los elementos en una tupla son constantes y no se pueden extraer.

my_tuple[5] = 1.80
print(my_tuple)
Tampoco se permite añadir valores nuevos a las tuplas.
"""

my_other_tuple = (35, 60, 40, 53, 36, 53)
print(my_tuple + my_other_tuple) # Concatenamos tuplas.

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple) # Otra forma de concatenarlas es creando una variable.

print(my_sum_tuple[3:6]) # Podemos hacer rebanadas / slices de elementos.
print(my_sum_tuple[1:4:2])

my_tuple = list(my_tuple) # Al cambiar a tipo 'list' no son necesarios los corchetes.
print(type(my_tuple))

my_tuple[3] = "lockes.CO"
my_tuple.insert(1, "Más que apuesto")
print(my_tuple) # Ahora tenemos nuevos valores a lo que era una tupla. Podemos hacer esto último si es que queremos añadir nuevos valores o modificar aquellos fijos.

my_tuple = tuple(my_tuple) # Volvemos a valores fijos.
print(my_tuple)
print(type(my_tuple))

# del my_tuple[2] / No se permite, ya que los elementos de una tupla no se pueden eliminar.

del my_tuple # Ahora my_tuple no está definida debido a que la hemos eliminado, esto la verdad es que es poco incoherente cuando lo vemos, ya que una tupla no puede modificarse.
# print(my_tuple) / NameError: name 'my_tuple' is not defined, es decir, la tupla no está definida.
# 'del' es utilizado para eliminar variables, no su contenido, aunque esto se exceptua dentro de las listas al especificar el elemento que deseamos eliminar de ellas.