# Variables

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 3
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
# El tipo sin el apartado de "print" es "tuple", es decir, una secuancia de objetos
print(type((my_string_variable, my_int_to_str_variable, my_bool_variable)))
# Pero si le añadimos el "print" no tiene ningun tipo o dato en especifico, es decir, "NonType", debido a que es una función del sistema
print(type(print(my_string_variable, my_int_to_str_variable, my_bool_variable))) # También se nos vuelve a imprimir la cadena de texto si es que añadimos el "print" final


print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable)) #"len" de la palabra "lenght" (Cuenta la longitud)

# Diversas variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!, suele causar errores y confusiones.
name, surname, alias, age = "Iván", "Fernández", "lockes", 17
print("Buenas,", "soy", name, surname + ",", "alias", alias + ",", "y tengo", age, "años.")
print(type(age))

#Practicas con input
"""
name = input("¿Cómo te llamas? ")
print("Encantado de conocerte", name) # Antes teníamos una variable con el nombre "name", pero, como su nombre indica, el valor de una variable puede variar, es decir, esta sobreescribiendo su valor al que nosotros le indiquemos.

age = input("¿Y cuantos años tienes? ") # Antes teníamos una variable con el nombre "age", pero, como su nombre indica, el valor de una variable puede variar, es decir, esta sobreescribiendo su valor al que nosotros le indiquemos.
print("¿Conque", age, "eh?")
"""

# Cambiamos su tipo, esto en cualquier proyecto con varias personas puede suceder, y que por ejemplo se sume lo que no queremos que se sume, multiplique o reste.
name = 17
age = "Iván"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = 32 # Coge el último
print(type(address))


# Mirar lo basico del video que no se haya visto (Mañana)