import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import requests
import random

# Ejemplo de lógica de extracción
def main():
    print("Iniciando proceso ETL...")

    # Conexión a SQLite
    conn = sqlite3.connect('bebidas_ventas.db')
    cursor = conn.cursor()

    try:
        # Crear tablas si no existen
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Bebidas (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            categoria TEXT,
            alcoholica TEXT,
            tipo_vaso TEXT
        );
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Ventas (
            id INTEGER PRIMARY KEY,
            bebida_id INTEGER,
            pais TEXT,
            ciudad TEXT,
            bar TEXT,
            fecha TEXT,
            cantidad INTEGER,
            precio REAL,
            FOREIGN KEY(bebida_id) REFERENCES Bebidas(id)
        );
        """)
        conn.commit()
       


        # Obtener países y ciudades desde la API dentro del main
        print("Obteniendo datos de países y ciudades...")
        url = "https://restcountries.com/v3.1/all"
        response = requests.get(url)
        if response.status_code == 200:
            countries = response.json()
            country_city_pairs = {
                country.get("name", {}).get("common", "Unknown"): country.get("capital", ["Unknown"])[0]
                for country in countries if "capital" in country
            }
            
        else:
            print(f"Error al obtener datos de países: {response.status_code}")
            return  # Salir si no se pueden obtener datos


        paises = list(country_city_pairs.keys())  # Lista de países
        ciudades = country_city_pairs           # Diccionario país -> ciudad (capital)

        # Agregar 20 bebidas a la base de datos
        for _ in range(20):  # 20 bebidas
            response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/random.php")
            data = response.json()
            if data and "drinks" in data:
                bebida = data['drinks'][0]
                nombre = bebida.get('strDrink', 'Desconocido')
                categoria = bebida.get('strCategory', 'Desconocida')
                alcoholica = bebida.get('strAlcoholic', 'Desconocida')
                tipo_vaso = bebida.get('strGlass', 'Desconocido')

                # Insertar bebida en la tabla Bebidas
                cursor.execute("INSERT INTO Bebidas (nombre, categoria, alcoholica, tipo_vaso) VALUES (?, ?, ?, ?)",
                               (nombre, categoria, alcoholica, tipo_vaso))
                bebida_id = cursor.lastrowid

                # Simular ventas para cada bebida
                for _ in range(random.randint(5, 10)):  # Entre 5 y 10 ventas por bebida
                    pais = random.choice(paises)
                    ciudad = ciudades[pais]  # Capital del país
                    bar = f"Bar {random.randint(1, 20)}"
                    fecha = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")
                    cantidad = random.randint(1, 300)
                    precio = round(random.uniform(5, 20), 2)

                    cursor.execute(
                        "INSERT INTO Ventas (bebida_id, pais, ciudad, bar, fecha, cantidad, precio) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (bebida_id, pais, ciudad, bar, fecha, cantidad, precio))

        conn.commit()

        # Leer las tablas con pandas
        global bebidas, ventas
        bebidas = pd.read_sql_query("SELECT * FROM Bebidas", conn)
        ventas = pd.read_sql_query("SELECT * FROM Ventas", conn)

    except sqlite3.OperationalError as e:
        print(f"Error operativo en SQLite: {e}")
    finally:
        # Cerrar conexión
        conn.close()
        print("Conexión a la base de datos cerrada.")

    print("ETL finalizado.")


if __name__ == "__main__":
    main()