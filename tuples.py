# Las tuplas son inmutables

x = (1, 2, 3) # Creo una tupla
print(x)
print(type(x))

birthday = tuple(("23", "Mayo", "1995")) # Construyo una tupla con el método tuple
print(birthday)

y = (2) # Es un número
y = (2,) # Es una tupla

print(x[1]) # Imprimo el valor del índice 1 en la tupla

del y # Elimina la tupla, deja de estar definido