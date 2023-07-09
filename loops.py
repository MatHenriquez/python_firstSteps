# Bucles

foods = ['apples', 'bread', 'fried chicken', 'cheese', 'milk', 'salt', 'pepper', 'hot dog']

# Bucle for-in
for food in foods:
    if food == 'milk':
        continue # Pasa a la siguiente iteración sin terminar de ejecutar la actual
    if food == 'pepper':
        break   # Termina el bucle for inmediatamente
    print(food)

for number in range(1, 8):
    print(number)

for char in "Aloha":
    print(char)

# Bucle while
age = 1

while age < 18:
    print(f"Te faltan {18 - age} vueltas al sol para ser mayor de edad.")
    age = age + 1