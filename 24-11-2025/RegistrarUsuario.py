import csv

def registrar_usuario(id_nuevo, nombre, apellido, edad, estado_civil):
    """
    Agrega un nuevo usuario al final del archivo 'datos.csv'.
    """
    # 1. Validación simple para asegurar que el ID es un número (o al menos convertible)
    try:
        id_nuevo = int(id_nuevo) 
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return

    try:
        # Abrimos el archivo en modo 'a' (append/añadir) para agregar al final.
        with open('datos.csv', 'a', newline='') as archivo_salida:
            escritor = csv.writer(archivo_salida)
            
            # Preparamos la nueva fila de datos
            # Aseguramos que 'edad' sea un entero, aunque el CSV lo guardará como texto
            try:
                edad = int(edad)
            except ValueError:
                print("Error: La edad debe ser un número entero.")
                return
                
            nuevo_registro = [id_nuevo, nombre, apellido, edad, estado_civil]
            
            # Escribimos la fila en el archivo
            escritor.writerow(nuevo_registro)
            
        print(f"\n✅ Usuario con ID {id_nuevo} registrado exitosamente.")
        
    except FileNotFoundError:
        print(f"\n❌ Error: El archivo 'datos.csv' no fue encontrado. Asegúrate de ejecutar BD.py primero.")
    except Exception as e:
        print(f"\n❌ Ocurrió un error al registrar el usuario: {e}")

# --- Bloque Principal para Ejecución desde Consola ---
if __name__ == "__main__":
    print("--- 👤 REGISTRO DE NUEVO USUARIO ---")
    
    # Solicitamos los datos del nuevo usuario usando input()
    print("Por favor, ingrese los siguientes datos:")
    
    # Los datos se recogen como cadenas de texto (str)
    nuevo_id = input("ID (Solo números): ")
    nuevo_nombre = input("Nombre: ")
    nuevo_apellido = input("Apellido: ")
    nueva_edad = input("Edad (Solo números): ")
    nuevo_estado_civil = input("Estado Civil: ")
    
    # Llamamos a la función con los datos recolectados
    registrar_usuario(nuevo_id, nuevo_nombre, nuevo_apellido, nueva_edad, nuevo_estado_civil)
    
    print("\n----------------------------------")
    print("💡 Ejecuta MostrarUsuarios.py para verificar el nuevo registro.")