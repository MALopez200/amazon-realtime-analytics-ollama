import random
import time
import subprocess
import sqlite3
import string
import datetime

conexion = sqlite3.connect('amazon_clon.db')
cursor  = conexion.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS CLIENTES(
            COSTUMER_ID INTEGER PRIMARY KEY,
            NAME TEXT,
            EMAIL TEXT,
            PHONE TEXT)
''')

letras = list(string.ascii_letters)

nombre_usuario = ''
correo_usuario = ''
dominio_usuario = ''
telefono_usuario = ''

for i in range(10):
    letra = random.choice(letras)
    correo_usuario = correo_usuario + letra
    
for i in range(5):
    letra = random.choice(letras)
    dominio_usuario = dominio_usuario + letra

correo_final = f'{correo_usuario}@{dominio_usuario}.com'

for i in range(8):
    letra = random.choice(letras)
    nombre_usuario = nombre_usuario + letra

for i in range(10):
    numero = random.randint(0, 9)
    telefono_usuario = telefono_usuario + str(numero)

id_prueba = random.randint(100000, 999999)

cursor.execute('''
    INSERT INTO CLIENTES (COSTUMER_ID, NAME, EMAIL, PHONE)
    VALUES (?, ?, ?, ?)
''', (id_prueba, nombre_usuario, correo_final, telefono_usuario))

conexion.commit()

conexion.close()


