# STRINGS #

my_string = "My String"
my_other_string = 'My Other String' # Se pueden escribir con "" o ''.

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)
print(len(my_string + " " + my_other_string))

my_new_line_string = "Este es un String\ncon salto de linea" # Con salto de linea "\n"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación" # Con tabulación "\t"
print(my_tab_string)

my_scape_string = "\tEste es un String\nescapado"
print(my_scape_string)


# Formateo con letras y números

"""
Muy común al internacionalizar textos, por ejemplo, tenemos una aplicación en español e inglés.
Más rapido y eficiente en comparación al tener que concatenar textos.
"""

name, surname, age = "Iván", "Fernández", 17.3

print("Mi nombre es {} {} y mi edad es {:.0f}".format(name, surname, age)) # Forma nueva, introducida en Python 3
print("Mi nombre es %s %s y mi edad es %.0f" %(name, surname, age)) # Forma antigua, nos aseguramos de que imprimimos todo como queremos, es decir, como un "str", "int", etc.

print("never gonna give you up, never gonna let you down, gay el q lo lea, balls")
"""
%s = "str"
%d = "int"
%f = "float"
{:.nf} = Poner el número de decimales que queramos en la forma nueva, siendo "n" dicho número.
%.nf = Poner el número de decimales que queramos en la forma antigua, siendo "n" dicho número.
"""

print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) # Esto es más cutre, te lleva más tiempo y es algo más compicado. (No es aconsejable)


# Inferencia o interpolación de datos con letras y números, la mejor para imprimir datos tal cual pero, si estamos formateando, la de los % es la mejor.
# Suelen estructurarse de la siguiente manera: f"contenido"
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

a = 4
b = 3
print(f"{a} + {b} = {a + b}")


# Desempaquetado de caracteres en variables
language = "Python"
a, b, c, d, e, f= language
# Numeración de los caracteres de la palabra "Python": P = 0, y = 1, t = 2, h = 3, o = 4, n = 5.

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


# División

language_slice = language[1:3] # Coge las letras de "Python" de la 1 a la 3 pero sin incluir esta última.
print(language_slice)

language_slice = language[1:] # Coge las letras de "Python" de la 1 hasta el final.
print(language_slice)

language_slice = language[-2] # Coge la letra -2, siendo esta la "o".
print(language_slice)

language_slice = language[0:6:3] # Empezando por el 0 va a coger el caracter 3 puestos adelante de este.
print(language_slice)


# Reverse

reversed_language = language[::-1] # Al revés, llendo desde el final. 
print(reversed_language)

reversed_language = language[::-2] # Al revés, llendo desde el final y así cada 2 caracteres.
print(reversed_language)

reversed_language = language[::-3] # Al revés, llendo desde el final y así cada 3 caracteres.
print(reversed_language)


# Métodos o funciones del sistema.

print(language.__len__()) # Una que ya habiamos visto.
# O también como ya hicimos: print(len(language)).

print(language.capitalize()) # Pone en mayúscula la primera letra.
print(language.upper()) # Todo en mayúsculas.
print(language.count("t")) # Cuenta las letras o números.
print(language.isnumeric()) # Si es un número (Entre "" si es un número).
print("1".isnumeric()) # Si es un número (Entre "" si es un número).
print(language.lower()) # Todas minúsculas.
print(language.upper().isupper()) # Todo en mayúsculas, pero el resultado sera "True" o "False" debido a que isupper comprueba si todo esta en mayúsculas o no.
print(language.startswith("Py")) # Si empieza con lo indicado dentro del parentesis.
print("Py" == "py")