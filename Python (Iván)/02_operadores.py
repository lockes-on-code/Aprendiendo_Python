### Operadores ariméticos ###

# Operadores ariméticos básicos con números

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3) # Operador de módulo, es decir, el resto obtenido al realizar una división, en cuyo caso es 1.
print(81 // 7) # A esto se le llama una flor división, es decir, este es el cociente de una división, siempre sera un número entero.
print(2 ** 3) # Basicamente una potencia.

print(2 ** 3 + 3 - 7 / 1 // 4) # Todos los signos se pueden combinar entre ellos


# Operadores ariméticos básicos con palabras y mezclas de datos.

print("Hola " + "Python, " + "¿Qué tal?") # Lo ha concatenado todo, pero lo junta a diferencia de poner "," la cual deja espacios, es por eso que hay que colocarle a las palabras los espacios.
# print("Hola" - "Python") Esto dara error debido a que son "str", es decir, con este tipo de datos no se pueden realizare las mismar operaciones que con los datos numéricos.

"""
print("Hola " + 5) Dara error debido a que no se puede trabajar con tipos diferentes. 
Para juntar distintos tipos de datos tenemos que utilizar funciones del sistema, es decir, convertirlo en una función "str".
"""
print("Hola " + str(5)) # Se permite porque el dato es ahora "str"
print("Hola " * 5) # La multiplicación si permite el comobinacion de estos dos tipos de datos.
print("Hola " * int(2 ** 3 + 3 - 7 / 1 // 4)) # El resultado de la operacion da un dato tipo "float" y este no se permite multiplicar con los datos "str", por eso cambie el tipo del dato a "int".

my_float = 2.5 * 2
print("Hola " * int(my_float))
print("")



### Operadores comparativos ###

"""
Operadores comparativos con números.
Todos los valores son "bool".
"""
print(" COMPARATIVOS CON NÚMEROS ")
print("")
print(3 > 4)
print(3 >= 4)
print(3 < 4)
print(4 <= 4)
print(3 == 4) # ¿Es igual a?
print(3 != 4) # ¿No es igual a?
print(3 > 4 == 2) # Se pueden juntar distintos operadores de este tipo
print("")

"""
Operadores comparativos con datos "str".
Se comparan las primeras letras de ambas palabras
"""
print(" COMPARATIVOS CON 'str' ")
print("")
print("Paco" > "Python") # Comparación de ordenación alfabetica
print("Picadura" >= "Python") # Comparación de ordenación alfabetica
print("Peso" < "Python") # Comparación de ordenación alfabetica

print("aaaa" >= "AAAA") # Las letras minusculas tienen un valor mayor a las mayúsculas
print("AAAA" >= "aaaa") # Ordenación alfabetica por ASCII
print("aaaaaa" <= "aaaaa") # Cuantos más caracteres más grande

print("Pytho" == "Python") # Si es la misma palabra
print("Pytho" != "Python") # Si es una palabra distinta
print("")



### Operadores lógicos ###
# Lógica y las tablas de la verdad (Conjunción "and" y disyunción "or").

print(3 > 4 and "Paco" > "Python") # "False" y "False" = "False"
print(3 > 4 or "Paco" > "Python") # "False" o "False" = "False"

print(3 < 4 and "Paco" > "Python") # "True" y "False" = "False" , lo mismo en el otro sentido.
print(3 < 4 or "Paco" > "Python") # "True" o "False" = "True" , lo mismo en el otro sentido.

print(3 < 4 and "Paco" < "Python") # "True" y "True" = "True"
print(3 < 4 or "Paco" < "Python") # "True" o "True" = "True"
print(3 < 4 or ("Paco" > "Python" and 4 == 4)) # Tablas de la verdad.

# print(3 > 4 not "Paco" > "Python") Error
print(not(3 > 4)) # La negación en las tablas de la verdad.