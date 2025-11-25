import csv
import os

def actualizar_usuario(id_a_actualizar, nuevo_nombre, nuevo_apellido, nueva_edad, nuevo_estado_civil):
    """
    Actualiza los datos de un usuario en 'datos.csv' por su ID.
    """
    filas = []
    encontrado = False
    
    # 1. Leer todas las filas y modificar la que coincida con el ID
    try:
        with open('datos.csv', 'r', newline='') as archivo_entrada:
            lector = csv.reader(archivo_entrada)
            
            for fila in lector:
                # Si es la fila de encabezado o el ID NO coincide, la guardamos tal cual
                if fila[0] == 'ID' or str(fila[0]) != str(id_a_actualizar):
                    filas.append(fila)
                # Si el ID coincide, creamos la nueva fila con los datos actualizados
                else:
                    fila_actualizada = [
                        id_a_actualizar, 
                        nuevo_nombre, 
                        nuevo_apellido, 
                        nueva_edad, 
                        nuevo_estado_civil
                    ]
                    filas.append(fila_actualizada)
                    encontrado = True
                    
    except FileNotFoundError:
        print(f"Error: El archivo 'datos.csv' no fue encontrado.")
        return

    # Si no se encontró el ID, informamos y salimos
    if not encontrado:
        print(f"No se encontró un usuario con el ID {id_a_actualizar} para actualizar.")
        return

    # 2. Escribir todas las filas (incluida la actualizada) de vuelta al archivo
    with open('datos.csv', 'w', newline='') as archivo_salida:
        escritor = csv.writer(archivo_salida)
        escritor.writerows(filas)
        
    print(f"Usuario con ID {id_a_actualizar} actualizado exitosamente.")

# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Asegúrate de que BD.py se haya ejecutado al menos una vez
    print("Contenido antes de la actualización:")
    try:
        with open('datos.csv', 'r', newline='') as f:
            print(f.read())
    except FileNotFoundError:
        print("El archivo 'datos.csv' aún no existe.")

    # Intenta actualizar el usuario con ID 123 (Ana)
    actualizar_usuario(123, "Anabella", "Perez-Garcia", 20, "Comprometida")
    
    print("\nContenido después de la actualización:")
    try:
        with open('datos.csv', 'r', newline='') as f:
            print(f.read())
    except FileNotFoundError:
        pass