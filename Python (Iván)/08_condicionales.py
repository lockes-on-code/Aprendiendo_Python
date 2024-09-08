### Condicionales ###
# Nos representan la manera de establecer flujos de ejecución de nuestro código, es decir, decidir si algo de nuestro código se va a ejecutar o no.

my_condition = False # Al parecer la forma más facil de entender un condicional es con una variable tipo 'bool'.

if my_condition : # Al ejecutar una condicion del if tiene que ser verdadera. Es lo mismo que if my_condicion == True.
    print("Se ejecuta la condicion del if") # Lo que se desee a ejecutar por consola va identado en la siguiente linea de código después de ":".


my_condition = 15 # Si no le aplicamos una condición, como en este caso, el if va a imprimir de todas formas, es decir, lo toma por bueno este valor y seguirá. Esto es debido a que tenemos algo con valor y eso le vale.

if my_condition == 16: # Si queremos arreglar lo anterior hay que aplicar una condición, para ello hay que igualar el if a un valor. Al hacerse la igualación el valor previamente creado toma un valor de tipo 'bool', es decir, True o False.
    print("Se ejecuta la condicion del segundo if")

if my_condition > 15:
    print("El valor es mayor que 15")
else: # "esle" sirve para decir que, solo si my_condition no se cumple, se imprima lo de la siguiente línea de código tabulada.
    print("El valor es menor o igual que 15")


# Otro ejemplo con "else" seria como si fuesen contraseñas los valores.

my_password = "MeGustaPython"
if my_password == "MeGustaPython":
    print("Contraseña correcta")
else: # Es decir, si la contraseña no es igual a "MeGustaPython" imprime la siguiente línea de código tabulada.
    print("Contraseña incorrecta")


# Podemos jugar con los operadores lógicos que vimos en el apartado de operadores.

if my_condition > 15 and my_condition < 20: # Ahora se tienen que cúmplir ambas condiciones. En este caso, solo se cúmple la segunda parte de la condición.
    print("Es mayor que 15 y menor que 20")
else:
    print("Es menor o igual que 15 o mayor o igual que 20")
    
    
    
    print("Valor incorrecto") # Podemos escribir lo que queramos que se imprima de la condición mientras que este tabulada la línea de código, también podemos poner los espacios que queremos entre líneas, no hace falta que vayan a continuación.


if my_condition > 15 and my_condition < 20: 
    print("Es mayor que 15 y menor que 20")

print("Línea de código sin tabular") # Si no tabluamos la línea de código se imprimira siempre.


my_condition = 5 * 4

if my_condition > 15 and my_condition < 20: 
    print("Es mayor que 15 y menor que 20")
elif my_condition == 20: # La combinación de "else" e "if". Si no se cumple una condición previa aplicamos una nueva condicion con "elif", es decir, es como una comprobación extra.
    print("Es igual a 20")
else:
    print("Es menor o igual que 15 o mayor o igual que 20") # Si no se cúmple ninguna de los dos apartados anteriores se recurre a "else".


print("La ejecución continúa")



my_string = ""

if my_string: # Una cadena de texto vacía se representa como False debido a que no hay ningun valor.
    print("Mi cadena de texto no está vacía")


my_string = "Cadena con valor"

if my_string:
    print("Mi cadena de texto no está vacía")


my_string = "Cadena con valoor"

if my_string == "Cadena con valor": # Lo mismo que con las contraseñas
    print("Las cadenas de texto coinciden")


my_string = ""

if not my_string: # Implementamos un operador lógico, este if busca si se cumple que está vacio la variable my_string.
    print("Las cadenas de texto está vacía")


my_string = "Cadena con valoor"

if not my_string == "Cadena con valor": # Implementamos un operador lógico.
    print("Las cadenas de texto no coinciden")