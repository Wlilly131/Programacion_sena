#LISTAS EN PYTHON
#Las listas don datos que tienen como caracteristicas ser mutables
#las listas son ordenadas
#Las listas se definen con llaves []
#Ejemplo
estudiante = ["ERIK","ZULETA","ANGIE","KAROL","LEONARDO"]
print(estudiante) #Imprimir la lista
print(len(estudiante)) #imprimir la cantidads de datosa de la lista
print(estudiante[2]) #imprimir la posicion de la lista
estudiante[2] = "LORENA" #Modificar o mutar una lista
print(estudiante) # imprimir la lista nuevamente
estudiante.append("DIEGO") #appen sirve para agregar un objeto a la lista
print(estudiante) # imprimir lista
estudiante.remove("ERIK")#remove sirve para eliminar un objeto de la lista
print(estudiante)
del estudiante [3] #del sirve para eliminar una posicion
print(estudiante)
print("mostrar todas las frutaS")
for estudiante in estudiante:
    print(" ",estudiante)
#======================================
#===============TUPLAS=================
#======================================
#LAS TUPLAS SON ORDENADAS
#LAS TUPLAS NO SON MUTABLES
#LAS TUPLAS SE DEFINEN CON ()
equipos = ("nacional", "millonaros","santafe","junior","america","tolima")
print(equipos)
print("el equipo es ",equipos[3]) #muestra la posicion