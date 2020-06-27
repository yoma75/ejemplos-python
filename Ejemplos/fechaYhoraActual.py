# Obtener la fecha y hora actuales del sistema

# Modulo incorporado
import datetime

ahora = datetime.datetime.now()
print(ahora)

# Editar el formato de fecha y hora
print(ahora.strftime('%d/%m/%Y %H:%M:%S'))