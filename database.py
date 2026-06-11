import sqlite3

def conectar_bd(ruta='amazon_clon.db'):
    """Crea conexión y asegura que la tabla ventas exista."""
    conexion = sqlite3.connect(ruta)
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ventas (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            TIMESTAMP TIMESTAMP,
            PAYMENT_METHOD TEXT,

            CUSTOMER_ID INTEGER,
            DEVICE_TYPE TEXT,
            MARKETING_CHANNEL TEXT,

            PRODUCT_NAME TEXT,
            CATEGORY TEXT,
            SUB_CATEGORY TEXT,
            WARRANTY_MONTHS INTEGER,
            PRODUCT_RATING REAL,

            PRICE REAL,
            QUANTITY INTEGER,
            DISCOUNT_PERCENTAGE REAL,

            LOCATION_STATE TEXT,
            POSTAL_CODE TEXT,
            IS_GIFT TEXT,
            SHIPPING_METHOD TEXT,
            SHIPPING_CARRIER TEXT,
            DELIVERY_STATUS TEXT,

            RETURN_STATUS TEXT
        )
    ''')

    return conexion, cursor
