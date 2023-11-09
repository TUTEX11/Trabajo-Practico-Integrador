import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

# Datos de ejemplo
libros = [
    ("001", "El señor de los anillos", 25.99, "disponible"),
    ("002", "Cien años de soledad", 20.50, "disponible"),
    ("003", "1984", 18.75, "disponible"),
    ("004", "Don Quijote de la Mancha", 22.30, "disponible"),
    ("005", "Moby Dick", 19.99, "disponible"),
    ("006", "Orgullo y prejuicio", 16.45, "disponible"),
    ("007", "Crimen y castigo", 21.20, "disponible"),
    ("008", "Las aventuras de Tom Sawyer", 15.75, "disponible"),
    ("009", "La Odisea", 23.40, "disponible"),
    ("010", "La metamorfosis", 17.90, "disponible")
]

# Insertar los libros en la tabla
cursor.executemany('''
    INSERT INTO Libros (Código, Título, Precio_Reposición, Estado) 
    VALUES (?, ?, ?, ?)
''', libros)

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Se han insertado los libros en la tabla Libros.")
