import sqlite3
import time
from consultor import consultar_local

conexion = sqlite3.connect('amazon_clon.db')
cursor = conexion.cursor()

while True:
    cursor.execute('''
        SELECT PRODUCT_NAME, SUM(QUANTITY), AVG(PRICE) FROM ventas  GROUP BY PRODUCT_NAME
        ORDER BY COUNT(*) DESC
        LIMIT 10
    ''')

    consulta = cursor.fetchall()

    prompt = f'eres un asistente que revisa los datos de {consulta} debes tener en cuenta que los datos vienen en formato: nombre producto, unidades vendidas, precio entonces primero analiza el valor de las ventas totales de cada producto y luego de ello analiza el top 3 de los productos que mas valor en ventas refleja y recomiendame que porcentaje deberia subir de precio de cada uno y con los que menos valor de ventas refleja me dices que descuento deberia aplicar para que se tenga una mayor rotacion y generar mejores ingresos'

    analisis = consultar_local(prompt)

    print(analisis)

    time.sleep(30000)