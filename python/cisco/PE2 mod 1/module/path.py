# Hay una variable especial (en realidad una lista) que almacena todas las ubicaciones (carpetas o directorios) 
# que se buscan para encontrar un módulo que ha sido solicitado por la instrucción import.

#La variable se llama path (ruta), y es accesible a través del módulo llamado sys. Así es como puedes verificar su valor:

import sys

#for p in sys.path:
#   print(p)

from sys import path
path.append('..\\packages')




