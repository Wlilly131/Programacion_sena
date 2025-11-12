#listas en python
# Las listas son datos que tiene como caracteristicas ser mutables - las listas son ordenadas
#Las listas se definen con llaves []
estudiantes = ["William", "Zuleta", "David", "Miller"]
print(estudiantes) # imprimir lista
print(len(estudiantes)) # imprimir cantidad de datos de la lista
print(estudiantes) # imprimir la posicion 2 de la lista
estudiantes[2] = "Antonio" # modificar o mutar una lista
print(estudiantes) #modificar o mutar una lista
estudiantes.append("Carlos") #appen sirve para agregar un nuevo objeto a la lista
print(estudiantes)
estudiantes.remove("Zuleta") # remove sirve para borrar un elemento de la lista
print(estudiantes)


del estudiantes[0]
print(estudiantes)
print("Mostrar todas las frutas")
print("Prueba 2 git")
for estudiantes in estudiantes:
  print("", estudiantes)

#____________tuplas----------
#las tuplas son ordenadas
#las tuplas no son mutables
#Las tuplas se definen con parentesis ()

equipos = ("Nacional", "Millonarios", "Santa Fe", "Junior")
print(equipos)
print("El quipo es", equipos[3])
