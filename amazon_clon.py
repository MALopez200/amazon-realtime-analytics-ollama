import sqlite3
import random
import time

conexion = sqlite3.connect('amazon_clon.db')

cursor = conexion.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    producto TEXT,
    precio REAL,
    garantia INTEGER,
    ubicacion TEXT,
    calificacion INTEGER,
    transporte INTEGER,
    fecha_hora TIMESTAMP
)
''')
productos = [
    'Celular Pro', 'Celular Max', 'Celular Ultra', 'Celular Gamer', 'Celular Smart', 
    'Celular Eco', 'Celular Slim', 'Celular Premium', 'Celular Plus', 'Celular X', 
    'Laptop Pro', 'Laptop Max', 'Laptop Ultra', 'Laptop Gamer', 'Laptop Smart', 
    'Laptop Eco', 'Laptop Slim', 'Laptop Premium', 'Laptop Plus', 'Laptop X', 
    'Monitor Pro', 'Monitor Max', 'Monitor Ultra', 'Monitor Gamer', 'Monitor Smart', 
    'Monitor Eco', 'Monitor Slim', 'Monitor Premium', 'Monitor Plus', 'Monitor X', 
    'Teclado Pro', 'Teclado Max', 'Teclado Ultra', 'Teclado Gamer', 'Teclado Smart', 
    'Teclado Eco', 'Teclado Slim', 'Teclado Premium', 'Teclado Plus', 'Teclado X', 
    'Mouse Pro', 'Mouse Max', 'Mouse Ultra', 'Mouse Gamer', 'Mouse Smart', 
    'Mouse Eco', 'Mouse Slim', 'Mouse Premium', 'Mouse Plus', 'Mouse X', 
    'Auriculares Pro', 'Auriculares Max', 'Auriculares Ultra', 'Auriculares Gamer', 'Auriculares Smart', 
    'Auriculares Eco', 'Auriculares Slim', 'Auriculares Premium', 'Auriculares Plus', 'Auriculares X', 
    'Reloj Pro', 'Reloj Max', 'Reloj Ultra', 'Reloj Gamer', 'Reloj Smart', 
    'Reloj Eco', 'Reloj Slim', 'Reloj Premium', 'Reloj Plus', 'Reloj X', 
    'Cámara Pro', 'Cámara Max', 'Cámara Ultra', 'Cámara Gamer', 'Cámara Smart', 
    'Cámara Eco', 'Cámara Slim', 'Cámara Premium', 'Cámara Plus', 'Cámara X', 
    'Impresora Pro', 'Impresora Max', 'Impresora Ultra', 'Impresora Gamer', 'Impresora Smart', 
    'Impresora Eco', 'Impresora Slim', 'Impresora Premium', 'Impresora Plus', 'Impresora X', 
    'Altavoz Pro', 'Altavoz Max', 'Altavoz Ultra', 'Altavoz Gamer', 'Altavoz Smart', 
    'Altavoz Eco', 'Altavoz Slim', 'Altavoz Premium', 'Altavoz Plus', 'Altavoz X'
]

estados = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", 
    "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", 
    "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", 
    "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", 
    "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", 
    "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", 
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", 
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", 
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", 
    "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming",
    "Washington D.C.", "Puerto Rico"
]

while True:

    producto = random.choice(productos)
    precio = random.uniform(1.00, 1000.00)
    garantia = random.choice([0, 1])
    ubicacion = random.choice(estados)
    calificacion = random.randint(1,5)
    transporte = random.choice([0, 1])
    tiempo = time.strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute('''
        INSERT INTO ventas(producto,
        precio,
        garantia,
        ubicacion,
        calificacion,
        transporte,
        fecha_hora)
        VALUES(?,?,?,?,?,?,?)
        ''',(producto,precio,garantia,ubicacion,calificacion,transporte,tiempo))
    
    conexion.commit()
    print(f'se ha agradado la venta de {producto} a la base de datos')

    time.sleep(1)
