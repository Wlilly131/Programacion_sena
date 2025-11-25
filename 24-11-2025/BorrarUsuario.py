import csv
import os

def eliminar_usuario(id_a_eliminar):
    """
    Elimina un usuario del archivo 'datos.csv' por su ID, solicitado desde la consola.
    """
    filas = []
    encontrado = False

    # 1. Convertir y validar el ID a eliminar
    try:
        # Intentamos convertir el ID de entrada a entero para asegurar la consistencia.
        id_a_eliminar = str(int(id_a_eliminar))
    except ValueError:
        print("\n❌ Error: El ID ingresado no es un número válido.")
        return

    # 2. Leer todas las filas excepto la que tiene el ID a eliminar
    try:
        with open('datos.csv', 'r', newline='') as archivo_entrada:
            lector = csv.reader(archivo_entrada)
            
            # Recorrer las filas, guardando solo las que NO coinciden con el ID
            for fila in lector:
                # Comprobación: si el ID es el encabezado ('ID') O si el ID de la fila NO es el que queremos borrar.
                if fila[0] == 'ID' or fila[0] != id_a_eliminar:
                    filas.append(fila)
                else:
                    encontrado = True
    
    except FileNotFoundError:
        print(f"\n❌ Error: El archivo 'datos.csv' no fue encontrado.")
        return
    except IndexError:
        print("\n⚠️ Advertencia: Error de formato en alguna fila del archivo. Imposible eliminar.")
        return

    # Si no se encontró el ID, informamos y salimos
    if not encontrado:
        print(f"\n⚠️ No se encontró un usuario con el ID {id_a_eliminar} para eliminar.")
        return

    # 3. Escribir las filas restantes de vuelta al archivo
    # Esto sobrescribe el archivo, eliminando permanentemente la fila.
    try:
        with open('datos.csv', 'w', newline='') as archivo_salida:
            escritor = csv.writer(archivo_salida)
            escritor.writerows(filas)
            
        print(f"\n✅ Usuario con ID {id_a_eliminar} eliminado exitosamente.")
    except PermissionError:
        # Capturamos el error de permisos, ya que es el que has experimentado
        print("\n❌ PermissionError: No se pudo escribir en 'datos.csv'. Asegúrate de que el archivo no esté abierto en otro programa (como Excel) e intenta de nuevo.")
    except Exception as e:
        print(f"\n❌ Ocurrió un error al escribir el archivo: {e}")

# --- Bloque Principal para Ejecución desde Consola ---
if __name__ == "__main__":
    print("--- 🗑️ ELIMINAR USUARIO POR ID ---")
    
    # 1. Mostrar usuarios para que el usuario sepa qué ID borrar
    try:
        with open('datos.csv', 'r', newline='') as f:
            print("\nUsuarios actuales:\n" + f.read().strip())
    except FileNotFoundError:
        print("El archivo 'datos.csv' aún no existe.")
        
    # 2. Solicitar el ID a eliminar
    id_a_borrar = input("\nIngrese el ID del usuario que desea eliminar (solo números): ")
    
    # 3. Llamar a la función de eliminación
    if id_a_borrar:
        eliminar_usuario(id_a_borrar)
    
    print("\n----------------------------------")
    print("💡 Ejecuta MostrarUsuarios.py para verificar los cambios.")