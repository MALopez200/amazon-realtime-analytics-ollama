import time
from dotenv import load_dotenv
import datetime
from consultor import consultar_local, auditar_respuesta
from alertas import enviar_alerta
from database import conectar_bd

# Cargar variables desde el archivo .env
load_dotenv()

# Conexión a la base de datos (se mantendrá abierta durante el bucle)
conexion, cursor = conectar_bd()

while True:
    #tiempo actual para el analisis de la ia
    ahora = datetime.datetime.now()
    # ------------------------------------------------------------
    # 1. TOP 5 PRODUCTOS MÁS VENDIDOS
    # ------------------------------------------------------------
    cursor.execute('''
        SELECT PRODUCT_NAME, COUNT(*)
        FROM ventas
        GROUP BY PRODUCT_NAME
        ORDER BY COUNT(*) DESC
        LIMIT 5
    ''')
    top_productos = cursor.fetchall()

    if not top_productos:
        print ('No hay datos por analizar')
    else:
        try:
            enviar_alerta("analisis periodico", str(top_productos))
        except Exception:
            print('no hay conexion para enviar los datos')
        print("\n🔥 TOP 5 PRODUCTOS:")
        for producto in top_productos:
            print(f"   • {producto[0]} ({producto[1]} ventas)")

        prompt_bodega = (
            f"Eres el administrador de la bodega. Estos son los 5 productos que se están "
            f"vendiendo más: {top_productos}. Dame una estrategia de 2 pasos para asegurarme "
            f"de que nunca nos quedemos sin stock. Responde en un párrafo de 30 palabras."
        )

        print("\n📦 ANALIZANDO INVENTARIO...")
        ahora = datetime.datetime.now()
        timestamp_legible = ahora.strftime("%Y-%m-%d %H:%M:%S")
        print(timestamp_legible)

        respuesta = consultar_local(prompt_bodega)
        print(respuesta)
        auditoria = auditar_respuesta(respuesta, top_productos,'top 5')
        print('Auditoria', auditoria)
        print("=" * 60)

    # ------------------------------------------------------------
    # 2. DEVOLUCIONES DE REGALOS POR ESTADO
    # ------------------------------------------------------------
    cursor.execute('''
        SELECT LOCATION_STATE, SUM(PRICE)
        FROM ventas
        WHERE RETURN_STATUS = 'Devuelto' AND IS_GIFT = 'Si'
        GROUP BY LOCATION_STATE
        ORDER BY SUM(PRICE) DESC
        LIMIT 5
    ''')
    calidad = cursor.fetchall()
    if not calidad:
        print ('No hay datos por analizar')
    else:
        try:
            enviar_alerta('Analisis devoluciones', str(calidad))
        except Exception:
            print('no hay conexion para enviar los datos')
        prompt_calidad = (
            f"Eres el jefe de control de calidad. Esta es la lista de devoluciones por "
            f"estado: {calidad}. Todos son obsequios. Indica exactamente qué zona de USA es "
            f"la más afectada y sugiere acciones de servicio al cliente para retener a esos compradores."
        )

        print("\n🔍 ANALIZANDO DEVOLUCIONES...")
        ahora = datetime.datetime.now()
        timestamp_legible = ahora.strftime("%Y-%m-%d %H:%M:%S")
        print(timestamp_legible)

        respuesta = consultar_local(prompt_calidad)
        print(respuesta)
        print("=" * 60)

    # ✅ Pausa antes de la siguiente iteración
    time.sleep(300)

# ❗ Si el bucle infinito se interrumpe, se cierra limpiamente
conexion.close()
