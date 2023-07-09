# Es una lista desordenada

colors = { 'Red', 'Green', 'Blue'} # Defino un set
print(type(colors)) # Expected output: <class 'set>
print(colors)

print('Red' in colors) # Me fijo si Red está o no en el set

colors.add('Purple') # Añado un color al principio del set
print(colors)

colors.remove('Green') # Elimino un color del set
print(colors)

colors.clear() # Vacía el set
print(colors) # Expected output: set()

del colors # Elimina colors, ya no está definido