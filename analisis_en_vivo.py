import sqlite3
import subprocess

conexion = sqlite3.connect('amazon_clon.db')
cursor  = conexion.cursor()

cursor.execute('SELECT SUM(precio) FROM VENTAS')
total_ventas = cursor.fetchone()[0]

cursor.execute('''
    SELECT ubicacion, 
            COUNT(*), 
            SUM(precio), 
            SUM(precio) / COUNT(*) 
    FROM ventas 
    GROUP BY ubicacion 
    ORDER BY COUNT(*) DESC 
    LIMIT 3
''')
top_estados = cursor.fetchall()

conexion.close()

datos_crudos = f"""
Reporte del sistema de ventas en tiempo real:
- Ingresos totales acumulados: ${total_ventas:.2f}
- Top 3 estados con más transacciones:
    1. {top_estados[0][0]} ({top_estados[0][1]} ventas por {top_estados[0][1]} USD con un promedio de {top_estados[0][3]})
    2. {top_estados[1][0]} ({top_estados[1][1]} ventas por {top_estados[1][1]} USD con un promedio de {top_estados[1][3]} por venta)
    3. {top_estados[2][0]} ({top_estados[2][1]} ventas por {top_estados[2][1]} USD con un promedio de {top_estados[2][3]} por venta)
"""

prompt = f'Eres un analista de negocio experto. Analiza estos datos reales: {datos_crudos}. Dame 3 observaciones estratégicas basadas ESTRICTAMENTE en los números provistos, sin calcular nuevos promedios'

print ('ANALIZANDO LOS DATOS...')

resultado = subprocess.run(
    ['ollama', 'run', 'llama3.2:latest',prompt], 
    capture_output=True, 
    text=True,
    encoding='utf-8'
)

print("\n================ REPORTE GENERADO POR IA LOCAL ================")
print(resultado.stdout)
print("===============================================================")