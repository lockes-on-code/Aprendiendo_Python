### Listas ###

my_list = list([]) # Un array no es lo mismo, una lista nos proporciona operaciones propias de una lista.
my_other_list = [] # Aparentemente otra forma de hacer una lista, al imprimir el tipo de ambos es 'list'.
# Tanto las listas como los arrays nos permiten almacenar datos.

print(len(my_list))

my_list = [17, 31, 30, 18, 23, 28, 31] # El uso principal uso de las listas es el de almacenamiento de datos.
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
# Numeración de los elementos de una lista es el siguiente: 0, 1, 2, n-1... Siendo "n" el numero de elementos que tengamos en una lista. Y escribo -1 ya que se empieza con el 0 a enumerar.

"""
print(my_other_list[-5]) / Daría un indexerror al pasarnos del rango permitido cuyo máximo, en negativos, es "-4".
print(my_other_list[4]) / Otro indexerror de rango al ser el maximo permitido "4" en los valores positivos.
El rango de valores permitidos en "my_other_list" es entre "-5 y 4" de acuerdo a esta lista.
"""

# print(my_other_list.count()) / Al verlo pensamos que nos va a contar elementos, pero esto no es así. Para que funcione hay que añadirle algo que contar.
print(my_other_list.count("Iván")) # Aunque ya lo vimos es para contar elementos dentro de la lista.
print(my_list.count(31)) # Otro ejemplo del mismo tipo.

age, height, name, surname = my_other_list # He asignado una variable a cada elemento de la lista, los escoge en orden. Tiene que haber el mismo número de variables como de elementos en la lista, si no da error.
print(name) # Forma de complicarse, formas más sencillas entre las lineas 21 y 30.

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)
# Se puede desordenar, esto es posiblemente un foco principal de errores.

print(my_list + my_other_list) # Concatenamos listas, al parecer solo funciona la suma de listas, o eso creo.


# Prueba de multiplicar, solo con elementos tipo 'int' en listas.
"""
new_list = [1, 2, 30]
other_new_list = [2, 5, 15]

print(new_list * other_new_list) 
No funciona al ser variables tipo 'list'

print(int(new_list) * int(other_new_list))
No funciona ya que int() no funciona con variables tipo 'list'
"""

# Más funciones con las listas. 
# Con la gran mayoría de estas funciones primero hay que ejecutarlas para luego poder imprimirlas, si no imprime "None" en la consola.

my_other_list.append("lockes.CO") # La función de listas del sistema cuyo principal uso es para añadir nuevos elementos al final de la lista. 
print(my_other_list)

my_other_list.insert(1, "Apuesto") # Sirve para insertar elementos en la posicion de la lista que desees, primero se coloca la posición en la que queremos insertar un elemento y luego aquello que queramos insertar.
print(my_other_list)

my_other_list[1] = "Más que apuesto" # Podemos remplazar valores de la lista de esta manera.
print(my_other_list)

print(my_other_list[2]) # Y como vemos los elementos se corren de posición, ya que el "1.79" estaba en la posición 1.

my_other_list.remove("Más que apuesto") # Función de listas del sistema para poder eliminar cualquier valor de la lista.
print(my_other_list)

my_list.remove(31) # Otro ejemplo con la función remove, si nos damos cuenta esta función eliminara el primer valor que encuentre que nosotros le hayamos indicado.
print(my_list)


my_list.pop(3) # Otra función para eliminar elementos, pero esta elimina según la posición que se le indique, si no escribimos nada se eliminara el último elemento por defecto.
print(my_list.pop()) # Escribe solo el elemento que se elimina de la lista.
print(my_list) # La lista sin el elemento 3 y el último.

my_pop_element = my_list.pop(3) # Podemos guardar la función anterior como una variable.
print(my_pop_element) # Como antes el "print(my_list.pop())"
print(my_list)

my_other_list.append(my_list.pop()) # Forma de traspaso de datos de una lista a otra.
my_other_list.insert(1, my_pop_element) # Otra forma de traspaso de datos.
print(my_other_list)
print(my_list) # Con los elementos eliminados tras el traspaso.

del my_other_list[6] # Sirve para eliminar elementos por su índice, con esta función no se pueden utilizar, es decir, solo queríamos cargarnos un dato de la lista.
print(my_other_list)

my_new_list = my_list.copy() # Copia la lista en su estado actual.

my_list.clear()
print(my_list)
print(my_new_list) # Copia la lista de los traspasos de datos, esto principalmente se debe a que el "clear" se hizo después del "copy".

my_new_list.reverse() # Función para imprimir los valores de una lista al reves.
print(my_new_list)

my_new_list.sort() # Ordena los valores de menor a mayor.
print(my_new_list)

# my_other_list.sort() / Entre variables 'str' e 'int' no se pueden ordenar de menor a mayor


# Ahora rebanadas de los elementos de una lista.
my_new_list.append(93) # Añadimos más variables a la lista.
my_new_list.append(64)
my_new_list.append(38) 
print(my_new_list)
print(my_new_list[1:3]) # Esto ya lo vimos con variables 'str'.
print(my_new_list[0:4:2])


my_list = "Hola Python" # Teníamos una lista con el mismo nombre y debido al tipado dinámico de Python esta ahora es una variable tipo 'str'.
# Este tipado dinamico puede causar una principal fuente de errores.
# Este es un lenguaje debilmente tipado.

print(my_list)
print(type(my_list))