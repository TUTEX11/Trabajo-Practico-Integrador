from sqlite3 import *

def run():
    # Lista de 10 nombres
    nombres = ["Juan", "María", "Pedro", "Ana", "Luis", "Sofía", "Carlos", "Laura", "Diego", "Valentina"]

    # Lista de 10 apellidos
    apellidos = ["García", "Rodríguez", "González", "Fernández", "López", "Martínez", "Pérez", "Gómez", "Sánchez", "Díaz"]

    # Lista de 10 direcciones
    direcciones = ["Calle Falsa 123", "Avenida Principal 456", "Calle Principal 789", "Calle Ancha 234", "Avenida Estrecha 567",
                "Calle Larga 890", "Avenida Corta 123", "Calle Grande 456", "Avenida Pequeña 789", "Calle Circular 234"]

    # Lista de 10 números de teléfono
    numeros_telefono = ["1234567890", "2345678901", "3456789012", "4567890123", "5678901234",
                        "6789012345", "7890123456", "8901234567", "9012345678", "0123456789"]

    # Lista de 10 direcciones de correo electrónico
    emails = ["juan@example.com", "maria@example.com", "pedro@example.com", "ana@example.com", "luis@example.com",
            "sofia@example.com", "carlos@example.com", "laura@example.com", "diego@example.com", "valentina@example.com"]
    

    with connect('biblioteca.db') as conn:

        cur = conn.cursor()
        
        for i in range(len(nombres)):

            nombre = nombres[i]
            apellido = apellidos[i]
            direccion = direcciones[i]
            telefono = numeros_telefono[i]
            email = emails[i]

            cur.execute('INSERT INTO Socios (Nombre, Apellido, Dirección, Teléfono, Email) VALUES (?,?,?,?,?)', 
                        (nombre, apellido, direccion, telefono, email))
        


if __name__ == '__main__':
    run()