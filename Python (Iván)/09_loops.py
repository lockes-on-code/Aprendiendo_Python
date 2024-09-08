### Bucles / Loops / Ciclos ###
"""
DEFINICIÓN
Uno de los grandes mecanismos que tenemos en programación que nos sirve para iterar, es decir, intentar repetir algo. Nos sirve para pasar por un mismo código varias veces.
"""

# While, podríamos decir que es un if que se repite.

my_condition = 0 # Hay que pasarle una condición

while my_condition < 10: # Al parecer, cuando se comienza a programar, hay un error muy común denominado el while-true, es decir, mientras sea verdadero haz algo.
    print(my_condition) # En este caso, si no añadimos ningun valor a my_condition (El error while-true), se va a imprimir cero hasta el infinito, esto principalmente se debe a que my condition no para de pasar por el while a no ser que su valor sea falso para la condición establecida.
    my_condition += 2 # Añadimos "x" constantemente a my_condition para evitar el error previo.
else: # Opcional.
    print("Mi condicion es mayor o igual que 10") # Como en los condicionales, podemos utilizar "else".


"""
elif my_condition == 10: / No se acepta debido a que es un "if" externo, funciona si va con un "if" antepuesto, ya que "if" se acepta. 
    print("Mi condición es igual a 10")
"""


while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Ejecución detenida")
        break # Para detener la ejecución de "while" en un momento concreto.

    print(my_condition)

print("La ejecución continúa")


# For, al igual que el bucle "while", tiene que cúmplir una condición, además nos sirve para iterar un listado de elementos.

my_list = [17, 31, 30, 18, 23, 28, 31]
for element in my_list: # Se va a repetir tantas veces como elementos iterables en la lista. Primero llamamos a los elementos, en este caso "elements", y luego a la lista.
    print(element)


my_tuple = (17, 1.79, "Iván", "Fernández", "Iván") # Imprime los valores.
for a in my_tuple: 
    print(a)


my_set = {"Iván", "Fernández", 17} # Imprime los valores desordenados.
for 要素 in my_set: 
    print(要素)


my_dict = {"Nombre":"Iván", "Apellido":"Fernández", "Edad":17, 1:"Python"} # Aquí solo se imprimen las claves por defecto.
for στοιχείο in my_dict.values(): # Si ponemos la función values imprimira los valores.
    print(στοιχείο)
    if στοιχείο == 17: 
        break # Terminamos el bucle cuando el valor en el diccionario sea 17.
else:
    print("El bucle for para el diccionario ha terminado")

print("La ejecución continúa")

for στοιχείο in my_dict.values(): # Si ponemos la función values imprimira los valores.
    print(στοιχείο)
    if στοιχείο == 17: 
        continue # Que siga pero volviendo al "for", es decir, cuando llega a 17 no se imprimira "Se ejecuta".
    print("Se ejecuta")
    
else:
    print("El bucle for para el diccionario ha terminado")

print("La ejecución continúa")