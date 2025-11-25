#La cadena de caracteres se refiere a una serie de datos que ocuapan unespacio de memoria
#ejemplo a,1,?;Jm= y si se unen forman cadena de caracteres
#:::::::::::::::::::::::::::::::::::
print("Hola mundo")
print("Willam Sierra")
curso = "Programacion Uno"
universidad = "Sena"
print("Su curso es:", curso)
institucion = "Sena"
print("Su curso es:", curso, "y su institucion es:", institucion)
trimestre = 1
print("Su curso es:", curso, "y su institucion es:", institucion, "y su trimestre es:", trimestre)
print(len(institucion)) #el comando sirve para contar los caracteres de las variables
#:::::::::::::::::::::::::::::::::::
print(curso.upper()) #el comando upper sirve para poner las cadenas de texto en mayusculas
print(curso.lower()) #el comando lower sirve para poner las cadenas de texto en minusculas
#:::::::::::::::::::::::::::
print(institucion[0]) #Las corchetes extraen un caracter especifico de una cadena de texto en cierta posición
print(institucion[1])
print(institucion[2])
print(institucion[3])
#:::::::::::::::::::::
print(institucion[0:1]) #Los corchetes y los 2 puntos traen un rango de una cadena 
#::::::::::::::::::
#CONCATENAR
print((institucion + " " +curso).upper())
#COMPARAR UNA CADENA 
print(curso == institucion) #FALSO
print(institucion == universidad)
print("Analisis y desarrollo de sistemas".replace("sistemas","software"))