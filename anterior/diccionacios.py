
# ----------------------------------------------
# DICCIONARIOS Y SETS EN PYTHON - EXPLICACIÓN
# ----------------------------------------------

# DICCIONARIO:
# Un diccionario en Python es una colección no ordenada de elementos que se almacenan como pares clave-valor.
# Cada clave dentro del diccionario debe ser única, y se accede al valor a través de su clave.
# Los diccionarios se definen usando llaves {}, por ejemplo:
# persona = {"nombre": "Ana", "edad": 25}
# Son mutables (se pueden modificar), y muy útiles para representar objetos, registros, etc.

persona = {
    "ID":1,
    "Nombre":"Carlos",
    "Edad":30,
    "Profesion" : "Ingenierio"
}
print("El diccionario completo es: ", persona)
print("El nombre es : ", persona["Nombre"])
print("La edad es : ", persona["Edad"])
print("La profesion es : ", persona["Profesion"])
persona["Edad"] = 40
print("Edad persona", persona["Edad"])
persona["Ciudad"] = "Bogota"
print(persona["Ciudad"])