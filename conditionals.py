age = 28

if age >= 18:   # Condición a evaluar
    print("Es mayor de edad.") # Se ejecuta sólo si se cumple la condición
else:
    print("Es menor de edad.") # Se ejecuta sólo si NO se cumple la condición

color = "yellow"

if color == "blue":
    print("Yes, the color is blue")
elif color == "yellow":
    print("The color is yellow")
else:
    print(f"No, the color is not blue or yellow. Is {color}")

# Operadores lógicos
if age > 18 and age < 65: # Con and deben cumplirse ambas condiciones
    print("Te encuentras en edad laboral activa.")
else:
    print("Te encuentras en edad laboral pasiva.")

name = "Mati"

if not(name == "Mati"): # not devuelve el opuesto del resultado obtenido
    print("No eres mi tocayo.")
else:
    print("Eres mi tocayo")

name = "Camila"

if name == "Camilo" or name == "Camila": # Con or basta que se cumpla una de las condiciones
    print("Eres mi tocayo/a.")
else:
    print("No eres mi tocayo/a")