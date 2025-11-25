import csv

def mostrar_usuarios():
    """
    Lee y muestra todos los usuarios del archivo 'datos.csv'.
    """
    try:
        # Abrimos el archivo en modo 'r' (read/lectura)
        with open('datos.csv', 'r', newline='') as archivo_entrada:
            lector = csv.reader(archivo_entrada)
            
            print("\n=======================================================")
            print("         LISTA COMPLETA DE USUARIOS EN datos.csv       ")
            print("=======================================================")
            
            # Iteramos sobre cada fila del archivo CSV
            for i, fila in enumerate(lector):
                # La primera fila es el encabezado
                if i == 0:
                    # Usamos join para imprimir el encabezado separado por |
                    print(f"| {' | '.join(fila)} |")
                    print("-------------------------------------------------------")
                else:
                    # Formateamos la fila de datos
                    print(f"| {fila[0]:<4} | {fila[1]:<10} | {fila[2]:<10} | {fila[3]:<4} | {fila[4]:<15} |")

            print("=======================================================\n")
            
    except FileNotFoundError:
        print(f"Error: El archivo 'datos.csv' no fue encontrado. Asegúrate de ejecutar BD.py primero.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

# --- Ejemplo de uso ---
if __name__ == "__main__":
    mostrar_usuarios()