import csv
import os

# --- 1. CONFIGURACIÓN INICIAL (Función de BD.py) ---
def inicializar_bd():
    """Crea el archivo datos.csv con un encabezado si no existe, o lo sobrescribe."""
    try:
        # Intentar leer primero para ver si ya tiene datos
        with open('datos.csv', 'r', newline='') as archivo:
            # Si el archivo existe y tiene al menos una línea (el encabezado), no hacemos nada
            # Podríamos chequear si la primera línea es el encabezado, pero por simplicidad omitiremos la lectura
            pass 
        print("La base de datos (datos.csv) ya existe.")
    except FileNotFoundError:
        # Si el archivo no existe, lo creamos y agregamos datos iniciales
        with open('datos.csv', 'w', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(['ID', 'Nombre', 'Apellido', 'Edad', 'Estado Civil'])
            # Ejemplo de datos iniciales
            escritor.writerow([123, "Ana", "perez", 18, "Soltera"])
            escritor.writerow([456, "Luis", "gomez", 25, "Casado"])
            escritor.writerow([789, "Maria", "lopez", 30, "Divorciada"]) 
        print("La base de datos (datos.csv) ha sido creada con datos iniciales.")
    print("-------------------------------------------------")


# --- 2. FUNCIONES CRUD (Registrar, Actualizar, Borrar, Mostrar) ---

# 2.1. REGISTRAR USUARIO (Función de RegistrarUsuario.py)
def registrar_usuario():
    print("\n--- 👤 REGISTRO DE NUEVO USUARIO ---")
    try:
        nuevo_id = input("ID (Solo números): ")
        if not nuevo_id.isdigit():
            print("❌ Error: El ID debe ser un número entero.")
            return

        nuevo_nombre = input("Nombre: ")
        nuevo_apellido = input("Apellido: ")
        nueva_edad = input("Edad (Solo números): ")
        
        if not nueva_edad.isdigit():
            print("❌ Error: La edad debe ser un número entero.")
            return
            
        nuevo_estado_civil = input("Estado Civil: ")
        
        # Opcional: Validación para evitar IDs duplicados
        if verificar_id_existe(nuevo_id):
            print(f"⚠️ Error: El ID {nuevo_id} ya existe. No se registró el usuario.")
            return

        with open('datos.csv', 'a', newline='') as archivo_salida:
            escritor = csv.writer(archivo_salida)
            nuevo_registro = [nuevo_id, nuevo_nombre, nuevo_apellido, int(nueva_edad), nuevo_estado_civil]
            escritor.writerow(nuevo_registro)
            
        print(f"\n✅ Usuario con ID {nuevo_id} registrado exitosamente.")
        
    except FileNotFoundError:
        print("\n❌ Error: El archivo 'datos.csv' no fue encontrado.")
    except Exception as e:
        print(f"\n❌ Ocurrió un error al registrar el usuario: {e}")

# Función auxiliar para verificar si un ID ya está en el archivo
def verificar_id_existe(id_a_verificar):
    try:
        with open('datos.csv', 'r', newline='') as archivo_entrada:
            lector = csv.reader(archivo_entrada)
            next(lector) # Saltar el encabezado
            for fila in lector:
                if fila and str(fila[0]) == str(id_a_verificar):
                    return True
        return False
    except FileNotFoundError:
        return False # No existe el archivo, entonces no existe el ID


# 2.2. ACTUALIZAR USUARIO (Función de ActualizarUsuarios.py)
def actualizar_usuario():
    print("\n--- 🔄 ACTUALIZAR USUARIO POR ID ---")
    mostrar_usuarios(False) # Mostrar la lista sin el encabezado
    
    id_a_modificar = input("\nIngrese el ID del usuario a modificar (solo números): ")

    if not id_a_modificar.isdigit():
        print("❌ ID no válido. La operación de actualización fue cancelada.")
        return

    filas = []
    encontrado = False
    
    try:
        with open('datos.csv', 'r', newline='') as archivo_entrada:
            lector = csv.reader(archivo_entrada)
            
            # Recorremos el archivo para encontrar el ID
            for fila in lector:
                if fila[0] == 'ID':
                    filas.append(fila) # Guardamos el encabezado
                elif fila[0] == id_a_modificar:
                    encontrado = True
                    print(f"\n-- Ingresando NUEVOS datos para ID {id_a_modificar} --")
                    
                    nuevo_nombre = input(f"Nuevo Nombre (Actual: {fila[1]}): ")
                    nuevo_apellido = input(f"Nuevo Apellido (Actual: {fila[2]}): ")
                    nueva_edad = input(f"Nueva Edad (Actual: {fila[3]}): ")
                    nuevo_estado_civil = input(f"Nuevo Estado Civil (Actual: {fila[4]}): ")
                    
                    # Validación de edad antes de guardar
                    if not nueva_edad.isdigit():
                        print("❌ Error: La nueva edad debe ser un número entero. Cancelando actualización.")
                        filas.append(fila) # Volver a agregar la fila original
                        continue
                        
                    fila_actualizada = [
                        id_a_modificar, 
                        nuevo_nombre, 
                        nuevo_apellido, 
                        int(nueva_edad), 
                        nuevo_estado_civil
                    ]
                    filas.append(fila_actualizada)
                else:
                    filas.append(fila) # Guardamos las demás filas sin cambio

        if not encontrado:
            print(f"\n⚠️ No se encontró un usuario con el ID {id_a_modificar} para actualizar.")
            return

        with open('datos.csv', 'w', newline='') as archivo_salida:
            escritor = csv.writer(archivo_salida)
            escritor.writerows(filas)
            
        print(f"\n✅ Usuario con ID {id_a_modificar} actualizado exitosamente.")
        
    except PermissionError:
        print("\n❌ PermissionError: No se pudo escribir en 'datos.csv'. Asegúrate de que el archivo no esté abierto.")
    except FileNotFoundError:
        print("\n❌ Error: El archivo 'datos.csv' no fue encontrado.")
    except Exception as e:
        print(f"\n❌ Ocurrió un error: {e}")


# 2.3. BORRAR USUARIO (Función de BorrarUsuarios.py)
def eliminar_usuario():
    print("\n--- 🗑️ ELIMINAR USUARIO POR ID ---")
    mostrar_usuarios(False) # Mostrar la lista sin el encabezado
    
    id_a_eliminar = input("\nIngrese el ID del usuario que desea eliminar (solo números): ")
    
    try:
        if not id_a_eliminar.isdigit():
            print("\n❌ Error: El ID ingresado no es un número válido.")
            return
            
        id_a_eliminar = str(id_a_eliminar)
        filas = []
        encontrado = False

        with open('datos.csv', 'r', newline='') as archivo_entrada:
            lector = csv.reader(archivo_entrada)
            
            for fila in lector:
                if fila[0] == 'ID': # Guardar el encabezado
                    filas.append(fila)
                elif fila[0] != id_a_eliminar:
                    filas.append(fila) # Guardar las filas que NO queremos borrar
                else:
                    encontrado = True
        
        if not encontrado:
            print(f"\n⚠️ No se encontró un usuario con el ID {id_a_eliminar} para eliminar.")
            return

        with open('datos.csv', 'w', newline='') as archivo_salida:
            escritor = csv.writer(archivo_salida)
            escritor.writerows(filas)
            
        print(f"\n✅ Usuario con ID {id_a_eliminar} eliminado exitosamente.")

    except PermissionError:
        print("\n❌ PermissionError: No se pudo escribir en 'datos.csv'. Asegúrate de que el archivo no esté abierto.")
    except FileNotFoundError:
        print(f"\n❌ Error: El archivo 'datos.csv' no fue encontrado.")
    except Exception as e:
        print(f"\n❌ Ocurrió un error: {e}")


# 2.4. MOSTRAR USUARIOS (Función de MostrarUsuarios.py)
def mostrar_usuarios(mostrar_titulo=True):
    """Lee y muestra todos los usuarios del archivo 'datos.csv'."""
    try:
        with open('datos.csv', 'r', newline='') as archivo_entrada:
            lector = csv.reader(archivo_entrada)
            
            if mostrar_titulo:
                print("\n=======================================================")
                print("         LISTA COMPLETA DE USUARIOS EN datos.csv       ")
                print("=======================================================")
            
            # Iteramos sobre cada fila del archivo CSV
            for i, fila in enumerate(lector):
                if not fila: continue # Omitir filas vacías
                
                # Intentamos formatear la salida (asumimos 5 columnas)
                try:
                    if i == 0:
                        # Encabezado
                        print(f"| {fila[0]:<4} | {fila[1]:<10} | {fila[2]:<10} | {fila[3]:<4} | {fila[4]:<15} |")
                        print("-------------------------------------------------------")
                    else:
                        # Datos
                        print(f"| {fila[0]:<4} | {fila[1]:<10} | {fila[2]:<10} | {fila[3]:<4} | {fila[4]:<15} |")
                except IndexError:
                    # En caso de que una fila tenga un formato incorrecto
                    print(f"| ERROR en la Fila {i+1}: {fila} |")

            if mostrar_titulo:
                 print("=======================================================\n")
            
    except FileNotFoundError:
        print(f"\n❌ Error: El archivo 'datos.csv' no fue encontrado. Ejecuta la opción 0 o reinicia el programa.")
    except Exception as e:
        print(f"\n❌ Ocurrió un error al leer el archivo: {e}")

# --- 3. MENÚ PRINCIPAL Y LÓGICA DE CONTROL ---

def menu_principal():
    """Muestra el menú y maneja la selección del usuario."""
    
    inicializar_bd() # Asegurar que el archivo exista al iniciar
    
    while True:
        print("\n*************************************************")
        print("* SISTEMA DE GESTIÓN DE USUARIOS          *")
        print("*************************************************")
        print("1. ➕ Registrar Nuevo Usuario")
        print("2. ✏️  Actualizar Usuario (por ID)")
        print("3. 🗑️  Borrar Usuario (por ID)")
        print("4. 📋 Mostrar Todos los Usuarios")
        print("0. 🚪 Salir")
        print("-------------------------------------------------")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            actualizar_usuario()
        elif opcion == '3':
            eliminar_usuario()
        elif opcion == '4':
            mostrar_usuarios()
        elif opcion == '0':
            print("\n👋 ¡Gracias por usar el sistema! Saliendo...")
            break
        else:
            print("\n⚠️ Opción no válida. Intente de nuevo.")


# Ejecutar el menú al iniciar el script
if __name__ == "__main__":
    menu_principal()