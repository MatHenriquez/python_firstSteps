# Módulos

# own modules: definimos por el usuario
from modules import myMath # Importo mi módulo myMath que está en la carpeta modules
myMath.add(1, 2) # Llamo a una de las funciones que definí en el módulo
myMath.substract(3, 2)

# third part modules: definido por otros. Son descargables
from colorama import Fore, Back, init # Importo Fore y BAck del módulo colorama que instalé con: pip install colorama
init(convert=True) # Para que funcione el Fore y el Back
print(Fore.RED + "Hello, world!") # Uso Fore para imprimir los mensajes a partir de este en rojo

# python modules: módulos pre-construidos en python
import datetime # Importo el módulo de fechas y horas
print(datetime.date.today()) # Imprime la fecha actual
print(datetime.timedelta(minutes = 110)) # Pasa de minutos a horas

