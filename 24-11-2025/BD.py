import csv # importa la libreria csv para manejar archivos CSV
#CreAR UN ARCHIVO PARA ALMACENAR DATOS
with open('datos.csv', 'w', newline='') as archivo:
    escritor = csv.writer(archivo) # crea un objeto escritor para escribir en el archivo CSV
    #escribir el nombre de las columnas
    escritor.writerow(['ID', 'Nombre', 'Apellido', 'Edad', 'Estado Civil'])#ejemplo de datos para agregar al archivo CSV
    escritor.writerow([123, "Ana","perez",18, "Soltera"])
    escritor.writerow([456, "Luis","gomez",25, "Casado"])
    escritor.writerow([789, "Maria","lopez",30, "Divorciada"])          