import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('biblioteca.db')

# Crear un cursor
cursor = conn.cursor()

# Definir el esquema de la tabla "Socios"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Socios (
        ID_Socio INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT,
        Apellido TEXT,
        Dirección TEXT,
        Teléfono TEXT,
        Email TEXT
    )
''')

# Definir el esquema de la tabla "Libros"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Libros (
        ID_Libro INTEGER PRIMARY KEY AUTOINCREMENT,
        Código TEXT,
        Título TEXT,
        Precio_Reposición REAL,
        Estado TEXT
    )
''')

# Definir el esquema de la tabla "Préstamos"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Préstamos (
        ID_Préstamo INTEGER PRIMARY KEY AUTOINCREMENT,
        ID_Libro INTEGER,
        ID_Socio INTEGER,
        Fecha_Prestamo DATE,
        Fecha_Devolución_Pactada DATE,
        FOREIGN KEY (ID_Libro) REFERENCES Libros(ID_Libro),
        FOREIGN KEY (ID_Socio) REFERENCES Socios(ID_Socio)
    )
''')

# Definir el esquema de la tabla "Devoluciones"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Devoluciones (
        ID_Devolución INTEGER PRIMARY KEY AUTOINCREMENT,
        ID_Préstamo INTEGER,
        Fecha_Devolución_Real DATE,
        Retraso INTEGER,
        FOREIGN KEY (ID_Préstamo) REFERENCES Préstamos(ID_Préstamo)
    )
''')

# Definir el esquema de la tabla "Extravíos"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Extravíos (
        ID_Extravío INTEGER PRIMARY KEY AUTOINCREMENT,
        ID_Libro INTEGER,
        Fecha_Extravío DATE,
        FOREIGN KEY (ID_Libro) REFERENCES Libros(ID_Libro)
    )
''')

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()
