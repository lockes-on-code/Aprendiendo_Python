### Funciones ###
"""
DEFINICIÓN
Presentes en muchos otros lenguajes de programación, con las funciones intentamos resolver dos problemas. 
Primero, va a intentar resolver un problema muy concreto que tenemos que indicar. 
Y, por otra parte, gracias a las funciones, vamos a evitar errores, debido a que todo el código que va a resolver un problema muy concreto va a estar en un único lugar, entonces nosotros siempre que queramos resolver ese problema llamaremos a esa misma función, con lo cual, todo estara centralizado y no tendremos que duplicar código como al principio.
Las llamamos con la palabra reservada "def".
"""

def my_function(): # Para definir una función.
    print("Esto es una función") # Para que pertenezca a la función hay que tabular.


my_function() # Y escribimos esto para llamar a la función.
my_function()
my_function()


# Uso de parámetros

def sum_two_values(first_value, second_value): # Vamos a hacer la suma de dos valores. Primero, definimos los parámetros dentro del paréntesis.
    print(first_value + second_value) # Ahora imprimimos la suma de los dos valores.

sum_two_values(2, 15) # Y ahora al llamar a la función indicamos ambos valores dentro del paréntesis. Si ponemos más o menos valores de los requeridos no funciona.
sum_two_values(293478, 1494875) # Si yo tuviera que hacer una gran cantidad de sumas es mucho mas simple y rápido con funciones que con los operadores.
sum_two_values(1.7, 8.5) # Suma con valores tipo 'float'.
sum_two_values("4", "8") # Concatenando strings. Al intentar definir que los valores son unicamente de tipo 'int' Python, con su tipado debil y dinámico, seguira sumando dos strings.

"""
Para definir el valor deseado se ponen dos puntos y el tipo de dato después de los parámetros. Esto, en general, solo sirve para que los demas pasen el tipo de dato que se desea utilizar.
sum_two_values (int("4"), int("8")) / Así se haría para cambiar el tipo de los valores.
"""

# Ejemplo para especificar tipo de dato.

def div_two_numbers(first_number: int, second_number: int): # Especificamos datos tipo 'int'.
    print(first_number / second_number)

div_two_numbers(5, 2) # También funcionan datos tipo 'float'.
# div_two_numbers ("5", "2") / Error al ser datos tipo 'str' en una división.


# Retorno de parámetros

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum # Usamos la palabra reservada "return".

sum_two_values_with_return(8, 12) # Parace no devolver nada, vamoa a asignarle una variable.
my_result = sum_two_values_with_return(8, 12) # Con "return" podemos almacenar el resultado de funciones, y dicho resultado puede ser cualquier tipo de dato.
my_other_result = sum_two_values (1.7, 8.5) # No nos devuelven nada las funciones sin "return".
print(my_result)
print(sum_two_values_with_return(8, 12)) # Otra forma de imprimirlo sin variable, es decir, utilizar el resultado directamente.
print(my_other_result)


# Formateo en funciones

def print_name(name, surname):
    print(f"{name} {surname}") # La "f " es del formateo de strings ya visto.

print_name(surname = "Fernández", name = "Iván") # Pusímos los valores al revés y podemos asignar a cada uno que valor es cual.


# Valores por defecto 

def print_name_with_default(name, surname, alias = "Sin alias"): # Podemos añadir un valor por defecto si es que este campo no es rellenado.
    print(f"{name} {surname}, alias: {alias}")

print_name_with_default("Iván", "Fernández")
print_name_with_default("Iván", "Fernández", "lockes")


# Funciones con parámetros arbitrarios.

def print_texts(*text): # Con el asterisco estamos estableciendo que podemos poner el número de datos que nos de la gana.
    print(text) 

print_texts("Hola", "Python", "lockes")
print_texts("Hola")


def print_upper_texts(*texts):
    for text in texts: # Podemos usar loops.
        print(text.upper()) # Y usar funciones de los strings.

print_upper_texts("Hola", "Python", "lockes")
print_upper_texts("Hola")