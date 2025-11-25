import csv
import os # Importar 'os' para manejar archivos, útil para renombrar/eliminar

def eliminar_usuario(id_a_eliminar):
    """
    Elimina un usuario del archivo 'datos.csv' por su ID.
    """
    filas = []
    # 1. Leer todas las filas excepto la que tiene el ID a eliminar
    try:
        with open('datos.csv', 'r', newline='') as archivo_entrada:
            lector = csv.reader(archivo_entrada)
            # Guardar el encabezado
            encabezado = next(lector)
            filas.append(encabezado)
            
            # Recorrer las filas de datos
            encontrado = False
            for fila in lector:
                # Comprobar si el primer elemento (ID) coincide con el ID a eliminar
                # Convertimos a string por si el ID en el CSV es un string
                if str(fila[0]) != str(id_a_eliminar):
                    filas.append(fila)
                else:
                    encontrado = True
    
    except FileNotFoundError:
        print(f"Error: El archivo 'datos.csv' no fue encontrado.")
        return

    # Si no se encontró el ID, informamos y salimos
    if not encontrado and len(filas) > 1: # len > 1 porque el encabezado siempre está
        print(f"No se encontró un usuario con el ID {id_a_eliminar}.")
        return

    # 2. Escribir las filas restantes de vuelta al archivo
    # Usamos 'w' para sobrescribir completamente el archivo
    with open('datos.csv', 'w', newline='') as archivo_salida:
        escritor = csv.writer(archivo_salida)
        escritor.writerows(filas)
        
    print(f"Usuario con ID {id_a_eliminar} eliminado exitosamente (o no encontrado).")

# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Asegúrate de que BD.py se haya ejecutado al menos una vez para crear datos.csv
    print("Contenido antes de la eliminación:")
    # Función simple para mostrar el contenido (no es necesario que esté en el módulo)
    try:
        with open('datos.csv', 'r', newline='') as f:
            print(f.read())
    except FileNotFoundError:
        print("El archivo 'datos.csv' aún no existe.")
    
    # Intenta eliminar el usuario con ID 456 (Luis)
    eliminar_usuario(456)
    
    print("\nContenido después de la eliminación:")
    try:
        with open('datos.csv', 'r', newline='') as f:
            print(f.read())
    except FileNotFoundError:
        pass