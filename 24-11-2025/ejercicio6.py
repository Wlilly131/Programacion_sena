#------------FUNCIONES-----------
#--------------------------------
usuarios = []
def agregar_usuarios ():
    id = int(input("Ingrese su identificacion: "))
    nombre = input("ingrese nombre: ").lower()
    apellido = input("ingrese su apellido: ").lower()
    edad = int(input("ingrese su edad: "))
    estado_civil = input("Ingrese su estado civil: ").lower()
    
    usuario = {
        "id": id,
        "nombre": nombre, 
        "apellido": apellido,
        "edad": edad,
        "estado_civil": estado_civil,
    }

    usuarios.append(usuario)
    print ("usuario agregado correctamente")

agregar_usuarios()
print(usuarios)