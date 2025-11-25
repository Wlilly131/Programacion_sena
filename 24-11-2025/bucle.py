#2 tipos de bucles: for y by 
#========Control=========
#Ciclo o bucle for
for i in range (1,6):
    print(i)
lista = ["melon", "pera", "manzana", "uva", "fresa"]
for fruta in lista:
    print(fruta)
#=========While=========
contador = 1
while contador <= 10:
    print(contador)
    contador += 1
#=========IF=========
numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

edad_usuario = int(input("Ingrese su edad: "))
if edad_usuario < 18:
    print("No puedes pasar")
elif edad_usuario >100:
    print("Edad incorrecta")
else:
    print("Puedes pasar")