### Diccionarios ###

my_dict = dict() # Sintaxis de un diccionario.
my_other_dict = {} # La otra forma de llamar a un diccioanrio, identica a la forma de llamar a un set de forma simplificada pero, al imprimir su tipo, vemos que es un 'dict'.

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Iván", "Apellido":"Fernández", "Edad":17, 1:"Python"} # Como podemos ver, a diferencia de los sets, los valores dentro de un diccionario van en pares de relación clave-valor, primero definimos una clave para luego darle un valor.

"""
Tenemos una nueva estructura para poder relacionar datos.
Al último dato le hemos puesto un id.
Aunque no es necesario saberlo, esta estructura es similar a los JSON en JavaScript.
"""

# Podemos formatear diccionarios para que sea más facil visualmente.
my_dict = {
    "Nombre":"Iván", 
    "Apellido":"Fernández", 
    "Edad":17, 
    "Lenguajes": {"Python", "HTML", "JavasScript"}, # Podemos ver que, en este caso, la clave es un 'str' y el valor es un 'set'.
    1: 1.79
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict)) # La función del sistema "len" cuenta el número de claves asociadas a un valor o conjunto de valores.
print(len(my_dict))

print(my_dict["Nombre"]) # Si ponemos unos corchetes podemos ver que imprime el valor de la clave "Nombre".
# Esta es la mayor peculiaridad de los diccionarios, la facilidad con la que podemos acceder a un elemento.

my_dict["Nombre"] = "David" # Podemos cambiar el valor de una clave igualándola a un nuevo valor.
print(my_dict["Nombre"])
print(my_dict)

# Ahora vamos a acceder a la clave de tipo 'int', la cual se pone sin las comillas debido a que es un entero.
print(my_dict[1]) 


# Podemos añadir nuevas claves con sus respectivos valores de la siguiente forma, se colocan al final.
my_dict["Comunidad autonoma"] = "Principado de Asturias"
print(my_dict)


# Funciones con los diccionarios.
del my_dict["Comunidad autonoma"] # Podemos eliminar elementos de la siguiente forma con la función "del" y especifiquamos que es lo que queremos eliminar entre corchetes. 
print(my_dict)

my_dict.pop("Edad") # Otra manera de eliminar un elemento concreto del diccionario es mediante el uso de la función pop.
print(my_dict)

my_dict.popitem() # Podemos eliminar el último elemento de un diccionario de la siguiente forma, a diferencia de la función "pop" no podemos escoger la clave y valor que deseemos eliminar. 
print(my_dict)

print("Fernández" in my_dict) # Al verlo probablemente pensarás que es un error, pero da que es "false" debido a que estamos buscando por clave.
print("Apellido" in my_dict)


print(my_dict.items()) # Hace un listado con todos las claves y sus respectivos valores.
print(my_dict.keys()) # Listado con todas las llaves del diccionario.
print(my_dict.values()) # Listado con todos los valores del diccionario.



my_new_dict = dict.fromkeys(("Nombre", "Apellido", "Piso")) # Función para crear un nuevo diccionario sin valores, la variable / estructura anterior al punto da igual.
print(my_new_dict)

my_list = ["Nombre", "Apellido", "Piso"] # Podemos crear un nuevo diccionario a partir de listas.
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, 0) # Si ponemos entre los parentesis un diccionario hecho anteriormente vemos que las claves de este nuevo diccionario son las mismas que las del anterior.
print(my_new_dict)

# Con esta función podemos añadir los datos más adelante y aprovechart claves y, si ponemos algun valor despues de una coma, vemos que todas las claves toman dicho valor.

# Forma de hacerlo con una serie de claves.
my_new_dict = dict.fromkeys(("Nombre", "Apellido", "Edad"), 0) # Ponemos las claves entre parentesis y luego el valor que queramo añadir.
print(my_new_dict)

# Y podemos dar un conjunto de valores.
my_new_dict = dict.fromkeys(("Nombre", "Apellido", "Edad"), ("Iván", "Fernández", 17))
print(my_new_dict)

print(list(my_new_dict)) # Si yo lo transformo en una lista / tupla / set solo dan las claves.
print(tuple(my_new_dict))
print(set(my_new_dict))


my_values = my_new_dict.values()
print(type(my_values))
print(list(my_dict.values())) # Puedo hacer una lista de valores con la función "values".


my_new_dict = dict.fromkeys(("Nombre", "Apellido", "Edad"), "lockes")
print(dict.fromkeys(list(my_new_dict.values()))) # Incluso podemos dar vueltas y hacer un nuevo diccionario a partir de una lista de valores de otro diccionario.
print(list(dict.fromkeys(list(my_new_dict.values())).keys())) # Una lista a partir de lo anterior, el keys es para tomar las claves del diccionario.