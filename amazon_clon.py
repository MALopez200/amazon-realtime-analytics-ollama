import sqlite3
import random
import time
from datetime import datetime

# =====================================================================
# 1. CONEXIÓN Y CREACIÓN DE LA BASE DE DATOS
# =====================================================================
conexion = sqlite3.connect('amazon_clon.db')
cursor = conexion.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS ventas (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    TIMESTAMP TIMESTAMP,
    PAYMENT_METHOD TEXT,

    COSTOMER_ID INTEGER,
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

# =====================================================================
# 2. PARÁMETROS FIJOS (CATÁLOGOS CARGADOS AFUERA DEL BUCLE PARA OPTIMIZAR)
# =====================================================================
categorias_general = {
    "Electronics": {
        "Computers & Accessories": ["Computadora", "Teclado", "Mouse", "Monitor", "Impresora", "Cargador", "Tableta"],
        "Audio & Video": ["Televisor", "Control remoto", "Auriculares", "Micrófono", "Altavoz", "Cámara"],
        "Phones & Gadgets": ["Teléfono", "Consola de juegos", "Reloj de pulsera", "Linterna", "Batería"]
    },
    "Home & Kitchen": {
        "Furniture": ["Mesa", "Silla", "Escritorio", "Sillón", "Cama", "Armario"],
        "Bedding & Decor": ["Almohada", "Sábana", "Cobija", "Colchón", "Lámpara", "Bombilla", "Espejo", "Cuadro", "Reloj", "Cortina", "Alfombra"],
        "Appliances": ["Ventilador", "Calefactor", "Aire acondicionado", "Refrigerador", "Microondas", "Horno", "Licuadora", "Cafetera", "Tostadora"]
    },
    "Tools & Office Supply": {
        "Kitchenware": ["Sartén", "Olla", "Plato", "Vaso", "Taza", "Tenedor", "Cuchillo", "Cuchara", "Servilleta"],
        "Stationery": ["Libro", "Cuaderno", "Bolígrafo", "Lápiz", "Goma de borrar", "Regla", "Tijeras", "Cinta adhesiva", "Pegamento", "Calculadora"],
        "Hardware": ["Llave", "Candado", "Billetera", "Mochila", "Bolso", "Maleta", "Gafas", "Gafas de sol", "Paraguas", "Martillo", "Destornillador", "Alicates", "Llave inglesa", "Clavo", "Tornillo", "Taladro", "Cinta métrica"],
        "Personal Care": ["Cepillo de dientes", "Pasta de dientes", "Jabón", "Champú", "Toalla"]
    }
}

marcas = {
    "Electronics": ["Apple", "Microsoft", "Google", "Samsung", "Sony", "Nintendo", "Intel", "AMD", "Nvidia", "Asus", "HP", "Dell", "Lenovo", "Logitech", "Razer", "Corsair", "Bose", "Sennheiser"],
    "Home & Kitchen": ["IKEA", "Philips", "Panasonic", "LG", "Samsung", "General Electric", "Siemens", "Oreo", "Nestle"],
    "Tools & Office Supply": ["Caterpillar", "Stanley", "DeWalt", "Bosch", "3M", "FedEx", "UPS", "DHL", "Bic", "Paper Mate"]
}

modificador_tecnologia = ["Pro", "Max", "Ultra", "4K", "Inalámbrico", "Bluetooth", "Smart", "Gamer", "Slim"]
modificador_hogar = ["Vintage", "Minimalista", "Moderno", "Clásico", "Elegante", "Premium", "Compacto"]
modificador_herramientas = ["De alta resistencia", "Multi-usos", "Portátil", "Manual", "Digital", "Industrial"]

estados = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", 
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY",
    "DC", "PR"
]

# MAPEO OPERATIVO: Un solo Código Postal real amarrado fijamente a cada Estado
codigos_postales_estados = {
    "AL": "35203", "AK": "99501", "AZ": "85001", "AR": "72201", "CA": "90001",
    "CO": "80201", "CT": "06101", "DE": "19801", "FL": "33101", "GA": "30301",
    "HI": "96801", "ID": "83701", "IL": "60601", "IN": "46201", "IA": "50301",
    "KS": "66101", "KY": "40201", "LA": "70112", "ME": "04101", "MD": "21201",
    "MA": "02101", "MI": "48201", "MN": "55401", "MS": "39201", "MO": "64101",
    "MT": "59601", "NE": "68101", "NV": "89101", "NH": "03101", "NJ": "07101",
    "NM": "87101", "NY": "10001", "NC": "28301", "ND": "58501", "OH": "43201",
    "OK": "73101", "OR": "97201", "PA": "19101", "RI": "02901", "SC": "29201",
    "SD": "57101", "TN": "37201", "TX": "73301", "UT": "84101", "VT": "05601",
    "VA": "23219", "WA": "98101", "WV": "25301", "WI": "53201", "WY": "82001",
    "DC": "20001", "PR": "00901"
}

tipos_de_envios = ['Standard', 'Express', 'Free']
metodos_de_pago = ['Tarjeta Credito', 'Tarjeta Debito', 'PayPal', 'Tarjeta Regalo']
dispositivos = ['Celular', 'Escritorio', 'Tablet']
canales_marketing = ['Anuncios de Google', 'Redes Sociales', 'Organico', 'Afiliado']
carriers_envio = ['Servientrega', 'Coordinadora', 'Envía', 'Interrapidisimo']
estados_entrega = ['Entregado', 'Enviado', 'En camino']


# =====================================================================
# 3. BUCLE DE SIMULACIÓN (SOLO DECISIONES DINÁMICAS EN TIEMPO REAL)
# =====================================================================
while True:
    # --- Selección del Producto ---
    categoria = random.choice(list(categorias_general.keys()))
    sub_category_elegida = random.choice(list(categorias_general[categoria].keys()))
    item_elegido = random.choice(categorias_general[categoria][sub_category_elegida])
    marca_elegida = random.choice(marcas[categoria])

    # --- Lógica de Precios, Modificadores y Garantías por Pasillo ---
    if categoria == "Electronics":
        modificador_elegido = random.choice(modificador_tecnologia)
        precio = round(random.uniform(200.00, 1500.00), 2)
        warranty_months = random.choice([12, 24, 36])
    elif categoria == "Home & Kitchen":
        modificador_elegido = random.choice(modificador_hogar)
        precio = round(random.uniform(40.00, 400.00), 2)
        warranty_months = random.choice([0, 6, 12])
    else:
        modificador_elegido = random.choice(modificador_herramientas)
        precio = round(random.uniform(5.00, 100.00), 2)
        warranty_months = 0

    product_name = f"{marca_elegida} {item_elegido} {modificador_elegido}"
    product_rating = round(random.uniform(3.5, 5.0), 1)

    # --- Transacción, Descuentos y Tiempo ---
    cantidad = random.randint(1, 10)
    
    azar_descuento = random.random()
    if azar_descuento < 0.70:
        descuento = 0.0
    else:
        descuento = round(random.uniform(0.05, 0.20), 2)

    forma_de_pago = random.choice(metodos_de_pago)
    fecha_venta = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # --- Cliente y Marketing ---
    id_cliente = random.randint(100000, 999999)
    device_type = random.choice(dispositivos)
    marketing_channel = random.choice(canales_marketing)

    # --- Geografía y Operaciones Amarradas ---
    estado_envio = random.choice(estados)
    postal_code = codigos_postales_estados[estado_envio]  
    
    is_gift = random.choice(['Si', 'No'])
    tipo_envio = random.choice(tipos_de_envios)
    shipping_carrier = random.choice(carriers_envio)
    delivery_status = random.choice(estados_entrega)

    # --- Probabilidad clásica de Devoluciones (5% de tasa fija) ---
    azar_devolucion = random.random()
    if azar_devolucion < 0.05:
        return_status = 'Devuelto'
    else:
        return_status = 'Ninguno'

    # =====================================================================
    # 4. INSERCIÓN MÁXIMA EN SQLITE
    # =====================================================================
    
    
    
    cursor.execute('''
        INSERT INTO ventas (
            TIMESTAMP, PAYMENT_METHOD, COSTOMER_ID, DEVICE_TYPE, MARKETING_CHANNEL,
            PRODUCT_NAME, CATEGORY, SUB_CATEGORY, WARRANTY_MONTHS, PRODUCT_RATING,
            PRICE, QUANTITY, DISCOUNT_PERCENTAGE, LOCATION_STATE, POSTAL_CODE,
            IS_GIFT, SHIPPING_METHOD, SHIPPING_CARRIER, DELIVERY_STATUS, RETURN_STATUS
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        fecha_venta, forma_de_pago, id_cliente, device_type, marketing_channel,
        product_name, categoria, sub_category_elegida, warranty_months, product_rating,
        precio, cantidad, descuento, estado_envio, postal_code,
        is_gift, tipo_envio, shipping_carrier, delivery_status, return_status
    ))
    
    # El commit se ejecuta siempre para asegurar cada dato en el archivo .db
    conexion.commit()
    
    # El aviso en la terminal sí se queda filtrado por el residuo matemático para no saturar
    print(f"[{fecha_venta}] ⚡ venta de {product_name} realizada con exito!")
        
    # Espera controlada de una centésima de segundo
    time.sleep(0.5)