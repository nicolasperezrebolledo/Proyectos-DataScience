import threading
import sys

# Agregar la ruta del directorio donde están los módulos
sys.path.append(r"C:\Users\npere\OneDrive\Desktop\Universidad_La_Salle\Clases\Semestre_1\Infraestructuras_de_computación\Evaluación\2_Entregable_2\proyecto_ETL")

# Importar las etapas del proceso ETL
from Extraction import *
from Transformations import *
from Load import *

def iniciar_servidor_web():
    webserver = WebServer()
    webserver.empty_assets_dir()  # Limpia los gráficos previos
    t1 = threading.Thread(target=webserver.run_webserver)
    t1.start()
    return webserver, t1

def menu_interactivo(webserver):
    while True:
        print("""---- MD002-AC1 MENU ----
1. Ejecutar ETL
2. Reiniciar Base de Datos
3. Salir
        """)
        option = input("Selecciona una opción: ")
        if option == '1':
            num_users = int(input("Ingrese el número de usuarios a extraer: "))
            extraction(num_users)
            transformation()
            webserver.empty_assets_dir()  # Limpia gráficos anteriores
        elif option == '2':
            reset_db()
            webserver.empty_assets_dir()  # Limpia gráficos
        elif option == '3':
            webserver.stop_webserver()  # Detiene el servidor
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

def main():
    print("Iniciando servidor web...")
    webserver, t1 = iniciar_servidor_web()
    try:
        menu_interactivo(webserver)
    finally:
        t1.join()  # Esperar a que termine el servidor web
        print("Servidor web detenido. Saliendo del programa.")

if __name__ == "__main__":
    main()

