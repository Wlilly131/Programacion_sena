#======================================
# 1. Contar cuántos caracteres tiene la frase (incluyendo espacios)
frase = "Hola mundo"
print(len(frase))
# 2. Convertir el nombre a mayúsculas
nombre = "juan perez"
print(nombre.upper())
# 3. Contar cuántas veces aparece la letra "a" en el texto
texto = "La casa está vacía"
print(texto.count("a"))
# 4. Mostrar la palabra repetida 5 veces, separada por espacios
palabra = "Python"
print ((palabra + (" "))*5)
# 5. Mostrar la última letra de la cadena
mensaje = "Programación"
print(mensaje[(len(mensaje)-1)])
# 6. Mostrar la cadena al revés
cadena = "Hola Mundo"
print(cadena[::-1])
# 7. Reemplazar "Java" por "Python" en la frase
frase = "Me gusta Java"
print(frase.replace("Java","Python"))
# 8. Mostrar solo los primeros 4 caracteres del título
titulo = "Introducción"
print(titulo[:4])
# 9. Contar cuántas palabras tiene la oración (separadas por espacios)
oracion = "Python es divertido"
palabras = oracion.split()
cantidad = len(palabras)
print("La oracion Python es divertido tiene:", cantidad, "palabras")
# 10. Convertir la cadena a formato título → "El Señor De Los Anillos"
libro = "el señor de los anillos"
print(libro.title())
# 11. Quitar los espacios en blanco al inicio y al final del saludo
saludo = "   Hola mundo   "
saludo_limpio = saludo.strip()
print("Antes:", saludo)
print("Después:", saludo_limpio)
# 12. Verificar si la cadena contiene solo letras (sin números ni símbolos)
codigo = "Python3"

# 13. Mostrar las iniciales del nombre completo → "C.A.G."
nombre_completo = "Carlos Alberto García"
print(nombre_completo.strip())
# 14. Reemplazar las vocales con "_" (guion bajo)
frase = "Estoy aprendiendo Python"
for vocal in "aeiouAEIOU":
    frase = frase.replace(vocal, "_")
print(frase)
# 15. Crear un nombre de usuario con las 2 primeras letras del nombre + 3 últimas del apellido, en minúsculas
nombre = "Luis"
apellido = "Martínez"
print(nombre.lower()[:2]+apellido.lower()[-3:])



nombre1 = "William"
nombre2 = "Ricardo"
apellido1 = "Sierra"
apellido2 = "Luna"
print(nombre1[0]+nombre2[0]+apellido1+apellido2[0]+"@sena.edu.co")