#!/usr/bin/env python3
import os
#Limpiar


def clear_screen():
    os.system('clear')  # Para sistemas basados en Unix/Linux
    # Si estás en un sistema Windows, puedes usar 'cls' en lugar de 'clear'

if __name__ == "__main__":
    clear_screen()
    print("¡Pantalla limpia!")

#borrar db
print('Borrando archivo db.sqlite3')
rm db.sqlite3

#crear migraciones
print('creando migraciones')
python3 manage.py makemigrations

#aplicando migraciones
print('aplicando migraciones')
python3 manage.py migrate


