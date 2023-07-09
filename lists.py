lista_de_prueba = [1, 'hola', 1.34, True, []] # lista con diferentes tipos de datos
print(lista_de_prueba)

number_list = list((1, 2, 3, 4)) # list() crea una nueva lista con los valores pasados como tupla
print(number_list)

range_list = list(range(1, 15)) # Crea una lista con los valores dentro del rango especificado (no incluye el 15)
print(range_list)

print(len(number_list)) # Imprime la longitud de valores en la lista

print(lista_de_prueba[1]) # Imprime el valor de índice 1 de la lista
print(lista_de_prueba[-2]) # Imprime el anteúltimo valor de la lista

print(1.34 in lista_de_prueba) # Nos dice si 1.34 está o no en la lista

colors = ['blue', 'yellow', 'brown']
print(colors)

colors[2] = "grey" # Las listas no son inmutables
print(colors)

colors.append('pink') # Agrega un nuevo valor al final de la lista
print(colors)

colors.extend(('green', 'red')) # Agrega los valores pasados como tupla al final de la lista como elementos individuales
print(colors)

colors.insert(-1, 'black') # Agrega el valor pasado como argumento en el índice dado, sin quitar el que ya estaba
print(colors)

colors.insert(len(colors), 'purple') # Agrega el valor pasado como argumento al final de la lista
print(colors)

colors.pop() # Remueve el último elemento de la lista
print(colors)

colors.remove('grey') # Elimina de la lista el valor pasado
print(colors)

colors.sort() # Ordena alfabéticamente
print(colors)

colors.sort(reverse=True) # Ordena alfabéticamente en orden descendente
print(colors)

print(colors.index('pink')) # Imprime el índice del valor pasado

print(colors.count('red')) # Imprime la cantidad de veces que se repite el valor pasado

colors.clear() # Deja la lista vacía
print(colors)

