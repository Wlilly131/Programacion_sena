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





# ==============================
# EJEMPLO DE LISTA EN PYTHON
# ==============================
#creamor una lista con varias frutas
frutas = ["manzana", "banana", "cereza",]#lista con tres elementos
print(frutas) #imprimir la lista completa 
#__________________________________
#Acceder a cada elemento de la lista por su posicion 
print(frutas[0]) #imprimir el primer elemento de la lista
print(frutas[1]) #imprimir el segundo elemento de la lista  

#__________________________________
#Modificar un elemento de la lista
frutas[1] = "naranja" #cambiar el segundo elemento de la lista
#cambiamos banana por naranja 
print(frutas) #imprimir la lista modificada
#__________________________________
#Agregar un elemento al final de la lista
frutas.append("uva") #agregar uva al final de la lista  
print(frutas) #imprimir la lista con el nuevo elemento
frutas.append("kiwi") #agregar kiwi al final de la lista  
print(frutas) #imprimir la lista con el nuevo elemento
#__________________________________
#Insertar un elemento en una posicion especifica
frutas.insert(1, "fresa") #insertar fresa en la posicion 1
print(frutas) #imprimir la lista con el nuevo elemento  
#__________________________________
#Eliminar un elemento de la lista por su valor
frutas.remove("cereza") #eliminar cereza de la lista        
print(frutas) #imprimir la lista sin cereza
#__________________________________
#Eliminar un elemento de la lista por su posicion   
del frutas[0] #eliminar el primer elemento de la lista
print(frutas) #imprimir la lista sin el primer elemento
#__________________________________
#Eliminar el ultimo elemento de la lista
frutas.pop() #eliminar el ultimo elemento de la lista   
print(frutas) #imprimir la lista sin el ultimo elemento
#__________________________________ 
#Recorrer la lista con un buclae for
for fruta in frutas: #para cada fruta en la lista frutas
    print("me gusta comer" ,fruta) #imprimir la fruta
#


# ==============================
# EJEMPLO DE TUPLA EN PYTHON
# ==============================

# Creamos una tupla con colores
colores = ("rojo", "verde", "azul")  # Tupla con 3 elementos

print(colores)  # Mostramos la tupla completa

# Acceder a elementos por índice
print(colores[0])  # Muestra "rojo"
print(colores[2])  # Muestra "azul"

# Las tuplas son inmutables, así que esto daría error:
# colores[1] = "amarillo"  # ❌ No se puede cambiar

# Podemos recorrer la tupla con un bucle for
for color in colores:  # 'color' toma cada valor de la tupla
    print("Mi color favorito es", color)

# Si queremos cambiar algo, debemos crear una nueva tupla
nueva_tupla = colores + ("amarillo",)  # Creamos una nueva tupla añadiendo "amarillo"
print(nueva_tupla)

# También podemos desempaquetar la tupla en variables
rojo, verde, azul = colores  # Asigna cada valor a una variable diferente
print("Rojo:", rojo)
print("Verde:", verde)
print("Azul:", azul)