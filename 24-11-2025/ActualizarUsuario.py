import csv

def actualizar_usuario(id_a_actualizar, nuevo_nombre, nuevo_apellido, nueva_edad, nuevo_estado_civil):
    """
    Actualiza los datos de un usuario en 'datos.csv' por su ID.
    """
    filas = []
    encontrado = False
    
    # 1. Validación simple del ID a actualizar
    try:
        id_a_actualizar = str(int(id_a_actualizar))
    except ValueError:
        print("\n❌ Error: El ID ingresado para buscar debe ser un número entero.")
        return
        
    # 2. Validación simple de la nueva Edad
    try:
        # Intentamos convertir la edad a entero para guardarla
        nueva_edad_int = int(nueva_edad)
    except ValueError:
        print("\n❌ Error: La nueva edad debe ser un número entero.")
        return

    # 3. Leer todas las filas y modificar la que coincida con el ID
    try:
        with open('datos.csv', 'r', newline='') as archivo_entrada:
            lector = csv.reader(archivo_entrada)
            
            for fila in lector:
                # Si es el encabezado ('ID') o si el ID NO coincide, la guardamos tal cual
                if fila[0] == 'ID' or fila[0] != id_a_actualizar:
                    filas.append(fila)
                # Si el ID coincide, creamos la nueva fila con los datos actualizados
                else:
                    fila_actualizada = [
                        id_a_actualizar, 
                        nuevo_nombre, 
                        nuevo_apellido, 
                        nueva_edad_int, # Usamos la edad convertida a entero
                        nuevo_estado_civil
                    ]
                    filas.append(fila_actualizada)
                    encontrado = True
                    
    except FileNotFoundError:
        print(f"\n❌ Error: El archivo 'datos.csv' no fue encontrado.")
        return

    # 4. Escribir el archivo actualizado si se encontró el usuario
    if not encontrado:
        print(f"\n⚠️ No se encontró un usuario con el ID {id_a_actualizar} para actualizar.")
        return

    try:
        with open('datos.csv', 'w', newline='') as archivo_salida:
            escritor = csv.writer(archivo_salida)
            escritor.writerows(filas)
            
        print(f"\n✅ Usuario con ID {id_a_actualizar} actualizado exitosamente.")
    except PermissionError:
        print("\n❌ PermissionError: No se pudo escribir en 'datos.csv'. Asegúrate de que el archivo no esté abierto en otro programa.")
    except Exception as e:
        print(f"\n❌ Ocurrió un error al escribir el archivo: {e}")

# --- Bloque Principal para Ejecución desde Consola ---
if __name__ == "__main__":
    print("--- 🔄 ACTUALIZAR USUARIO POR ID ---")
    
    # 1. Mostrar usuarios (opcional, pero útil)
    try:
        with open('datos.csv', 'r', newline='') as f:
            print("\nUsuarios actuales:\n" + f.read().strip())
    except FileNotFoundError:
        print("El archivo 'datos.csv' aún no existe. Ejecuta BD.py.")
        exit() # Salir si no existe el archivo
        
    # 2. Solicitar el ID a actualizar
    id_a_modificar = input("\nIngrese el ID del usuario a modificar (solo números): ")
    
    # Si el ID es válido, pedimos los nuevos datos
    if id_a_modificar.isdigit():
        print(f"\n-- Ingresando NUEVOS datos para ID {id_a_modificar} --")
        
        # Recogemos los nuevos valores
        nuevo_nombre = input("Nuevo Nombre: ")
        nuevo_apellido = input("Nuevo Apellido: ")
        nueva_edad = input("Nueva Edad (Solo números): ")
        nuevo_estado_civil = input("Nuevo Estado Civil: ")
        
        # Llamamos a la función de actualización
        actualizar_usuario(id_a_modificar, nuevo_nombre, nuevo_apellido, nueva_edad, nuevo_estado_civil)
    else:
        print("\n❌ ID no válido. La operación de actualización fue cancelada.")
        
    print("\n----------------------------------")
    print("💡 Ejecuta MostrarUsuarios.py para verificar los cambios.")