x = 2
y = 5
z = "Pene"
#Prueba con variables y practica de la sintaxis 'print'
if y > x:
    print(float(x))
print("Happy birthday!... There's a bomb!, there's a bomb!, it's going to explode!")
print("")
print("A David le encanta el pito >:)")

print("whats 9 times 9??.... 21 ")
print("")

"""
Practica con funciones y variables globales/locales
Funciones sin parametros
Funciones con un prarmetro
Funciones con muletiples parametros y un resultado 
Variables locales
"""

global_1 = "Paco"

#función sin parámetros que solo devuelve 'Hola'
def diHola():
  print("¡Hola!")

diHola()  #llamada a la función 'Hola', la cual se muestra en la consola

#función con un parámetro
def holaConNombre(name): 
  print("¡" + "Hola " + name + "!")
  global_1 = "Juaco" #variable local con el mismo nombre que la global, debido a que esta dentro de la función 'holaConNombre' esta sera una función que solo se podra usar dentro de dicha función a no ser que le de la etiqueta 'global'
  print(global_1)

holaConNombre("Ada")  #llamada a la función 'Hola Ada!', la cual se muestra en la consola

print("Hola, " + global_1) #función global 

#función con múltiples parámetros y un resultado
def multiplica(val1, val2):
  print(val1 * val2)

multiplica(3, 5)