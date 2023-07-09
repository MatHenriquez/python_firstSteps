# Funciones

def saludo(name = "you... What was your name?"): # Defino una función y un parámetro por defecto
    print(f"Hello, {name}!")

saludo("Matt") # Llamo a la función
saludo() # Usa el valor  por defecto del parámetro

def suma(number_one = 0, number_two = 0):
    return number_one + number_two # Retorno un valor

resultado = suma(1, 4) # Guardo el valor retornado en una variable
print(resultado)

# Funciones lambda

add = lambda number_one, number_two: number_one + number_two # Función anónima que retorna lo que está en la misma línea

print(add(1, 3))