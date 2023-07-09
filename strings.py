# Métodos de strings
myStr = "Hola, mundo"

print(dir(myStr)) # Me ofrece info sobre métodos del tipo de dato que le paso como argumento

print(myStr.upper()) # upper convierte todo a mayúscula
print(myStr.lower()) # lower convierte todo a minúscula
print(myStr.swapcase()) # swapcase invierte mayúsculas y minúsculas

print(myStr.replace('mundo', 'mundo cruel')) # replace reemplaza el primer parámetro por el segundo
print(myStr.replace('Hola', 'Chau').upper()) # Métodos encadenados

print(myStr.count('o')) # count cuenta cuantas veces aparece 'l'
print(myStr.split()) # split separa las palabras del string en una lista de strings. Por defecto lo hace buscando los espacios en blanco
print(myStr.find('H')) # find me debuelve la posición del caracter que le paso como argumento 0 -1 si no lo encuentra
print(len(myStr)) # len muestra la longitud del string

print(myStr.isnumeric()) # isnumeric dice si es de tipo number o no
print(myStr.isalpha()) # isalpha dice si es alfanumérico o no

print(myStr[3]) # Imprime el caracter del index 4
print(myStr[-1]) # Imprime el caracter del último index 

print("Saludo " + myStr) # Imprime los strings concatenados
print(f"Mi saludo es: {myStr}") # Imprime templated string
print("Mi saludo 2 es: {0}".format(myStr))